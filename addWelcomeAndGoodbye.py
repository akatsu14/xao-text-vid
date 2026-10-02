import os


# Câu chào đầu và kết thúc
# royal document story
header = "Welcome back to our channel, where we provide updates and undisclosed narratives on Catherine, Princess of Wales, and her royal family. We are excited to share the following news with you:\n"
footer = "\nThank you for watching the video! Please let us know your thoughts, and goodbye for now!\n"

# royal list
# header = "Welcome back to our channel, where we share updates and untold stories about Catherine, Princess of Wales, and her royal family. Today, we bring you some news:\n"
# footer = "\nThank you for watching the video! Please let us know your thoughts, and goodbye for now!\n"

# Noble Royal News
# header = "Welcome back to our channel, where we provide updates and exclusive insights on Catherine, Princess of Wales, and her royal family. We are pleased to announce the following news:\n"
# footer = "\nThanks for viewing the video! What do you think about this? Let us know your thoughts and see you in a future video!\n"

# Đường dẫn tới thư mục chứa các file txt
folder = r"quilbot\20260630 royal document story"

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Thêm header nếu chưa có
        if not lines or header.strip() not in lines[0]:
            lines.insert(0, header)
        # Thêm footer nếu chưa có
        if not lines[-1].strip() == footer.strip():
            if not lines[-1].endswith('\n'):
                lines[-1] += '\n'
            lines.append(footer)
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)