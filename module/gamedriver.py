import time
import pyautogui
from module.parallel_executor import ParallelExecutor
from module.screen_capture import screen_capture

class IsRunningGameException(Exception):
    pass

class GameDriver:
    GAME_MODE = { "DEFAULT":1,
                  "TDM":2, 
                  "FFA":3, 
                  "OSK_TDM":4, 
                  "OSK_FFA":5 }
    def __init__(self, path, exec_cmd, screen_size, screen_ofset):
        self.executor = ParallelExecutor(
            cmd = exec_cmd + " " + path)
        self.isRunningGame = False
        self.screen_size = screen_size
        self.screen_ofset = screen_ofset
        self.windowIsActivated = False

    def startGame(self):
        print("Starting Game", end="...")
        self.executor.start()
        self.isRunningGame = True
        print("OK")

    def stopGame(self):
        print("Stopping Game", end="...")
        self.executor.stop()
        self.isRunningGame = False
        print("OK")

    def activateWindow(self):
        print("GameDriver:activateWindow", end="...")
        print("-- Please Move The Window to The Upper-Left Corner --")
        print("-- and Press Any Key --")
        input()
        self.windowIsActivated = True

        centor_x = self.screen_size["width"] / 2
        centor_y = self.screen_size["height"] / 2
        ofset_x = self.screen_ofset["x"]
        ofset_y = self.screen_ofset["y"]
        pyautogui.moveTo(centor_x+ofset_x, centor_y+ofset_y, 1)
        pyautogui.click()
        pyautogui.moveRel(1, 0, 1)

        print("OK")
    
    def get_game_status(self, *, get_screen = False, get_std_out = True):
        ss = screen_capture(    self.screen_size["width"], self.screen_size["height"],
                                self.screen_ofset["x"], self.screen_ofset["y"])
        return ss

    def send_cmd(self, cmd, interval):
        pyautogui.typewrite(cmd, interval)

    def setGameMode(self,  *, mode="DEFAULT"):
        try:
            if self.isRunningGame:
                GameDriver.GAME_MODE[mode]
                print("Setting GameMode: " + mode, end="...")
            else:
                raise IsRunningGameException
        except KeyError:
            print("GAME_MODE does not exist")
            return False
        except IsRunningGameException:
            print("Game is not running")
            return False
        else:
            print("OK")
            return GameDriver.GAME_MODE[mode]
    def setGameMap(self):
        pass
    
        