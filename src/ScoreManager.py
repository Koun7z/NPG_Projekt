from src.Enumerators import Mode, Difficulty
from src.StorageManager import StorageManager
from src.Score import Score


class ScoreManager:
    _instance = None
    _current_correct_chars: int
    _score: Score

    _storage_manager: StorageManager

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._current_correct_chars = 0
        self.storage_manager = StorageManager()

    def __del__(self):
        pass

    def update_score(self, n_chars: int):
        """
        Updates the score based on the current progress
        :param n_chars: Number of correctly typed characters
        """
        self._current_correct_chars += n_chars

    def calculate_score(self, mode: Mode, difficulty: Difficulty, time: float) -> None:
        """
        Creates new score object
        :param mode: Current game mode
        :param difficulty: Current difficulty level
        :param time: Time taken
        """
        raise NotImplementedError

    def rank_score(self) -> bool:
        """
        Compares current score with all other saved scores of same mode and difficulty.
        :return: True if score in top 10
        """
        raise NotImplementedError

    def update_top_10(self) -> None:
        """
        Updates score list with top 10 scores.
        """
        raise NotImplementedError






