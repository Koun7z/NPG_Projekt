from typing import List

import pygame


class GameManager:
    _instance = None
    CHAR_LIST: List[str]

    _player_input: List[str]

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

    def clear_input(self):
        self._player_input.clear()
