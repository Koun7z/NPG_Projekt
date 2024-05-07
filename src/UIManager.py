from typing import Type

import pygame

from src.Layout import Layout


class UIManager:
    _instance = None
    _layouts: dict[str, Layout]
    _window: pygame.Surface
    _clock: pygame.time.Clock
    _current_layout: str
    _width_window: int
    _height_window: int
    _font: dict[str, pygame.font.Font]
    _running: bool

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._width_window = 1600
        self._height_window = 900

        pygame.init()
        self._window = pygame.display.set_mode((self._width_window, self._height_window))
        self._clock = pygame.time.Clock()
        self._running = True

        self._font = {}
        self._layouts = {}

    def render(self):
        raise NotImplementedError

    def change_layout(self, layout_name: str) -> bool:
        """
        Changes active layout
        \n Returns true if successful
        """
        if layout_name in self._layouts:
            self._current_layout = layout_name
            return True

        return False

    def get_current_layout_name(self) -> str:
        raise NotImplementedError

    def get_current_layout(self) -> Layout:
        raise NotImplementedError

    def get_width_window(self) -> int:
        raise NotImplementedError

    def get_height_window(self) -> int:
        raise NotImplementedError

    def get_window(self) -> pygame.display:
        raise NotImplementedError

    def get_font(self) -> pygame.font.Font:
        raise NotImplementedError

    def add_font(self, font_name: str, font: pygame.font.Font) -> bool:
        raise NotImplementedError

    def close(self):
        self._running = False
