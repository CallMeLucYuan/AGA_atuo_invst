from pynput import keyboard
import threading
import time
import auto_battle
import pic_compare
import pyautogui
flag = False
t = None
THRESHOLD = 0.8
next_button = "./pics/next.png"
strt_inv    = "./pics/strt_inv.png"
coin        = "./pics/coin_100.png"
sortie      = "./pics/sortie.png"
ok_brtton   = "./pics/ok.png"
pause       = "./pics/pause_button.png"  

def fight_loop():
    global  flag
    while(flag):
        try:
            auto_battle.fight_once()
        except:
            flag =False


def on_press(key):
    global flag,t
    if hasattr(key, 'vk') and 97 == key.vk:
        print("stop")
        flag = False
        if t is not None:
            t.join()
            t = None
def on_release(key):
    pass

def routine(img_model_path, name):
    avg = pic_compare.get_xy(img_model_path,THRESHOLD)
    print(f"clicking{name}")
    auto_Click(avg)

def auto_Click(var_avg):
    if( var_avg[0] > 0 or var_avg[1] > 0):
        pyautogui.click(var_avg[0], var_avg[1], button='left')
    time.sleep(1)


     
listener = keyboard.Listener( on_press=on_press,  on_release=on_release)
listener.start()      

while(True):       
    routine(strt_inv, "strt_inv") 

# if hasattr(key, 'vk') and 96 == key.vk:
# flag = True
# print("start")
# t = threading.Thread(target=fight_loop)
# t.start()