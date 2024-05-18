from typing import List
from src.Enumerators import Mode, Difficulty
import pygame


class GameManager:
    _instance = None
    _storageManager: StorageManager

    CHAR_LIST: List[str]

    _player_input: List[str]
    _target_text: List[str]
    _target_list: List[str]

    _current_mode: Mode

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._player_input = []
        self.CHAR_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z', 'ą', 'ę', 'ó', 'ź', 'ż', ',', '.', '?', ':', ';', '1', '2',
                          '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
                          '_', '+', '=', '`', '~']

    def handle_input(self, event: pygame.event.Event):

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

    def get_input(self):
        return self._player_input

    def get_input_text(self):
        return "".join(self._player_input)

    def clear_input(self):
        self._player_input.clear()

    def check_target_completed(self) -> int:
        raise NotImplementedError

    def load_target_list(self, diff: Difficulty):
        raise NotImplementedError

    def next_target_sentence(self, random: bool) -> bool:
        raise NotImplementedError

    def next_target_word(self, random: bool) -> bool:
        raise NotImplementedError

    def get_target_text(self) -> str:
        raise NotImplementedError

    def get_random_sentence(self) -> str:
        raise NotImplementedError

    def get_random_word(self) -> str:
        raise NotImplementedError

    def set_mode(self, mode: Mode):
        raise NotImplementedError

