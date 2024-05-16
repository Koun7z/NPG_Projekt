from pygame_gui.elements import UILabel
from datetime import datetime


class Counter:
    _start_time: datetime
    _stop_time: datetime
    _is_active: bool
    _ui_label: UILabel

    def __init__(self, *args, **kwargs):
        self._start_time = datetime.now()
        self._stop_time = datetime.now()
        self._is_active = False
        self._ui_label = UILabel(*args, **kwargs)

    def start(self) -> bool:
        if self._is_active:
            return False
        self._is_active = True
        self._start_time = datetime.now()
        return True

    def stop(self) -> bool:
        if not self._is_active:
            return False
        self._is_active = False
        self._stop_time = datetime.now()
        return True

    def reset(self):
        raise NotImplementedError

    def get_time(self) -> int:
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
