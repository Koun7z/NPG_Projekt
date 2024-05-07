from typing import List

import pygame


class Layout:
    def render(self, window: pygame.window, events: List[pygame.event.Event]):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
