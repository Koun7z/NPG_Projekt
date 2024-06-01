import math
from typing import List

import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel

from src.Layout import Layout
from src.ScoreManager import ScoreManager
from src.GameManager import GameManager


class ResultScreenLayout(Layout):
    _add_name: bool

    def __init__(self):
        super().__init__()

        from src.UIManager import UIManager
        self._manager = pygame_gui.UIManager((UIManager().get_width_window(),
                                              UIManager().get_height_window()), "./resources/themes.json")

        self._top_bar = UIPanel(relative_rect=pygame.Rect((-10, -10), (UIManager().get_width_window() + 20, 200)),
                                object_id=ObjectID(class_id='@top_bar',
                                                   object_id='#top_bar'),
                                margins={"left": 0, "top": 0, "right": 0, "bottom": 0},
                                manager=self._manager)

        self._prev_button = UIButton(relative_rect=pygame.Rect((50, 50), (200, 100)),
                                     object_id=ObjectID(class_id='@top_bar_button', object_id='#prev_button'),
                                     manager=self._manager,
                                     text="Back",
                                     container=self._top_bar)

        self._reset = UIButton(relative_rect=pygame.Rect((280, 50), (200, 100)),
                               object_id=ObjectID(class_id='@top_bar_button', object_id='#reset_button'),
                               manager=self._manager,
                               text="Restart",
                               container=self._top_bar)

        self._score_board_button = UIButton(relative_rect=pygame.Rect((510, 50), (200, 100)),
                                            object_id=ObjectID(class_id='@top_bar_button', object_id='#score_board_button'),
                                            manager=self._manager,
                                            text="Score Board",
                                            container=self._top_bar)

        self._enter_name_text = UILabel(relative_rect=pygame.Rect((350, -20), (UIManager().get_width_window(), 160)),
                                        text="Niestety nie udało ci się osiągnąć nowego rekordu",
                                        object_id=ObjectID(class_id='@progress_test', object_id='#progress_test'),
                                        manager=self._manager)

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        from src.UIManager import UIManager
        window.fill(self.get_color_of("background"))

        for event in events:

            self._manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == self._prev_button:
                    UIManager().change_layout("Main_Menu_Layout")
                    break

                if event.ui_element == self._reset:
                    GameManager().restart()
                    UIManager().change_layout(UIManager().get_layout_name_by_mode(GameManager().get_mode()))

                if event.ui_element == self._score_board_button:
                    # TODO: add Scoreboard transition
                    print("ScoreBoard")

            # Events not related to inputting name should be handled before this if statement
            if not self._add_name:
                continue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  # K_RETURN to enter xd

                ScoreManager().set_player_name(GameManager().get_input_text())
                GameManager().clear_input()
                ScoreManager().update_top_10()
                self._add_name = False
                self._enter_name_text.set_text("Wynik zapisany!")

            GameManager().handle_input(event)

        self._manager.update(UIManager().get_delta_time())

        font = UIManager().get_font("result")

        if self._add_name:
            if ScoreManager().get_score().ranking == 1:
                self._enter_name_text.set_text(
                    "Gratulacje osiągnąłeś nowy nalepszy wynik!\nWpisz imię aby go zapisać\n        ")
            else:
                self._enter_name_text.set_text(
                    f"Gratulacje osiągnąłeś {ScoreManager().get_score().ranking} nalepszy wynik!\nWpisz imię aby go zapisać\n       ")

        score_text = "Osiągnięty wynik:\n" \
                     f"Imię: {ScoreManager().get_score().player_name}{GameManager().get_input_text()}\n" \
                     f"Punkty: {ScoreManager().get_score().value}\n" \
                     f"Czas gry: {ScoreManager().get_score().time // 60:.0f}:{ScoreManager().get_score().time % 60:.0f},{(ScoreManager().get_score().time * 100) % 100:.0f}\n"

        text_surface = font.render(score_text, True, self.get_color_of("ui_text_2"))

        left_offset = math.ceil((UIManager().get_width_window() - text_surface.get_width()) / 2)
        top_offset = math.ceil((UIManager().get_height_window() + 100 - text_surface.get_height()) / 2)

        window.blit(text_surface, (left_offset, top_offset))

        self._manager.draw_ui(window)

        pygame.display.update()

    def start(self):
        GameManager().clear_input()
        self._add_name = ScoreManager().rank_score()

    def stop(self):
        ScoreManager.reset()
