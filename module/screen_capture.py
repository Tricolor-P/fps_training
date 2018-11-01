import cv2
import numpy as np
def screen_capture(width,height,ofset_x,ofset_y):
    screenshot = pyautogui.screenshot(region=(  width,
                                                height, 
                                                ofset_x, 
                                                ofset_y))
    gray = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_RGB2GRAY)
    gameImage_main     = gray[0:int(height*0.91), 0:width]
    return gameImage_main