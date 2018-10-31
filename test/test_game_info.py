import pytest
from module.game_info import GameInfo

def test_GameConfig_leadJson_01():
    assert GameInfo.PATH == None
    assert GameInfo.EXEC_CMD == None
    GameInfo().leadConfigJson()
    assert GameInfo.PATH != None
    assert GameInfo.EXEC_CMD != None