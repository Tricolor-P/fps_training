import cv2
import numpy as np
import pyautogui

class GameScreen:
    def __init__(self, width, height, ofset_x, ofset_y):
        self.width = width
        self.height = height
        self.ofset_x = ofset_x
        self.ofset_y = ofset_y

        self.main_screen = None
    
    def captured(self):
        screenshot = pyautogui.screenshot(region=(  self.width, self.height, 
                                                    self.ofset_x, self.ofset_y))
        gray = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_RGB2GRAY)
        self.main_screen = gray[0:int(self.height*0.91), 0:self.width]
    
    def save(self, name):
        cv2.imwrite( name, self.main_screen)