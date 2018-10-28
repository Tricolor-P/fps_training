import pytest
from module.gamedriver import GameDriver

def test_startGame_01():
    gamedriver = GameDriver()
    assert gamedriver.isRunningGame == False
    gamedriver.startGame()
    assert gamedriver.isRunningGame == True
    gamedriver.stopGame()

def test_setGameMode_01():
    gamedriver = GameDriver()
    gamedriver.startGame()
    assert gamedriver.setGameMode() == 1
    assert gamedriver.setGameMode(mode="TDM") == 2
    assert gamedriver.setGameMode(mode="FFA") == 3
    assert gamedriver.setGameMode(mode="OSK_TDM") == 4
    assert gamedriver.setGameMode(mode="OSK_FFA") == 5
    gamedriver.stopGame()

def test_setGameMode_Except_01(capsys):
    #not exist gamemode
    gamedriver = GameDriver()
    gamedriver.startGame()
    res = gamedriver.setGameMode(mode="aaaa")
    captured = capsys.readouterr()
    assert res == False
    assert captured.out == "GAME_MODE does not exist\n"
    gamedriver.stopGame()

def test_setGameMode_Except_02(capsys):
    #gamemode changs when not running
    gamedriver = GameDriver()
    res = gamedriver.setGameMode()
    captured = capsys.readouterr()
    assert res == False
    assert captured.out == "Game is not running\n"
