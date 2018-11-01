"""
責務：ゲーム設定ファイルのロードを行う
設定ファイルに記述すること
ゲームパス
ゲーム起動コマンド
ウィンドウサイズ
ゲームプレイを始めるために必要なコマンド
    マップ変更コマンド
    ゲームモード変更コマンド
ゲームプレイに必要な操作
　　キー操作
　　　移動
　　　射撃
　　　リロード
　　マウス操作
　　　ｘ，ｙ
"""
import json
from collections import OrderedDict

class GameInfo():
    PATH = None
    EXEC_CMD = None
    SCREEN_SIZE = None
    SCREEN_OFSET = None
    GAME_SETTING_CMD = None
    GAME_PLAYING_OPS = None
    GAME_MODES = None
    GAME_MAPS = None
    BOT_STR = None
    TEAMS = None

    def __init__(self):
        self.loadConfigJson()
        pass
    def loadConfigJson(self):
        with open("config/game_info.json") as f:
            df = json.load(f)
            GameInfo.PATH = df["path"]
            GameInfo.EXEC_CMD = df["execCmd"]
            GameInfo.SCREEN_SIZE = df["screenSize"]
            GameInfo.SCREEN_OFSET = df["screenOfset"]
            GameInfo.GAME_SETTING_CMD = df["gameSettingCmds"]
            GameInfo.GAME_PLAYING_OPS = df["gamePlayingOps"]
            GameInfo.GAME_MODES = df["modes"]
            GameInfo.GAME_MAPS = df["maps"]
            GameInfo.TEAMS = df["teams"]
            GameInfo.BOT_STR = df["botStr"]