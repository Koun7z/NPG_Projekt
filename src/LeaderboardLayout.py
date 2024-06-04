import math
from typing import List

import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel

from src.Enumerators import Mode, Difficulty
from src.Layout import Layout
from src.Score import Score
from src.ScoreManager import ScoreManager
from src.GameManager import GameManager
from src.StorageManager import StorageManager


class LeaderboardLayout(Layout):
    _add_name: bool

    def __init__(self):
        super().__init__()
        from src.UIManager import UIManager

        self.mode = Mode.Classic
        self.difficulty = Difficulty.Easy
        self._manager = pygame_gui.UIManager((UIManager().get_width_window(),
                                              UIManager().get_height_window()), "./resources/themes.json")

        self._top_bar = UIPanel(relative_rect=pygame.Rect((-10, -10), (UIManager().get_width_window() + 20, 200)),
                                object_id=ObjectID(class_id='@top_bar_leader',
                                                   object_id='#top_bar_leader'),
                                margins={"left": 0, "top": 0, "right": 0, "bottom": 0},
                                manager=self._manager)

        self._prev_button = UIButton(relative_rect=pygame.Rect((50, 50), (200, 100)),
                                     object_id=ObjectID(class_id='@top_bar_button_leader', object_id='#prev_button'),
                                     manager=self._manager,
                                     text="Back",
                                     container=self._top_bar)

        self.classic_easy_button = UIButton(relative_rect=pygame.Rect((280, 50), (220, 100)),
                                            object_id=ObjectID(class_id='@top_bar_button_leader',
                                                               object_id='#classic_easy_button'),
                                            manager=self._manager,
                                            text="Classic(Łatwy)",
                                            container=self._top_bar)

        self.classic_medium_button = UIButton(relative_rect=pygame.Rect((500, 50), (220, 100)),
                                              object_id=ObjectID(class_id='@top_bar_button_leader',
                                                                 object_id='#classic_medium_button'),
                                              manager=self._manager,
                                              text="Classic(Średni)",
                                              container=self._top_bar)

        self.classic_hard_button = UIButton(relative_rect=pygame.Rect((720, 50), (220, 100)),
                                            object_id=ObjectID(class_id='@top_bar_button_leader',
                                                               object_id='#classic_hard_button'),
                                            manager=self._manager,
                                            text="Classic(Trudny)",
                                            container=self._top_bar)

        self.fall_letters_button = UIButton(relative_rect=pygame.Rect((950, 50), (250, 100)),
                                            object_id=ObjectID(class_id='@top_bar_button_leader',
                                                               object_id='#train_button'),
                                            manager=self._manager,
                                            text="Spadające literki",
                                            container=self._top_bar)
        self.fall_letters_button.disable()

        self.leader_list: List[UILabel] = []
        self.add_leader_list((100, 190))
        self.add_leader_list((100, 330))
        self.add_leader_list((100, 470))
        self.add_leader_list((100, 610))
        self.add_leader_list((100, 750))

        self.add_leader_list((750, 190))
        self.add_leader_list((750, 330))
        self.add_leader_list((750, 470))
        self.add_leader_list((750, 610))
        self.add_leader_list((750, 750))

    def add_leader_list(self, position: (int, int)):
        UIPanel(relative_rect=pygame.Rect(position, (600, 140)),
                object_id=ObjectID(class_id='@leader_list_item_bg',
                                   object_id='#leader_list_item_bg'),
                manager=self._manager)
        self.leader_list.append(UILabel(
            relative_rect=pygame.Rect(position,
                                      (600, 150)),
            text="Miejsce",
            object_id=ObjectID(class_id='@leader_list_item', object_id='#leader_list_item'),
            manager=self._manager))

    def change_layout(self, mode: Mode, difficulty: Difficulty):
        self.mode = mode
        self.difficulty = difficulty
        self.load_score()

    def load_score(self):
        scores: List[Score] = StorageManager().load_player_scores(self.mode)
        scores = list(filter(lambda s: s.difficulty == self.difficulty, scores))
        scores = sorted(scores, key=lambda s: s.ranking)
        print(scores)
        print(len(scores))
        for i in range(len(self.leader_list)):
            if len(scores) > i:
                self.leader_list[i].set_text(scores[i].to_leaderboard())
            else:
                self.leader_list[i].set_text("")

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        from src.UIManager import UIManager
        window.fill(self.get_color_of("background"))

        for event in events:

            self._manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == self._prev_button:
                    UIManager().change_layout("Main_Menu_Layout")
                    break

                if event.ui_element == self.classic_easy_button:
                    self.change_layout(Mode.Classic, Difficulty.Easy)
                elif event.ui_element == self.classic_medium_button:
                    self.change_layout(Mode.Classic, Difficulty.Medium)
                elif event.ui_element == self.classic_hard_button:
                    self.change_layout(Mode.Classic, Difficulty.Hard)
                elif event.ui_element == self.fall_letters_button:
                    self.change_layout(Mode.FallingLetters, Difficulty.Easy)

            GameManager().handle_input(event)

        self._manager.update(UIManager().get_delta_time())

        self._manager.draw_ui(window)

        pygame.display.update()

    def start(self):
        GameManager().clear_input()
        self.load_score()

    def stop(self):
        ScoreManager.reset()
