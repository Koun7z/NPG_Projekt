import pygame
import pygame_gui

from src.Layout import Layout
from typing import List


class ClassicGameLayout(Layout):
    def __init__(self):
        from src.UIManager import UIManager
        self._manager = pygame_gui.UIManager((UIManager().get_width_window(),
                                              UIManager().get_height_window()))

        # Tutaj możesz inicjować wszystkie elementy potrzebne do układu gry
        # Na przykład tło, przyciski, obiekty gry, itp.
        self._colorPalette = {
            "ui_text": (69, 70, 76),         # primary text dolor
            "ui_text_2": (230, 181, 37),     # secondary text color
            "background": (89, 96, 128),     # primary background color
            "background_2": (69, 98, 230),   # secondary background color
            "target_text": (69, 70, 76),     # color of text to be typed
            "correct_text": (230, 181, 37),  # color of correctly typed text
            "wrong_text": (205, 115, 85)     # color of incorrectly typed text
        }

        self._fontPalette = {
            "ui_font": UIManager().get_font("Lucida Sans"),
            "target_font": UIManager().get_font("Consolas")  # must be monospace
        }

    def render(self, window: pygame.display, events: List[pygame.event.Event]):
        from src.UIManager import UIManager

        for event in events:
            self._manager.process_events(event)

        self._manager.update(UIManager().get_delta_time())

        window.fill((255, 255, 255))  # TODO: Change to window.fill(self.get_color_of("background"))
                                      # after implementing function

        # Tutaj możesz dodać renderowanie innych elementów układu gry
        # Na przykład przyciski, obiekty gry, itp.

        self._manager.draw_ui(window)
        pygame.display.update()
