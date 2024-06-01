import math
from typing import List

from src.Enumerators import Mode, Difficulty
from src.StorageManager import StorageManager
from src.Score import Score
from src.Counter import Counter


class ScoreManager:
    _instance = None
    _current_correct_chars: int
    _score: Score
    _time: Counter

    _storage_manager: StorageManager
    _top10_scores: List[Score]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._current_correct_chars = 0
        self.storage_manager = StorageManager()
        self._score = Score()

    def __del__(self):
        pass

    def set_player_name(self, name: str) -> None:
        """
        Sets the name of the score owner
        :param name: Player name
        :return:
        """
        self._score.player_name = name

    def update_score(self, n_chars: int) -> None:
        """
        Updates the score based on the current progress
        :param n_chars: Number of correctly typed characters
        """
        self._current_correct_chars += n_chars

    def calculate_score(self, mode: Mode, difficulty: Difficulty) -> None:
        """
        Creates new score object
        :param mode: Current game mode
        :param difficulty: Current difficulty level
        :param time: Time taken
        :return score
        """

        self._score.difficulty = difficulty
        self._score.mode = mode
        self._score.time = self._time.get_time_f()

        multiplier = difficulty.value
        match mode:
            case Mode.Classic:
                self._score.value = math.floor(self._current_correct_chars / (self._time.get_time_f() + 1) * multiplier * 100)

            case _:
                raise ValueError(f'Invalid mode: {mode}')

    def get_score(self):
        return self._score

    def rank_score(self) -> bool:
        """
        Compares current score with all other saved scores of same mode and difficulty.
        :return: True if score in top 10
        """
        scores = StorageManager().load_player_scores(self._score.mode)

        scores.append(self._score)
        scores.sort(key=lambda score: score.value, reverse=True)
        self._top10_scores = scores[:10]

        self._score.ranking = scores.index(self._score) + 1

        if self._score.ranking <= 10:
            for i in range(self._score.ranking, len(self._top10_scores)):
                self._top10_scores[i].ranking += 1
            return True

        return False

    def update_top_10(self) -> None:
        """
        Updates score list with top 10 scores.
        """
        StorageManager().save_player_scores(self._top10_scores, self._score.mode)

    def set_time(self, ctr: Counter) -> None:
        self._time = ctr
