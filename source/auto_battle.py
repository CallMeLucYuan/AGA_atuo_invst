import pyautogui
import time
import pygetwindow as gw

loop_count     = 0
loop_count_sp  = 1
loop_count_ass = 0



def fight_once():
    global loop_count    
    global loop_count_sp 
    global loop_count_ass
    try:     
        pyautogui.press('s')
        time.sleep(0.5)
        with pyautogui.hold('right'):  
            with pyautogui.hold('up'):  
                for i in range(1,50) :
                    pyautogui.press('x')
                    time.sleep(0.1)
        time.sleep(0.5)
        pyautogui.press('d')
        if(loop_count_sp == 1):
            pyautogui.press('space') 
            time.sleep(0.5)
            loop_count_sp = 0
        if(loop_count_ass == 1):
            pyautogui.press('r')
            time.sleep(0.5)
            loop_count_sp = 0 
        loop_count_sp   += 1
        loop_count_ass  += 1  
    except:       
        
        raise custom_error('Mouse get corner')
        
class custom_error(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.err_info = error_info
    def __str__(self) -> str:
        return super().err_info 
