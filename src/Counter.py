from pygame_gui.elements import UILabel
import time


class Counter:
    _start_time: float
    _stop_time: float
    _is_active: bool
    _ui_label: UILabel

    def __init__(self, *args, **kwargs):
        self._start_time = 0
        self._stop_time = 0
        self._is_active = False
        self._ui_label = UILabel(*args, **kwargs)

    def start(self) -> bool:
        if self._is_active:
            return False
        self._is_active = True
        self._start_time = time.time()
        return True

    def stop(self) -> bool:
        if not self._is_active:
            return False
        self._is_active = False
        self._stop_time = time.time()
        return True

    def reset(self):
        raise NotImplementedError

    def get_time(self) -> int:
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
