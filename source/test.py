
from pynput import keyboard
import threading
import time
import pyautogui


class KeyboardListener:
    def __init__(self):
        self.stop_event = threading.Event()

    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key):
        if key.char == 'a':
            self.stop_event.clear()
            while not self.stop_event.is_set():
                pyautogui.press('b')

    def on_release(self, key):
        if key == keyboard.Key.ctrl_l:
            self.stop_event.set()


# 测试
keyboard_listener = KeyboardListener()
keyboard_listener.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

keyboard_listener.stop_event.set()

