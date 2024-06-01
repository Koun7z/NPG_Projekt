from typing import List

import pygame
import pygame_gui


class Layout:
    _manager: pygame_gui.UIManager
    _colorPalette: dict[str, tuple[int, int, int]]
    _fontPalette: dict[str, pygame.font.Font]

    def __init__(self):
        from src.UIManager import UIManager

        self._colorPalette = {
            "ui_text": (69, 70, 76),  # primary text dolor
            "ui_text_2": (230, 181, 37),  # secondary text color
            "background": (89, 96, 128),  # primary background color
            "background_2": (69, 98, 230),  # secondary background color
            "target_text": (69, 70, 76),  # color of text to be typed
            "correct_text": (230, 181, 37),  # color of correctly typed text
            "wrong_text": (205, 115, 85)  # color of incorrectly typed text
        }

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def get_color_of(self, component_name: str) -> tuple[int, int, int]:
        """
        Returns the color of the given component name,
        if name is not recognized return chartreuse	#7FFF00	(127,255,0) - jest to neonowo żółty
        :param component_name: name of the component
        :return: RGB color value
        """
        if component_name in self._colorPalette:
            return self._colorPalette[component_name]
        else:
            return (127, 255, 0)

    def start(self):
        pass

    def stop(self):
        pass
