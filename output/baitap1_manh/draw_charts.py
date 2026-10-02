"""Ve ba bieu do tu results.json; can Pillow: python -m pip install Pillow."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE / "ket_qua/results.json").read_text())
OUT = BASE / "ket_qua"
BLUE, ORANGE = "#24577A", "#C66A21"


def font(size):
    for name in ["C:/Windows/Fonts/arial.ttf", "DejaVuSans.ttf"]:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def chart(ylabel):
    im = Image.new("RGB", (1500, 760), "white")
    d = ImageDraw.Draw(im)
    for value in range(0, 101, 20):
        y = 620 - value * 5
        d.line((130, y, 1430, y), fill="#DFE4E8", width=2)
        d.text((105, y), str(value), font=font(26), fill="black", anchor="rm")
    d.line((130, 120, 130, 620, 1430, 620), fill="black", width=3)
    d.text((130, 38), ylabel, font=font(30), fill="black")
    return im, d


im, d = chart("Likelihood (%)")
for i in range(5):
    center = 260 + i * 260
    for j, color in enumerate([BLUE, ORANGE]):
        h = DATA["likelihood"][j][i] * 500
        left = center - 80 + j * 82
        d.rectangle((left, 620 - h, left + 70, 620), fill=color)
    d.text((center, 655), str(i) if i < 4 else ">=4",
           font=font(28), fill="black", anchor="mm")
d.text((780, 715), "Số chỉ báo bất thường (x_bin)",
       font=font(30), fill="black", anchor="mm")
d.text((880, 40), "Normal", font=font(30), fill=BLUE)
d.text((1130, 40), "Failure", font=font(30), fill=ORANGE)
im.save(OUT / "likelihood.png")

im, d = chart("Precision và Recall (%)")
rows = DATA["cost_sweep"]
for key, color in [("precision", BLUE), ("recall", ORANGE)]:
    pts = [(200 + i * 195, 620 - r[key] * 500)
           for i, r in enumerate(rows)]
    for x, y in pts:
        d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=color)
    for (x, y), (xx, yy) in zip(pts, pts[1:]):
        d.line((x, y, xx, yy), fill=color, width=3)
for i, row in enumerate(rows):
    d.text((200 + i * 195, 655), str(row["ratio"]),
           font=font(28), fill="black", anchor="mm")
d.text((780, 715), "C_FN / C_FP (các kịch bản rời rạc)",
       font=font(30), fill="black", anchor="mm")
d.text((880, 40), "Precision", font=font(30), fill=BLUE)
d.text((1140, 40), "Recall", font=font(30), fill=ORANGE)
im.save(OUT / "cost.png")

im, d = chart("Posterior tại x_bin = 2 (%)")
ln, lf = DATA["likelihood"]
pts = []
for i in range(501):
    p = i / 1000
    q = lf[2] * p / (lf[2] * p + ln[2] * (1 - p))
    pts.append((130 + p * 2600, 620 - q * 500))
d.line(pts, fill=BLUE, width=5)
for value in [0, 10, 20, 30, 40, 50]:
    d.text((130 + value * 26, 655), str(value),
           font=font(28), fill="black", anchor="mm")
cross = 130 + DATA["cross_prior"] * 2600
for x in range(130, 1430, 24):
    d.line((x, 370, x + 12, 370), fill=ORANGE, width=3)
for y in range(120, 620, 24):
    d.line((cross, y, cross, y + 12), fill=ORANGE, width=3)
d.text((cross + 18, 145), "6.2832%", font=font(28), fill=ORANGE)
d.text((780, 715), "Prior Failure (%)", font=font(30), fill="black", anchor="mm")
im.save(OUT / "prior.png")
print("Da tao likelihood.png, cost.png va prior.png")
