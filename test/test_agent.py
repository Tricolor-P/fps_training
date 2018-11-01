import pytest
from module.agent import Agent

#単体テストにならんがgame_infoをインポートします
from module.game_info import GameInfo 

def stub_game_info():
    return "game_info"

def test_init_01():
    game_info = GameInfo()
    agent = Agent(game_info)
    assert agent.gen_game_setting_cmd(mode="OSK_TDM", map = "TRAINING_MAP") == "/mode 21; map small_train_map\n"

def test_gen_add_bot_cmd_01():
    game_info = GameInfo()
    agent = Agent(game_info) 
    assert agent.gen_add_bot_cmd(team="RVSF", strength="BAD", name = "bot1") == "/addbot RVSF bad bot1\n"

def test_gen_team_select_cmd_01():
    game_info = GameInfo()
    agent = Agent(game_info)
    assert agent.gen_team_select_cmd(team="CLA") ==  "/team CLA\n"