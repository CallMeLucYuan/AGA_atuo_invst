import pyautogui
import keyboard
import time
import pygetwindow as gw

def fight(flag):
    loop_count     = 0
    loop_count_sp  = 0
    loop_count_ass = 0
    if(flag):
        pyautogui.press('x')      
        if (loop_count == 50):
            pyautogui.press('s')
            pyautogui.press('d')    
            pyautogui.keyUp('left')
            loop_count = 0
        else:
            pyautogui.keyDown('left')
            loop_count += 1
        if (loop_count_sp == 300):
            pyautogui.press('space')    
            loop_count_sp += 1
        else:
            loop_count_sp = 0 
        if (loop_count_ass == 300):
            pyautogui.press('t')    
            loop_count = 0
        else:
            loop_count_ass += 1                     
        time.sleep(0.1)
        
   