import math

import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel

from src.Counter import Counter
from src.Layout import Layout
from typing import List

from src.ScoreManager import ScoreManager


class MainMenuLayout(Layout):
    game_active: bool = False

    def __init__(self):
        super().__init__()

        from src.UIManager import UIManager
        self._manager = pygame_gui.UIManager((UIManager().get_width_window(),
                                              UIManager().get_height_window()), "./resources/themes.json")
        self._colorPalette["background"] = (69, 79, 76)
        self.title = UILabel(
            relative_rect=pygame.Rect((0, 40),
                                      (UIManager().get_width_window(), 150)),
            text="Mistrz Klawiatury",
            object_id=ObjectID(class_id='@title', object_id='#title'),
            manager=self._manager)

        self.ClassicButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150, 200), (300, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#ClassicButton'),
            manager=self._manager,
            text="Tryb Klasyczny")

        self.TrainButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150, 300), (300, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#TrainButton'),
            manager=self._manager,
            text="Trenuj")
        self.TrainButton.disable()
        self.FallingButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150, 400), (300, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#FallingButton'),
            manager=self._manager,
            text="Spadające literki")
        self.FallingButton.disable()
        self.LeaderboardButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150, 500), (300, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#LeaderboardButton'),
            manager=self._manager,
            text="Leaderboard")
        self.ExitButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150, 600), (300, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#ExitButton'),
            manager=self._manager,
            text="Exit")
        self.EasyButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150 - 150 / 2, 200), (150, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#EasyButton'),
            manager=self._manager,
            visible=False,
            text="Łatwy")

        self.MediumButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 - 150 / 2, 200), (150, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#MediumButton'),
            manager=self._manager,
            visible=False,
            text="Średni")
        self.HardButton = UIButton(
            relative_rect=pygame.Rect((UIManager().get_width_window() / 2 + 150 / 2, 200), (150, 100)),
            object_id=ObjectID(class_id='@UIButton', object_id='#HardButton'),
            manager=self._manager,
            visible=False,
            text="Trudny")

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        from src.UIManager import UIManager

        ui_manager = UIManager()

        for event in events:
            self._manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.LeaderboardButton:
                    print("Leaderboard")
                    # TODO: Add link to LeaderBoard
                elif event.ui_element == self.ExitButton:
                    ui_manager.close()
                elif event.ui_element == self.ClassicButton:
                    self.ClassicButton.hide()
                    self.EasyButton.show()
                    self.MediumButton.show()
                    self.HardButton.show()

        self._manager.update(UIManager().get_delta_time())

        window.fill(self.get_color_of("background"))

        # Tutaj możesz dodać renderowanie innych elementów układu gry
        # Na przykład przyciski, obiekty gry, itp.
        self._manager.draw_ui(window)
        pygame.display.update()
