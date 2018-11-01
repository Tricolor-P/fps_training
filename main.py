import time
import pyautogui
from module.game_info import GameInfo
from module.gamedriver import GameDriver
from module.agent import Agent


if __name__ == "__main__":

    #ゲーム情報、どらいばー、エージェントの作成
    game_info =  GameInfo()
    gamedriver = GameDriver(game_info.PATH, game_info.EXEC_CMD,
                            game_info.SCREEN_SIZE, game_info.SCREEN_OFSET)
    agent = Agent(game_info)
    #コマンドを投げるに変更する↑
    

    #ゲームの起動
    gamedriver.startGame()
    gamedriver.activateWindow()
    time.sleep(1)

    #ゲームモード初期化
    print("AssaultCube:GameMode initializing", end="...")
    gamedriver.send_cmd(agent.gen_game_setting_cmd(mode="OSK_TDM", map="TRAINING_MAP"), 0.02)
    gamedriver.send_cmd(agent.gen_team_select_cmd(team="CLA"), 0.02)
    gamedriver.send_cmd(agent.gen_add_bot_cmd(name="bot1"), 0.02)
    gamedriver.send_cmd(agent.gen_add_bot_cmd(name="bot1"), 0.02)
    gamedriver.send_cmd(agent.gen_add_bot_cmd(name="bot1"), 0.02)
    gamedriver.send_cmd(agent.gen_add_bot_cmd(name="bot1"), 0.02)
    print("OK")

    gamedriver.stopGame()