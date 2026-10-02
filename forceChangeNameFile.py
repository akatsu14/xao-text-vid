import os
import re
import tkinter as tk
from tkinter import filedialog
import time
# =========================
# CHỌN FOLDER
# =========================
root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory(
    title="Chọn folder cần đổi tên file"
)

if not folder_path:
    print("Không có folder nào được chọn.")
    exit()

# =========================
# LẤY YYYYMMDD TỪ TÊN FOLDER
# =========================
folder_name = os.path.basename(folder_path)

match = re.match(r"(\d{8})", folder_name)

if not match:
    # Nếu không tìm thấy YYYYMMDD ở đầu tên folder, thì là coi như là hôm nay theo ngày hiện tại
    match = re.match(r"(\d{8})", time.strftime("%Y%m%d"))

date_prefix = match.group(1)

print(f"Folder: {folder_name}")
print(f"Ngày lấy được: {date_prefix}")
print("-" * 70)

# =========================
# LẤY DANH SÁCH FILE
# =========================
files = [
    f for f in os.listdir(folder_path)
    if os.path.isfile(os.path.join(folder_path, f))
]

# Sắp xếp theo tên để index ổn định
files.sort(key=str.lower)

remove_text = "[English (auto-generated)]"

# =========================
# ĐỔI TÊN
# =========================
for index, filename in enumerate(files, start=1):

    old_path = os.path.join(folder_path, filename)

    # Xóa "[English (auto-generated)]"
    clean_name = filename.replace(remove_text, "").strip()

    # Tên mới:
    # 20260814 1 + tên cũ
    new_name = f"{date_prefix} {index} {clean_name}"

    new_path = os.path.join(folder_path, new_name)

    # Nếu tên không thay đổi thì bỏ qua
    if old_path == new_path:
        continue

    # Tránh ghi đè file có sẵn
    if os.path.exists(new_path):
        print(f"[SKIP] File đã tồn tại: {new_name}")
        continue

    os.rename(old_path, new_path)

    print(f"[OK] {filename}")
    print(f"  -> {new_name}")

print("\nHoàn thành đổi tên!")