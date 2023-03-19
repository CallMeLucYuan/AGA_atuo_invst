import cv2
import pyautogui



def get_xy(img_model_path,THRESHOLD):
    pyautogui.screenshot().save("./pics/screenshot.png")
    img = cv2.UMat(cv2.imread("./pics/screenshot.png"))
    img_terminal = cv2.imread(img_model_path)
    height, width, channel = img_terminal.shape
    img_terminal_Umat= cv2.UMat(img_terminal)
    result = cv2.matchTemplate(img, img_terminal_Umat, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val < THRESHOLD:
        avg =(-1,-1)
        print(max_val)
        print("fail")
    else:    
        print(max_val)
        upper_left = cv2.minMaxLoc(result)[2]
        lower_right = (upper_left[0] + width, upper_left[1] + height)
        avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        print("success")
    return avg