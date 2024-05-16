from pygame_gui.elements import UILabel


class Counter:
    _start_time: int
    _is_active: bool
    _ui_label: UILabel

    def __init__(self, *args, **kwargs):
        self._start_time = 0
        self._is_active = False
        self._ui_label = UILabel(*args, **kwargs)

    def start(self) -> bool:
        raise NotImplementedError

    def stop(self) -> bool:
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def get_time(self) -> int:
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
