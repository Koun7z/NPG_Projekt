from typing import List

import pygame
import pygame_gui


class Layout:
    _manager: pygame_gui.UIManager
    _colorPalette: dict[str, tuple[int, int, int]]
    _fontPalette: dict[str, pygame.font.Font]

    def render(self, window: pygame.display, events: List[pygame.event.Event]):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def get_color_of(self, component_name: str) -> tuple[int, int, int]:
        """
        Returns the color of the given component name,
        if name is not recognized return <wybież se domyślny kolor, najlepiej taki co się rzuca w oczy>
        :param component_name: name of the component
        :return:  RGB color value
        """
        raise NotImplementedError

    def get_font_of(self, component_name: str) -> pygame.font.Font:
        """
        Returns the of the given component name, if name is not recognized return <wybież se domyślną czcionke>
        :param component_name: name of the component
        :return: Font object
        """
        raise NotImplementedError
