from pathlib import Path
import sys
import runpy
import shutil
import json
import csv
import numpy as np

base=Path('output/baitap2_manh').resolve()
fresh=Path('tmp/pdfs/bt2_fresh').resolve()
fresh.mkdir(exist_ok=True)
for name in ['regression_pca.py','predict_new.py']:
    shutil.copy2(base/name,fresh/name)
runpy.run_path(str(fresh/'regression_pca.py'),run_name='__main__')
a=json.loads((base/'ket_qua/results.json').read_text())
b=json.loads((fresh/'ket_qua/results.json').read_text())
assert a==b
print('Fresh run results exactly match.')
sys.path.insert(0,str(base))
sys.argv=['predict_new.py']
runpy.run_path(str(base/'predict_new.py'),run_name='__main__')
rows=list(csv.DictReader((base/'ket_qua/oof_predictions.csv').open()))
cv=list(csv.DictReader((base/'ket_qua/cv_folds.csv').open()))
folds={int(r['sample_id']):int(r['fold']) for r in csv.DictReader(
    (base/'ket_qua/outer_folds.csv').open())}
for model in [r['model'] for r in a['cv']]:
    rr=[r for r in rows if r['model']==model]
    assert len(rr)==353 and len({r['sample_id'] for r in rr})==353
    for f in range(1,6):
        group=[r for r in rr if folds[int(r['sample_id'])]==f]
        yy=np.array([float(r['target']) for r in group])
        pp=np.array([float(r['prediction']) for r in group])
        rmse=float(np.sqrt(np.mean((yy-pp)**2)))
        expect=float(next(r['RMSE'] for r in cv
                          if r['model']==model and int(r['fold'])==f))
        assert abs(rmse-expect)<1e-10
print('All 30 outer-fold RMSE scores verified from exported predictions.')
