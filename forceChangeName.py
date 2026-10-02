import os
import re
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

folder = filedialog.askdirectory(title="Chọn folder cần đổi tên file")

if not folder:
    print("Chưa chọn folder.")
    exit()

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if not os.path.isfile(old_path):
        continue

    new_name = filename

    # Xóa tiền tố dạng: YYYYMMDD + số thứ tự
    # Ví dụ: 20260904 1, 20260904 2, 20260904 15
    new_name = re.sub(r'^\d{8}\s+\d+\s*', '', new_name)

    # Xóa [English (auto-generated)]
    new_name = new_name.replace('[English (auto-generated)]', '')

    # Xóa khoảng trắng thừa
    new_name = re.sub(r'\s+', ' ', new_name).strip()

    new_path = os.path.join(folder, new_name)

    if new_name != filename:
        # Tránh ghi đè nếu tên mới đã tồn tại
        if os.path.exists(new_path):
            print(f"[BỎ QUA] File đã tồn tại: {new_name}")
            continue

        os.rename(old_path, new_path)
        print(f"{filename}")
        print(f"→ {new_name}\n")

print("Hoàn tất!")