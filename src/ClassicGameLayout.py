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

    def render(self, window: pygame.display, events: List[pygame.event.Event]):
        from src.UIManager import UIManager

        for event in events:
            self._manager.process_events(event)

        self._manager.update(UIManager().get_delta_time())

        window.fill((255, 255, 255))

        # Tutaj możesz dodać renderowanie innych elementów układu gry
        # Na przykład przyciski, obiekty gry, itp.

        self._manager.draw_ui(window)
        pygame.display.update()
