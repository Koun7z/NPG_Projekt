import json
from typing import Dict, List
from src.Enumerators import Difficulty, Mode
from src.ScoreManager import Score


class StorageManager:
    _instance = None
    _path_list: Dict[str, str]
    _quotes: List[str]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._player_scores = {}
        self._quotes = []
        self._path_list = {"Difficulty.Easy": "../resources/texts/easy_quotes.json",
                           "Difficulty.Medium": "../resources/texts//medium_quotes.json",
                           "Difficulty.Hard": "../resources/texts//hard_quotes.json",
                           "player": "../resources/players/scores.json"}

    # def add_player_score(self, score: Score) -> None:
    #     self._player_scores.append(score)

    # def get_player_score(self, player_name: str) -> int:
    #     return self._player_scores.get(player_name, 0)

    def save_player_scores(self, scores: List[Score]) -> bool:
        """
        Saves passed list of scores
        :param scores: list of scores
        :return: True if successful, False otherwise
        """
        try:
            filename = self._path_list["player"]
            with open(filename, 'w') as f:
                json.dump(scores, f)
            return True
        except Exception as e:
            print(f"Error saving player scores: {e}")
            return False

    def load_player_scores(self) -> List[Score]:
        try:
            filename = self._path_list["player"]
            with open(filename, 'r') as f:
                return json.load(f)

        except Exception as e:
            print(f"Error loading player scores: {e}")

        return []

    def load_quotes(self, diff: Difficulty, mode: Mode) -> bool:
        """
        Load quotes from file
        :return: true if successfully loaded quotes
        """
        try:
            filename = self._path_list[str(diff)]
            with open(filename, 'r', encoding='utf-8') as f:
                self._quotes = [line.strip() for line in f if line.strip()]
            return True
        except Exception as e:
            print(f"Error loading quotes: {e}")
            return False

    def get_quotes(self, diff: Difficulty, mode: Mode) -> List[str]:
        """
        Returns list of quotes, loads quotes if not loaded
        :param diff: difficulty
        :param mode: game mode
        :return: list of quotes
        """
        if self._quotes is None or len(self._quotes) == 0:
            self.load_quotes(diff, mode)
        return self._quotes
