import time
import pyautogui
from module.gamedriver import GameDriver

if __name__ == "__main__":

    #ゲームの起動
    acDriver = GameDriver(config=None)
    acDriver.startGame()
    print("-- Please Move The Window to The Upper-Left Corner --")
    print("-- and Press Any Key --")
    input()
    acDriver.setGameMode(mode="OSK_TDM")
    
    #変更必要、ドライバー以下に追加
    print("AssaultCube:Window activating", end="...")
    screen_width = 640
    screen_height = 400
    screen_ofset_width = 0
    screen_ofset_height = 52
    pyautogui.moveTo(screen_width/2+screen_ofset_width,
                 screen_height/2+screen_ofset_height,1)
    pyautogui.click()
    pyautogui.moveRel(1, 0, 1)
    print("Done.")
    
    print("AssaultCube:GameMode initializing", end="...")
    pyautogui.typewrite("/mode 21; map small_train_map\n",0.02)
    pyautogui.typewrite("/team CLA\n",0.02)
    pyautogui.typewrite("/addbot RVSF bad bot1\n",0.02)
    pyautogui.typewrite("/addbot RVSF bad bot2\n",0.02)
    pyautogui.typewrite("/addbot RVSF bad bot3\n",0.02)
    pyautogui.typewrite("/addbot RVSF bad bot4\n",0.02)

    time.sleep(3)
    acDriver.stopGame()