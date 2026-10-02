"""Ve bieu do tu ket_qua; chay sau regression_pca.py."""
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "ket_qua"
R = json.loads((OUT / "results.json").read_text(encoding="utf-8"))
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False})


def save(name):
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=200, facecolor="white")
    plt.close()


fig, ax = plt.subplots(figsize=(7.5, 3.4))
names = [r["model"] for r in R["cv"]]
ax.bar(names, [r["RMSE_mean"] for r in R["cv"]],
       yerr=[r["RMSE_std"] for r in R["cv"]], capsize=4,
       color=["#B9C1C8" if n == "Mean" else "#285D7E" for n in names])
ax.set(ylabel="RMSE CV trung bình ± SD", ylim=(0, 100))
ax.grid(axis="y", alpha=.2)
save("cv_comparison.png")

fig, axs = plt.subplots(1, 2, figsize=(8, 3.4))
k = np.arange(1, 11)
axs[0].plot(k, np.asarray(R["pca_variance"])*100, "o-", color="#285D7E")
axs[0].axhline(95, color="#B65B27", linestyle="--", label="95%")
axs[0].set(xlabel="Số thành phần PCA", ylabel="Phương sai tích lũy (%)",
           xticks=[2,4,6,8,10], ylim=(0,105))
axs[0].legend()
a = R["ablation"]
axs[1].errorbar([r["k"] for r in a], [r["RMSE_mean"] for r in a],
                yerr=[r["RMSE_std"] for r in a], fmt="o-", capsize=4,
                color="#285D7E")
axs[1].set(xlabel="Số thành phần PCA", ylabel="RMSE CV ± SD",
           xticks=[2,4,6,8,10], title="Ridge cố định alpha = 1")
for ax in axs:
    ax.grid(alpha=.2)
save("pca_effect.png")

with (OUT / "test_predictions.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
y = np.array([float(r["target"]) for r in rows])
pred = np.array([float(r[R["winner"]]) for r in rows])
fig, axs = plt.subplots(1, 2, figsize=(8, 3.4))
axs[0].scatter(y, pred, s=22, alpha=.75, color="#285D7E")
lo, hi = min(y.min(),pred.min())-10, max(y.max(),pred.max())+10
axs[0].plot([lo,hi],[lo,hi], "--", color="#B65B27")
axs[0].set(xlabel="Target thật", ylabel="Target dự đoán",
           title=R["winner"] + " trên Test", xlim=(lo,hi), ylim=(lo,hi))
axs[1].scatter(pred, y-pred, s=22, alpha=.75, color="#285D7E")
axs[1].axhline(0, linestyle="--", color="#B65B27")
axs[1].set(xlabel="Target dự đoán", ylabel="Phần dư y − dự đoán",
           title="Phần dư trên 89 mẫu Test")
for ax in axs:
    ax.grid(alpha=.2)
save("test_diagnostics.png")
print("Saved three charts.")
