import random
from typing import List
from src.Enumerators import Mode, Difficulty
import pygame

from src.ScoreManager import ScoreManager
from src.StorageManager import StorageManager


class GameManager:
    _instance = None
    _storage_manager: StorageManager
    CHAR_LIST: List[str]

    _player_input: List[str]
    _target_text: List[str]

    _current_mode: Mode
    _current_difficulty: Difficulty

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._player_input = []
        self._current_mode = Mode.Classic
        self._target_text = ["Ala ma kota", "Lorem ipsum", "Asdf"]
        self._current_difficulty = Difficulty.Hard
        self._current_mode = Mode.Classic

        self._storage_manager = StorageManager()

        self.CHAR_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z', 'ą', 'ę', 'ć', 'ó', 'ź', 'ż', ',', '.', '?', ':', ';', '1',
                          '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '-', '_', '+', '=', '`', '~']  # Could be in a file actually

        self.load_target_list(50, True)

    def handle_input(self, event: pygame.event.Event) -> None:

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_BACKSPACE:
            if len(self._player_input) > 0:
                self._player_input.pop()
            return

        if event.key == pygame.K_ESCAPE:
            self.clear_input()
            return

        if event.key == pygame.K_SPACE:
            self._player_input.append(" ")
            return

        for char in event.unicode:
            if char.lower() in self.CHAR_LIST:
                self._player_input.append(char)

    def get_input(self) -> List[str]:
        return self._player_input

    def get_input_text(self) -> str:
        return "".join(self._player_input)

    def clear_input(self) -> None:
        self._player_input.clear()

    def handle_target_completed(self) -> int:
        """
        Checks if the target text is typed correctly, and provides another target word if it is.
        :return: Number of correctly typed characters.
        """

        input_text = self.get_input_text()
        target_text = self.get_target_text()

        ctr = 0
        for char in input_text:
            if char != target_text[ctr]:
                break
            ctr += 1

        if ctr == len(target_text):
            match self._current_mode:
                case Mode.Classic:
                    if self.next_target_sentence():
                        self.win_classic_mode()
                    self._player_input.clear()

                    ScoreManager().update_score(len(target_text))

                case Mode.Menu:
                    raise NotImplementedError

                case Mode.Training:
                    raise NotImplementedError

                case Mode.FallingLetters:
                    raise NotImplementedError

                case _:
                    raise KeyError

        return ctr

    def get_next_target_sentence(self) -> str:
        if len(self._target_text) > 1:
            return self._target_text[1]
        return ""

    def next_target_sentence(self) -> bool:
        """
        Sets target to a new sentenced
        :return If true that list of sentence is empty and game end
        """
        if len(self._target_text) <= 1:
            self._target_text = []
            return True
        self._target_text = self._target_text[1:]
        return False

    def load_target_list(self, count: int, shuffle: bool = False) -> None:
        buff = self._storage_manager.get_quotes(self._current_difficulty, self._current_mode)[:]

        if shuffle:
            random.shuffle(buff)

        self._target_text = buff[:count]

    def next_target_word(self) -> bool:
        raise NotImplementedError

    def get_target_text(self) -> str:
        """
        :return: Current target text
        """
        match self._current_mode:
            case Mode.Classic:
                return self._target_text[0]
            case _:
                raise NotImplementedError

    def get_random_sentence(self, rm: bool) -> str:
        """
        Returns a random sentence from loaded file.
        :param rm: Whether to remove the sentence from the pool.
        :return: A random sentence.
        """
        raise NotImplementedError

    def get_random_word(self) -> str:
        raise NotImplementedError

    def set_mode(self, mode: Mode) -> None:
        """
        Sets the mode of the game
        :param mode: Game Mode
        """
        raise NotImplementedError

    def set_difficulty(self, diff: Difficulty) -> None:
        """
        Sets current difficulty.
        :param diff: Difficulty
        """
        raise NotImplementedError

    def win_classic_mode(self) -> None:
        raise NotImplementedError
