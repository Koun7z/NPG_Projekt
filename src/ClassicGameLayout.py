import math

import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel

from src.Counter import Counter
from src.Layout import Layout
from typing import List

from src.ScoreManager import ScoreManager


class ClassicGameLayout(Layout):

    game_active: bool = False

    def __init__(self):

        super().__init__()

        from src.UIManager import UIManager
        self._manager = pygame_gui.UIManager((UIManager().get_width_window(),
                                              UIManager().get_height_window()), "./resources/themes.json")

        # te -10 i 20 to są magiczne liczby bo idk czemu mam jakieś dziwne marginesy
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

        self._timer = Counter(relative_rect=pygame.Rect((-150, 10), (100, 100)),
                              anchors={'top': 'top',
                                       'right': 'right'},
                              text="timer",
                              object_id=ObjectID(class_id='@counter', object_id='#counter'),
                              manager=self._manager
                              )

        self._progress_test = UILabel(relative_rect=pygame.Rect((-150, 60), (100, 100)),
                                      anchors={'top': 'top',
                                               'right': 'right'},
                                      text="30%",
                                      object_id=ObjectID(class_id='@progress_test', object_id='#progress_test'),
                                      manager=self._manager)

        self.next_line_holder = UILabel(relative_rect=pygame.Rect((0, UIManager().get_height_window() / 2 + 20),
                                                                  (UIManager().get_width_window(), 100)),
                                        text="Lorem ipsum ...",
                                        object_id=ObjectID(class_id='@next_line_holder', object_id='#next_line_holder'),
                                        manager=self._manager)

    def render(self, window: pygame.Surface, events: List[pygame.event.Event]):
        from src.UIManager import UIManager
        from src.GameManager import GameManager

        ui_manager = UIManager()
        game_manager = GameManager()

        for event in events:
            self._manager.process_events(event)

            if not self.game_active:
                game_manager.clear_input()
                if event.type == pygame.KEYDOWN:  # Game starts after pressing first key
                    self.game_active = True
                    self._timer.start()
                    ScoreManager().set_time(self._timer)

            game_manager.handle_input(event)

        self._manager.update(UIManager().get_delta_time())
        self._timer.update()
        self.next_line_holder.set_text(GameManager().get_next_target_sentence())
        self._progress_test.set_text(str(math.floor(GameManager().get_progress() * 100)) + "%")

        window.fill(self.get_color_of("background"))

        font = self.get_font_of("target_font")
        target = game_manager.get_target_text()

        target_size = font.size(target)
        font_size = font.point_size
        width = ui_manager.get_width_window()

        if target_size[0] > width - 10:
            font.set_point_size(int(font_size * (1 - (target_size[0] - (width - 10)) / (width - 10))))

        text_surface = ui_manager.render_input_text_surface(font)

        left_offset = (ui_manager.get_width_window() - font.size(target)[0]) / 2
        top_offset = ui_manager.get_height_window() / 2
        window.blit(text_surface, (left_offset, top_offset))

        font.set_point_size(font_size)

        # Tutaj możesz dodać renderowanie innych elementów układu gry
        # Na przykład przyciski, obiekty gry, itp.
        self._manager.draw_ui(window)
        pygame.display.update()

    def stop(self):
        self._timer.stop()

