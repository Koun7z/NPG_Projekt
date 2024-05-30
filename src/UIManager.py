import math
from typing import Type

import pygame

from src.ClassicGameLayout import ClassicGameLayout
from src.MainMenuLayout import MainMenuLayout
from src.ResultScreenLayout import ResultScreenLayout
from src.Layout import Layout
from src.GameManager import GameManager


class UIManager:
    _instance = None
    _layouts: dict[str, Layout]
    _window: pygame.Surface
    _clock: pygame.time.Clock
    _current_layout: str
    _width_window: int
    _height_window: int
    _font: dict[str, pygame.font.Font]
    _running: bool
    _delta_time: float

    _game_manager: GameManager

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._width_window = 1600
        self._height_window = 900

        pygame.init()
        self._window = pygame.display.set_mode((self._width_window, self._height_window))
        self._clock = pygame.time.Clock()
        self._running = True

        self._font = {}
        self.add_font("text", pygame.font.Font("./resources/fonts/text/SometypeMono-Regular.ttf", 50))
        self.add_font("ui",
                      pygame.font.Font("./resources/fonts/UI/UbuntuMono-Regular.ttf", 20))  # UbuntuMono-Regular.ttf

        self._layouts = {
            "Main_Menu_Layout": MainMenuLayout(),
            "Classic_Game_Layout": ClassicGameLayout(),
            "ResultScreen_Layout": ResultScreenLayout(),
        }
        self._current_layout = ""
        self.change_layout("Main_Menu_Layout")

        self._game_manager = GameManager()

    def render(self):
        """
        Run main loop of game
        """
        while self._running:
            self._delta_time = self._clock.tick(60) / 1000.0
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.close()

            self.get_current_layout().render(self._window, events)

    def change_layout(self, layout_name: str) -> bool:
        """
        Changes active layout
        :param layout_name: layout name
        :return: True if successful
        """
        if layout_name in self._layouts:

            if self._current_layout != "":
                self.get_current_layout().stop()

            self._current_layout = layout_name

            self.get_current_layout().start()
            return True

        return False

    def get_current_layout_name(self) -> str:
        return self._current_layout

    def get_current_layout(self) -> Layout:
        return self._layouts.get(self._current_layout)

    def get_width_window(self) -> int:
        return self._width_window

    def get_height_window(self) -> int:
        return self._height_window

    def get_window(self) -> pygame.Surface:
        return self._window

    def get_font(self, font_name: str) -> pygame.font.Font:
        """
        Returns font for given name
        :param font_name: str - name of font
        :return: font
        """
        if font_name in self._font:
            return self._font[font_name]
        raise KeyError

    def get_delta_time(self):
        return self._delta_time

    def add_font(self, font_name: str, font: pygame.font.Font) -> bool:
        """
        Adds font to font database
        :param font_name: Name of adding font
        :param font: Object of adding font
        :return: True if successful
        """
        if font_name in self._font:
            return False
        self._font[font_name] = font
        return True

    def render_input_text_surface(self, font) -> pygame.Surface:
        """
        Renders target and inputted text
        :return: pygame.Surface with rendered text
        """
        layout = self.get_current_layout()

        text = self._game_manager.get_input_text()
        target = self._game_manager.get_target_text()

        background_color = layout.get_color_of("background")
        target_text_color = layout.get_color_of("target_text")
        correct_text_color = layout.get_color_of("correct_text")
        wrong_text_color = layout.get_color_of("wrong_text")

        good_chars = self._game_manager.handle_target_completed()

        good_text = text[0:good_chars]
        bad_text = text[good_chars:]

        good_size = font.size(good_text)
        bad_size = font.size(bad_text)

        target_render = font.render(target, True, target_text_color)
        input_render = font.render(good_text, True, correct_text_color)

        font.set_underline(True)
        line_render = font.render(" ", True, correct_text_color)
        input_render_err = font.render(bad_text, True, wrong_text_color)
        font.set_underline(False)

        rect = pygame.Rect(good_size[0], 0, bad_size[0], bad_size[1])
        pygame.draw.rect(target_render, background_color, rect)

        target_render.blit(input_render, (0, 0))
        target_render.blit(line_render, (good_size[0], 0))
        target_render.blit(input_render_err, (good_size[0], 0))

        return target_render

    def close(self):
        self._running = False
