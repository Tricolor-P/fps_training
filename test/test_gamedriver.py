import pytest
from module.gamedriver import GameDriver

def stub_game_info():
    path = "./../AssaultCube/assaultcube.sh"
    exec_cmd = "exec stdbuf -oL -eL"
    screen_size = {"width":640, "height":400}
    screen_ofset = {"x":0, "y":52}
    return path, exec_cmd, screen_size, screen_ofset


def test_startGame_01():
    path, exec_cmd, screen_size, screen_ofset = stub_game_info()
    gamedriver = GameDriver(path, exec_cmd, screen_size, screen_ofset)
    assert gamedriver.isRunningGame == False
    gamedriver.startGame()
    assert gamedriver.isRunningGame == True
    gamedriver.stopGame()
    assert gamedriver.isRunningGame == False

#標準入力を待つため、テスト不可、ゲームを起動するときにWindow位置の指定できればテストできるようになる
"""
def test_activateWindow_01():
    path, exec_cmd = stub_game_info()
    gamedriver = GameDriver(path, exec_cmd)
    gamedriver.activateWindow()
"""

#ファイル書き出しできないため、テスト不可
"""
def test_get_game_status_01():
    path, exec_cmd, screen_size, screen_ofset = stub_game_info()
    gamedriver = GameDriver(path, exec_cmd, screen_size, screen_ofset)
    assert gamedriver.get_game_status() == "aa"
"""
def test_setGameMode_01():
    path, exec_cmd, screen_size, screen_ofset = stub_game_info()
    gamedriver = GameDriver(path, exec_cmd, screen_size, screen_ofset)
    gamedriver.startGame()
    assert gamedriver.setGameMode() == 1
    assert gamedriver.setGameMode(mode="TDM") == 2
    assert gamedriver.setGameMode(mode="FFA") == 3
    assert gamedriver.setGameMode(mode="OSK_TDM") == 4
    assert gamedriver.setGameMode(mode="OSK_FFA") == 5
    gamedriver.stopGame()

def test_setGameMode_Except_01(capsys):
    #not exist gamemode
    path, exec_cmd, screen_size, screen_ofset = stub_game_info()
    gamedriver = GameDriver(path, exec_cmd, screen_size, screen_ofset)
    gamedriver.startGame()
    res = gamedriver.setGameMode(mode="aaaa")
    captured = capsys.readouterr()
    assert res == False
    assert captured.out == "Starting Game...OK\nGAME_MODE does not exist\n"
    gamedriver.stopGame()

def test_setGameMode_Except_02(capsys):
    #gamemode changs when not running
    path, exec_cmd, screen_size, screen_ofset = stub_game_info()
    gamedriver = GameDriver(path, exec_cmd, screen_size, screen_ofset)
    res = gamedriver.setGameMode()
    captured = capsys.readouterr()
    assert res == False
    assert captured.out == "Game is not running\n"
