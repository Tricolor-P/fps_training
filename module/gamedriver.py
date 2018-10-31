import time
import pyautogui
from module.parallel_executor import ParallelExecutor


class IsRunningGameException(Exception):
    pass

class GameDriver:
    GAME_MODE = { "DEFAULT":1,
                  "TDM":2, 
                  "FFA":3, 
                  "OSK_TDM":4, 
                  "OSK_FFA":5 }
    def __init__(self, path, exec_cmd):
        self.executor = ParallelExecutor(
            cmd = exec_cmd + " " + path)
        self.isRunningGame = False
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
        print("OK")
    
    def getGameStatus(self):
        pass

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
    
        