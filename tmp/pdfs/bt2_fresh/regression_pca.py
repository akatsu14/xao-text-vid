"""Bai tap 2: train/test, nested CV va tac dong cua PCA."""
import csv
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import scipy
import sklearn
from sklearn.base import clone
from sklearn.datasets import load_diabetes
from sklearn.decomposition import PCA
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

BASE = Path(__file__).resolve().parent
OUT = BASE / "ket_qua"
SEED = 68


def save_csv(name, rows):
    with (OUT / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def metrics(y, pred):
    return dict(MAE=float(mean_absolute_error(y, pred)),
                RMSE=float(np.sqrt(mean_squared_error(y, pred))),
                R2=float(r2_score(y, pred)))


def pipeline(reg, k=None):
    steps = [("impute", SimpleImputer(strategy="median")),
             ("scale", StandardScaler())]
    if k is not None:
        steps.append(("pca", PCA(n_components=k, svd_solver="full")))
    return Pipeline(steps + [("reg", reg)])


def candidates():
    a = {"reg__alpha": [0.1, 1, 10, 100]}
    s = {"reg__C": [10, 100, 1000], "reg__gamma": [0.01, 0.1]}
    ks = {"pca__n_components": [2, 4, 6, 8, 0.95]}
    return {
        "Mean": (pipeline(DummyRegressor(strategy="mean")), {}),
        "Linear": (pipeline(LinearRegression()), {}),
        "Ridge": (pipeline(Ridge(solver="svd")), a),
        "Ridge_PCA": (pipeline(Ridge(solver="svd"), 4), a | ks),
        "SVR": (pipeline(SVR(kernel="rbf", epsilon=0.1)), s),
        "SVR_PCA": (pipeline(SVR(kernel="rbf", epsilon=0.1), 4), s | ks)
    }


def tune(estimator, grid, x, y):
    if not grid:
        return clone(estimator).fit(x, y), {}
    search = GridSearchCV(
        clone(estimator), grid, scoring="neg_root_mean_squared_error",
        cv=KFold(3, shuffle=True, random_state=SEED + 1),
        n_jobs=1, error_score="raise", refit=True)
    search.fit(x, y)
    return search.best_estimator_, search.best_params_


def main():
    OUT.mkdir(exist_ok=True)
    data = load_diabetes(scaled=False)
    x, y = data.data, data.target
    ids = np.arange(len(y))
    train, test = train_test_split(ids, test_size=0.2, random_state=SEED)
    assert x.shape == (442, 10) and len(train) == 353 and len(test) == 89
    assert not set(train) & set(test)
    assert np.isfinite(x).all() and np.isfinite(y).all()
    xtr, ytr, xte, yte = x[train], y[train], x[test], y[test]
    for name, ix in [("train.csv", train), ("test.csv", test)]:
        save_csv(name, [dict(sample_id=int(i), **dict(zip(data.feature_names,
                 x[i].tolist())), target=float(y[i])) for i in ix])
    outer = list(KFold(5, shuffle=True, random_state=SEED + 2).split(xtr))
    save_csv("outer_folds.csv", [dict(sample_id=int(train[i]), fold=f + 1)
             for f, (_, va) in enumerate(outer) for i in va])
    definitions = candidates()
    fold_rows, summary, oof_rows = [], [], []
    for name, (estimator, grid) in definitions.items():
        model_rows = []
        for fold, (tr, va) in enumerate(outer, 1):
            fitted, params = tune(estimator, grid, xtr[tr], ytr[tr])
            pred = fitted.predict(xtr[va])
            row = dict(model=name, fold=fold, **metrics(ytr[va], pred))
            row["parameters"] = json.dumps(params, sort_keys=True)
            model_rows.append(row)
            oof_rows.extend(dict(model=name, sample_id=int(train[i]),
                                target=float(ytr[i]), prediction=float(p))
                            for i, p in zip(va, pred))
        fold_rows.extend(model_rows)
        summary.append(dict(model=name, **{
            f"{m}_{stat}": float(fn([r[m] for r in model_rows]))
            for m in ["MAE", "RMSE", "R2"]
            for stat, fn in [("mean", np.mean),
                             ("std", lambda v: np.std(v, ddof=1))]}))
        print(name, "CV RMSE", summary[-1]["RMSE_mean"], flush=True)
    # Chon ho mo hinh tu CV, truoc khi tinh ket qua Test.
    winner = min(summary, key=lambda r: (r["RMSE_mean"], r["MAE_mean"],
                 r["RMSE_std"], -r["R2_mean"]))["model"]
    save_csv("cv_folds.csv", fold_rows)
    save_csv("cv_summary.csv", summary)
    save_csv("oof_predictions.csv", oof_rows)
    (OUT / "selection.json").write_text(json.dumps(
        dict(winner=winner, criterion="CV RMSE mean; tie MAE, RMSE SD, R2"),
        indent=2), encoding="utf-8")
    final_rows, all_preds, final_params = [], {}, {}
    for name, (estimator, grid) in definitions.items():
        fitted, params = tune(estimator, grid, xtr, ytr)
        pred = fitted.predict(xte)
        all_preds[name] = pred.tolist()
        final_params[name] = params
        final_rows.append(dict(model=name, **metrics(yte, pred)))
        if name == winner:
            chosen = fitted
    # Kiem tra preprocessing chi fit tren Train.
    np.testing.assert_allclose(chosen.named_steps["impute"].statistics_,
                               np.median(xtr, axis=0))
    np.testing.assert_allclose(chosen.named_steps["scale"].mean_,
                               xtr.mean(axis=0))
    # PCA day du la phep quay; Ridge khong whitening phai tuong duong.
    direct = pipeline(Ridge(alpha=1, solver="svd")).fit(xtr, ytr)
    full = pipeline(Ridge(alpha=1, solver="svd"), 10).fit(xtr, ytr)
    rotation_error = float(np.max(np.abs(
        direct.predict(xte) - full.predict(xte))))
    assert rotation_error < 1e-7
    pca = full.named_steps["pca"]
    variance = np.cumsum(pca.explained_variance_ratio_)
    # Khao sat k rieng voi alpha=1, khong dung de chon lai winner.
    ablation = []
    for k in [2, 4, 6, 8, 10]:
        scores = []
        for tr, va in outer:
            fitted = pipeline(Ridge(alpha=1, solver="svd"), k)
            fitted.fit(xtr[tr], ytr[tr])
            scores.append(metrics(ytr[va], fitted.predict(xtr[va]))["RMSE"])
        ablation.append(dict(k=k, RMSE_mean=float(np.mean(scores)),
                            RMSE_std=float(np.std(scores, ddof=1))))
    save_csv("pca_ablation.csv", ablation)
    save_csv("test_metrics.csv", final_rows)
    save_csv("test_predictions.csv", [dict(sample_id=int(i),
             target=float(yte[j]), **{n: v[j] for n, v in all_preds.items()})
             for j, i in enumerate(test)])
    result = dict(winner=winner, cv=summary, test=final_rows,
        final_parameters=final_params, pca_variance=variance.tolist(),
        pca_ratio=pca.explained_variance_ratio_.tolist(),
        pca95_k=int(np.searchsorted(variance, 0.95) + 1),
        ablation=ablation, rotation_max_error=rotation_error,
        example=dict(sample_id=int(test[0]), x=xte[0].tolist(),
                     target=float(yte[0]), prediction=all_preds[winner][0]),
        data=dict(n=442, p=10, n_train=353, n_test=89, missing=0,
                  duplicate_X=int(len(x) - len(np.unique(x, axis=0))),
                  target_range=[float(y.min()), float(y.max())],
                  target_mean_train=float(ytr.mean()),
                  feature_names=data.feature_names,
                  sha256=hashlib.sha256(x.tobytes()+y.tobytes()).hexdigest()),
        versions=dict(python=platform.python_version(),
                      numpy=np.__version__, scipy=scipy.__version__,
                      sklearn=sklearn.__version__))
    (OUT / "results.json").write_text(json.dumps(result, indent=2),
                                      encoding="utf-8")
    (OUT / "dataset_description.txt").write_text(data.DESCR, encoding="utf-8")
    # Kiem tra metric doc lap bang NumPy cho mo hinh da chon.
    e = np.asarray(all_preds[winner]) - yte
    manual = dict(MAE=float(np.mean(abs(e))), RMSE=float(np.sqrt(np.mean(e**2))),
                  R2=float(1 - sum(e**2) / sum((yte-yte.mean())**2)))
    observed = next(r for r in final_rows if r["model"] == winner)
    assert all(abs(manual[m] - observed[m]) < 1e-10 for m in manual)
    print("Selected before Test:", winner)
    print("Test:", observed)
    print("PCA 95% components:", result["pca95_k"])
    print("All checks passed. Results:", OUT)


if __name__ == "__main__":
    main()
