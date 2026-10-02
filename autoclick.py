import time
import threading
from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()

running = False
exit_program = False

CLICK_INTERVAL = 0.5  # thời gian giữa mỗi lần click


def auto_click():
    global running, exit_program

    while not exit_program:
        if running:
            mouse.click(Button.left)
            time.sleep(CLICK_INTERVAL)
        else:
            time.sleep(0.1)


def on_press(key):
    global running, exit_program

    if key == keyboard.Key.f8:
        running = not running
        print("Auto left click:", "BẬT" if running else "TẮT")

    elif key == keyboard.Key.esc:
        exit_program = True
        print("Thoát chương trình")
        return False


click_thread = threading.Thread(target=auto_click)
click_thread.start()

print("Nhấn F8 để bật/tắt auto left click")
print("Nhấn ESC để thoát")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()