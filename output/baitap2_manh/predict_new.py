"""Du bao mau moi: python predict_new.py age sex bmi bp s1 s2 s3 s4 s5 s6."""
import csv
import json
import sys
from pathlib import Path
import numpy as np
from regression_pca import candidates

out = Path(__file__).resolve().parent / "ket_qua"
result = json.loads((out / "results.json").read_text(encoding="utf-8"))
features = result["data"]["feature_names"]
with (out / "train.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
x = np.array([[float(r[c]) for c in features] for r in rows])
y = np.array([float(r["target"]) for r in rows])
values = [float(v) for v in sys.argv[1:]] if len(sys.argv) > 1 else [
    42, 1, 30.6, 121, 176, 92.8, 69, 3, 4.2627, 89]
if len(values) != 10 or not np.isfinite(values).all():
    raise ValueError("Can 10 gia tri huu han theo thu tu: " + ", ".join(features))
name = result["winner"]
model = candidates()[name][0]
model.set_params(**result["final_parameters"][name])
model.fit(x, y)
print("Model:", name)
print("Predicted target:", float(model.predict([values])[0]))
