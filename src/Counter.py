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
        """
        Method that starts the counter.
        :return:  Return True if counter was started.
        """
        if self._is_active:
            return False
        self._is_active = True
        self._start_time = time.time()
        return True

    def stop(self) -> bool:
        """
        Method that stops the counter.
        :return:  Return True if counter was stopped.
        """
        if not self._is_active:
            return False
        self._is_active = False
        self._stop_time = time.time()
        return True

    def reset(self):
        """
        Method that resets the counter.
        """
        self._start_time = time.time()
        self._stop_time = time.time()
        self._is_active = False

    def get_time(self) -> int:
        """
        Method that returns time on counter.
        :return:  Return time in seconds
        """
        return int(self.get_time_f())

    def get_time_f(self) -> float:
        if self._is_active:
            return time.time() - self._start_time
        return self._stop_time - self._start_time

    def update(self):
        """
        Method that update counter text
        """
        t = self.get_time()
        minutes = t // 60
        seconds = t % 60
        self._ui_label.set_text(f"{minutes:02}:{seconds:02}")
