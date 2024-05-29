from typing import List

import pygame
import pygame_gui

from src.Layout import Layout
from src.ScoreManager import ScoreManager


class ResultScreenLayout(Layout):
    def __init__(self):
        super().__init__()

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        window.fill(self.get_color_of("background"))

        font = self.get_font_of("ui_font")  #
        size = font.point_size              # To tu taK tymczasowo
        font.set_point_size(50)             #

        window.blit(font.render(f"Tu bedzie wynik, a tak tymczasowo: {ScoreManager().get_score().value}", True, self.get_color_of("ui_text")), (400, 400))

        font.set_point_size(size)  # To też

        pygame.display.update()

