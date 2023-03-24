import cv2
import pyautogui



def get_xy(img_model_path,THRESHOLD):
    pyautogui.screenshot().save("./pics/screenshot.png")
    img = cv2.imread("./pics/screenshot.png")
    img_terminal = cv2.imread(img_model_path)
    height, width, channel = img_terminal.shape
    terminal_gray = cv2.UMat(cv2.cvtColor(img_terminal , cv2.COLOR_BGR2GRAY))
    image_gray = cv2.UMat(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    result = cv2.matchTemplate(image_gray, terminal_gray, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(1-min_val)
    if 1-min_val < THRESHOLD:
        avg =(-1,-1)
        print("fail")
    else:    
        upper_left = cv2.minMaxLoc(result)[2]
        lower_right = (upper_left[0] + width, upper_left[1] + height)
        avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        print("success")
    return avg


def get_xy_masked(img_model_path,mask_path,THRESHOLD):
    pyautogui.screenshot().save("./pics/screenshot.png")
    img = cv2.imread("./pics/screenshot.png")
    mask = cv2.imread(mask_path,0)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    img_terminal = cv2.imread(img_model_path)
    height, width, channel = img_terminal.shape
    terminal_masked = cv2.bitwise_and(img_terminal, img_terminal, mask=mask)
    terminal_gray = cv2.UMat(cv2.cvtColor(img_terminal , cv2.COLOR_BGR2GRAY))
    image_gray = cv2.UMat(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    result = cv2.matchTemplate(image_gray, terminal_gray, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(1-min_val)
    if 1-min_val < THRESHOLD:
        avg =(-1,-1)
        print("fail")
    else:    
        upper_left = cv2.minMaxLoc(result)[2]
        lower_right = (upper_left[0] + width, upper_left[1] + height)
        avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
        print("success")
    return avg