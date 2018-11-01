"""
責務：ゲーム操作のコマンドを作成する
１．ゲームモード設定のコマンドを作成する
２．ゲームプレイの操作コマンドを作成する（マルチプロセス）
"""

class Agent():
    def __init__(self, game_info):
        self.game_info = game_info
        pass
    def gen_game_setting_cmd(self, *, mode = "OSK_TDM", map = "TRAINING_MAP"):
        try:
            mode_cmd = self.game_info.GAME_SETTING_CMD["selectMode"]
            mode_id = self.game_info.GAME_MODES[mode]
            map_cmd = self.game_info.GAME_SETTING_CMD["selectMap"]
            map_id = self.game_info.GAME_MAPS[map]
            return "/" + mode_cmd + " " + mode_id + "; " + map_cmd + " " + map_id + "\n"
        except KeyError:
            print("KeyError")

    def gen_team_select_cmd(self, *, team = "CLA"):
        try:
            #select_cmd = self.game_info.GAME_SETTING_CMD.TEAM
            select_cmd = self.game_info.GAME_SETTING_CMD["selectTeam"]
            team_id = self.game_info.TEAMS[team]
            return "/" + select_cmd + " " + team_id + "\n"
        except KeyError:
            print("KeyError")
        

    def gen_add_bot_cmd(self, *, team="RVSF", strength="BAD", name = "BOT"):
        try:
            add_bot_cmd = self.game_info.GAME_SETTING_CMD["addBot"]
            team_id = self.game_info.TEAMS[team]
            str_id = self.game_info.BOT_STR[strength]
            return "/" + add_bot_cmd + " " + team_id + " " + str_id + " " + name + "\n"
        except KeyError:
            print("KeyError")
