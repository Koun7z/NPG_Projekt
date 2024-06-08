import pytest
import src.GameManager
from src.Enumerators import Mode, Difficulty


def test_load_by_char_hard():

    game_manager = src.GameManager.GameManager()

    game_manager._current_mode = Mode.Classic           # \
                                                        # |-> Those parameters dictate checked data set
    game_manager._current_difficulty = Difficulty.Hard  # /

    for i in range(10000):
        for j in range(100, 1001, 50):
            game_manager.load_target_list_n_chars(j)
            assert len("".join(game_manager._target_text)) == j


def test_load_by_char_medium():

    game_manager = src.GameManager.GameManager()

    game_manager._current_mode = Mode.Classic             # \
                                                          # |-> Those parameters dictate checked data set
    game_manager._current_difficulty = Difficulty.Medium  # /

    for i in range(10000):
        for j in range(100, 1001, 50):
            game_manager.load_target_list_n_chars(j)
            assert len("".join(game_manager._target_text)) == j

def test_load_by_char_easy():

    game_manager = src.GameManager.GameManager()

    game_manager._current_mode = Mode.Classic             # \
                                                          # |-> Those parameters dictate checked data set
    game_manager._current_difficulty = Difficulty.Easy  # /

    for i in range(10000):
        for j in range(100, 1001, 50):
            game_manager.load_target_list_n_chars(j)
            assert len("".join(game_manager._target_text)) == j