import pyautogui
import time
import pygetwindow as gw

loop_count     = 0
loop_count_sp  = 0
loop_count_ass = 0



def fight_once():
    global loop_count    
    global loop_count_sp 
    global loop_count_ass
    try:
        pyautogui.press('x')      
        if (loop_count == 50):
            pyautogui.press('s')
            time.sleep(2)
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
    except:       
        
        raise custom_error('Mouse get corner')
        
class custom_error(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.err_info = error_info
    def __str__(self) -> str:
        return super().err_info 
