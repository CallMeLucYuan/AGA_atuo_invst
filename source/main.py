from pynput import keyboard
import threading
import time
import auto_battle
import pic_compare
import pyautogui
import winsound
flag = False
t = None
THRESHOLD = 0.8
screen_cnst = 1
next_button = "./pics/next.png"
strt_inv    = "./pics/strt_inv.png"
sortie      = "./pics/sortie.png"
ok_brtton   = "./pics/ok.png"
end_screen  = "./pics/end_screen.png"
end_mask  = "./pics/end_mask.png"
def fight_loop():
    global  flag
    while(flag):
        try:
            auto_battle.fight_once()
        except:
            flag =False


def on_press(key):
    global flag,t
    if hasattr(key, 'vk') and 96 == key.vk:
        sm.update_state('selc_point') 
    if hasattr(key, 'vk') and 97 == key.vk:
        sm.update_state('idle')
def on_release(key):
    pass


class StateMachine:
    def __init__(self, start_state):
        self.current_state = start_state

    def update_state(self, new_state):
        self.current_state = new_state

    def run(self):
        while True:
            if self.current_state == 'selc_point':
                avg = pic_compare.get_xy(strt_inv , 0.95)
                if (avg[1] > 0 and avg[1] > 0):                 
                    winsound.Beep(262,1000)
                    pyautogui.click(int(1500*screen_cnst), int(1225*screen_cnst), button='left')
                    time.sleep(5)
                    pyautogui.click(int(1280*screen_cnst), int(620*screen_cnst), button='left')
                    time.sleep(0.5)
                    pyautogui.click(int(1280*screen_cnst), int(620*screen_cnst), button='left')
                    time.sleep(3)
                    pyautogui.click(int(1280*screen_cnst), int(1225*screen_cnst), button='left')
                    time.sleep(5)
                    print('ready for battle')
                    self.update_state('battle')
            elif self.current_state == 'battle':
                avg = pic_compare.get_xy_masked(end_screen, end_mask , 0.8)
                if avg[1] < 0 and avg[1] < 0:
                    auto_battle.fight_once()
                else:
                    pyautogui.click(int(1280*screen_cnst), int(1350*screen_cnst), button='left')
                    time.sleep(3)
                    pyautogui.click(int(1280*screen_cnst), int(1350*screen_cnst), button='left')
                    print('waiting for selecting point')
                    self.update_state('selc_point')    
            elif self.current_state == 'idle':
                time.sleep(1)
            else:
                raise ValueError(f'Invalid state: {self.current_state}')


screenWidth, screenHeight = pyautogui.size()
screen_cnst =  screenWidth / 2560  
listener = keyboard.Listener( on_press=on_press,  on_release=on_release)
listener.start()      
sm = StateMachine('idle')
sm.run()


# if hasattr(key, 'vk') and 96 == key.vk:
# flag = True
# print("start")
# t = threading.Thread(target=fight_loop)
# t.start()