import pytest
from module.game_screen import GameScreen

def test_screen_capture_01():
    game_screen = GameScreen(100,100,100,100)
    game_screen.captured()
    assert game_screen.main_screen.any() != None
    game_screen.save("test/test_screen_capture.png")