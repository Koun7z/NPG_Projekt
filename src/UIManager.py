from typing import Type

import pygame

import Layout


class UIManager:
    _instance = None
    _layouts: map[str, Layout]
    _window: pygame.display
    _current_layout: str
    _width_window: int
    _height_window: int
    _font: map[str, pygame.font.Font]

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError

    def _init(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def change_layout(self, layout_name: str) -> bool:
        raise NotImplementedError

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
        raise NotImplementedError
