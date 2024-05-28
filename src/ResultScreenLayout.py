from typing import List

import pygame
import pygame_gui

from src.Layout import Layout
from src.ScoreManager import ScoreManager

class ResultScreenLayout(Layout):
    def __init__(self):
        from src.UIManager import UIManager

        # Tutaj możesz inicjować wszystkie elementy potrzebne do układu gry
        # Na przykład tło, przyciski, obiekty gry, itp.
        self._colorPalette = {
            "ui_text": (69, 70, 76),  # primary text dolor
            "ui_text_2": (230, 181, 37),  # secondary text color
            "background": (89, 96, 128),  # primary background color
            "background_2": (69, 98, 230),  # secondary background color
            "target_text": (69, 70, 76),  # color of text to be typed
            "correct_text": (230, 181, 37),  # color of correctly typed text
            "wrong_text": (205, 115, 85)  # color of incorrectly typed text
        }

        self._fontPalette = {
            "ui_font": UIManager().get_font("ui"),
            "target_font": UIManager().get_font("text")  # must be monospace
        }

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        window.fill(self.get_color_of("background"))

        font = self.get_font_of("ui_font")  #
        size = font.point_size              # To tu taK tymczasowo
        font.set_point_size(50)             #

        window.blit(font.render(f"Tu bedzie wynik, a tak tymczasowo: {ScoreManager().get_score().value}", True, self.get_color_of("ui_text")), (400, 400))

        font.set_point_size(size)  # To też

        pygame.display.update()

