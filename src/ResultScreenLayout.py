from typing import List

import pygame
import pygame_gui

from src.Layout import Layout
from src.ScoreManager import ScoreManager
from src.GameManager import GameManager


class ResultScreenLayout(Layout):

    _add_name: bool

    def __init__(self):
        super().__init__()

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        from src.UIManager import UIManager
        window.fill(self.get_color_of("background"))

        for event in events:
            # Events not related to inputting name should be handled before this if statement
            if not self._add_name:
                continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # K_RETURN to enter xd
                ScoreManager().set_player_name(GameManager().get_input_text())
                GameManager().clear_input()
                ScoreManager().update_top_10()
                self._add_name = False
            GameManager().handle_input(event)

        font = self.get_font_of("ui_font")  #
        size = font.point_size              # To tu taK tymczasowo
        font.set_point_size(50)             #
        font.align = pygame.FONT_CENTER
        if self._add_name:
            window.blit(font.render("Enter your name to save score", True, self.get_color_of("ui_text")), (400, 100))

        window.blit(font.render(f"Tu bedzie wynik, a tak tymczasowo:\n"
                                f"Name: {ScoreManager().get_score().player_name}{GameManager().get_input_text()}\n"
                                f"Score: {ScoreManager().get_score().value}\n"
                                f"Time: {ScoreManager().get_score().time // 60:.0f}:{ScoreManager().get_score().time % 60:.0f},{(ScoreManager().get_score().time * 100) % 100:.0f}\n"
                                , True, self.get_color_of("ui_text")), (400, 400))

        font.set_point_size(size)  # To też
        font.align = pygame.FONT_LEFT
        pygame.display.update()

    def start(self):
        GameManager().clear_input()
        self._add_name = ScoreManager().rank_score()
