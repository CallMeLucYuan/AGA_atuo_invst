from pynput import keyboard
import threading
import pyautogui
import time

flag = False
loop_count     = 0
loop_count_sp  = 0
loop_count_ass = 0

def print_loop():
    global  loop_count    
    global  loop_count_sp 
    global  loop_count_ass

    while(flag):
        pyautogui.press('x')      
        if (loop_count == 50):
            pyautogui.press('s')
            pyautogui.press('d')    
            pyautogui.keyUp('left')
            loop_count = 0
        else:
            pyautogui.keyDown('left')
        if (loop_count_sp == 300):
            pyautogui.press('space')    
            loop_count_sp = 0 
        if (loop_count_ass == 300):
            pyautogui.press('t')    
            loop_count = 0
        loop_count      += 1  
        loop_count_sp   += 1
        loop_count_ass  += 1         
        time.sleep(0.1)

def on_press(key):
    global flag
    if hasattr(key, 'vk') and 96 == key.vk:
        flag = True
        print("start")
        t = threading.Thread(target=print_loop)
        t.start()
    elif hasattr(key, 'vk') and 97 == key.vk:
        print("stop")
        flag = False


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
