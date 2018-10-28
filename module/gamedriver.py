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
    GAME_PATH = "./../AssaultCube/assaultcube.sh"
    GAME_STARTUP_CMD = "exec stdbuf -oL -eL"
    def __init__(self, *, config=None):
        self.executor = ParallelExecutor(
            cmd = GameDriver.GAME_STARTUP_CMD + " " + GameDriver.GAME_PATH)
        self.isRunningGame = False

    def startGame(self):
        print("Sterting Game", end="...")
        self.executor.start()
        self.isRunningGame = True
        print("OK")

    def stopGame(self):
        print("Stopping Game", end="...")
        self.executor.stop()
        self.isRunningGame = False
        print("OK")

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
    def getGameStatus(self):
        pass
        