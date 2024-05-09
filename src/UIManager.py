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
        """
        Run main loop of game
        """
        while self._running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()
            self.get_current_layout().render(self._window, events)

    def change_layout(self, layout_name: str) -> bool:
        """
        Changes active layout
        :param layout_name: layout name
        :return: True if successful
        """
        if layout_name in self._layouts:
            self._current_layout = layout_name
            return True

        return False

    def get_current_layout_name(self) -> str:
        return  self._current_layout

    def get_current_layout(self) -> Layout:
        return self._layouts.get(self._current_layout)

    def get_width_window(self) -> int:
        return self._width_window

    def get_height_window(self) -> int:
        return self._height_window

    def get_window(self) -> pygame.Surface:
        return self._window

    def get_font(self, font_name: str) -> pygame.font.Font:
        """
        Returns font for given name
        :param font_name: str - name of font
        :return: font
        """
        if font_name in self._font:
            return self._font[font_name]
        raise KeyError

    def add_font(self, font_name: str, font: pygame.font.Font) -> bool:
        """
        Adds font to font database
        :param font_name: Name of adding font
        :param font: Object of adding font
        :return: True if successful
        """
        if font_name in self._font:
            return False
        self._font[font_name] = font
        return True

    def close(self):
        self._running = False
