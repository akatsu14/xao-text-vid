"""Bayes cho du lieu mo phong; chay: python bayes_server.py."""
import csv
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "ket_qua"
OUT.mkdir(exist_ok=True)
# Moi hang: x_bin, so Normal, so Failure. Bin 4 nghia la >=4.
TRAIN = [(0, 3900, 20), (1, 600, 35), (2, 70, 50),
         (3, 10, 55), (4, 4, 56)]
TEST = [(0, 980, 5), (1, 140, 8), (2, 20, 12),
        (3, 4, 14), (4, 2, 15)]


def write_csv(name, header, rows):
    with (OUT / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def make_samples(name, counts):
    # Mo rong tan so thiet ke thanh tung mau; khong sinh telemetry tho.
    rows = []
    for x, normal, failure in counts:
        for label, count in [(0, normal), (1, failure)]:
            for _ in range(count):
                rows.append([len(rows) + 1, x, label])
    write_csv(name, ["id", "x_bin", "label"], rows)
    with (OUT / name).open(encoding="utf-8") as f:
        return [(int(r["x_bin"]), int(r["label"]))
                for r in csv.DictReader(f)]


def fit(samples, alpha=1.0):
    counts = [[0] * 5 for _ in range(2)]
    for x, y in samples:
        counts[y][x] += 1
    totals = [sum(row) for row in counts]
    likelihood = [[(v + alpha) / (totals[y] + 5 * alpha)
                   for v in counts[y]] for y in range(2)]
    return totals[1] / sum(totals), likelihood


def posterior(prior, likelihood):
    ln, lf = likelihood
    return [lf[x] * prior / (lf[x] * prior + ln[x] * (1 - prior))
            for x in range(5)]


def evaluate(samples, post, threshold, c_fp=1, c_fn=20):
    tp = fp = fn = tn = 0
    for x, y in samples:
        pred = int(post[x] >= threshold)  # Hoa thi chon canh bao.
        tp += int(pred == 1 and y == 1)
        fp += int(pred == 1 and y == 0)
        fn += int(pred == 0 and y == 1)
        tn += int(pred == 0 and y == 0)
    return dict(threshold=threshold, TP=tp, FP=fp, FN=fn, TN=tn,
                accuracy=(tp + tn) / len(samples),
                precision=tp / (tp + fp) if tp + fp else 0.0,
                recall=tp / (tp + fn) if tp + fn else 0.0,
                cost=c_fp * fp + c_fn * fn)


def main():
    train = make_samples("train.csv", TRAIN)
    test = make_samples("test.csv", TEST)
    prior, likelihood = fit(train)
    post = posterior(prior, likelihood)
    map_result = evaluate(test, post, 0.5)
    risk_result = evaluate(test, post, 1 / 21)
    # Chi phi duoc danh gia lai theo tung kich ban.
    cost_sweep = []
    for ratio in [1, 2, 5, 10, 20, 50, 100]:
        row = dict(ratio=ratio)
        row.update(evaluate(test, post, 1 / (1 + ratio), c_fn=ratio))
        row["MAP_cost"] = evaluate(test, post, 0.5, c_fn=ratio)["cost"]
        cost_sweep.append(row)
    priors = [0.005, 0.01, 0.03, 0.045, 0.1, 0.2, 0.3, 0.5]
    prior_sweep = [dict(prior=p, posterior=posterior(p, likelihood)[2],
                        MAP=int(posterior(p, likelihood)[2] >= 0.5))
                   for p in priors]
    ln, lf = likelihood
    cross_prior = ln[2] / (ln[2] + lf[2])
    # Kiem tra so mau, xac suat va cac ket qua chinh cua bao cao.
    assert len(train) == 4800 and len(test) == 1200
    assert sum(y for _, y in train) == 216
    assert sum(y for _, y in test) == 54
    assert all(abs(sum(row) - 1) < 1e-12 for row in likelihood)
    assert all(0 <= p <= 1 for p in post)
    assert (map_result["TP"], map_result["FP"],
            map_result["FN"], map_result["TN"]) == (29, 6, 25, 1140)
    assert (risk_result["TP"], risk_result["FP"],
            risk_result["FN"], risk_result["TN"]) == (49, 166, 5, 980)
    assert map_result["cost"] == 506 and risk_result["cost"] == 266
    assert abs(posterior(cross_prior, likelihood)[2] - 0.5) < 1e-12
    result = dict(prior=prior, likelihood=likelihood, posterior=post,
                  MAP=map_result, Bayes=risk_result, cost_sweep=cost_sweep,
                  prior_sweep=prior_sweep, cross_prior=cross_prior)
    (OUT / "results.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8")
    write_csv("posterior.csv", ["x_bin", "P_Normal", "P_Failure"],
              [(x, 1 - p, p) for x, p in enumerate(post)])
    for name, rows in [("cost_sweep.csv", cost_sweep),
                       ("prior_sweep.csv", prior_sweep)]:
        write_csv(name, list(rows[0]), [list(row.values()) for row in rows])
    print("Prior:", prior)
    print("Posterior:", [round(p, 6) for p in post])
    print("MAP:", map_result)
    print("Bayes:", risk_result)
    print("Prior dao quyet dinh tai x=2:", cross_prior)
    print("Tat ca kiem tra deu dat. Thu muc ket qua:", OUT)


if __name__ == "__main__":
    main()
