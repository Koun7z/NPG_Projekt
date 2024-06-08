import json
from typing import Dict, List
from src.Enumerators import Difficulty, Mode
from src.Score import Score


class StorageManager:
    _instance = None
    _quotes_path_list: Dict[Difficulty, str]
    _score_path_list: Dict[tuple[Mode, Difficulty], str]
    _quotes: dict[Difficulty, List[str]]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._player_scores = {}
        self._quotes = {}
        self._quotes_path_list = {
            Difficulty.Easy: "./resources/texts/easy_quotes.txt",
            Difficulty.Medium: "./resources/texts/medium_quotes.txt",
            Difficulty.Hard: "./resources/texts/hard_quotes.txt"}

        self._score_path_list = {
            (Mode.Classic, Difficulty.Easy): "./data/savefiles/classic_scores_easy.cvs",
            (Mode.Classic, Difficulty.Medium): "./data/savefiles/classic_scores_medium.cvs",
            (Mode.Classic, Difficulty.Hard): "./data/savefiles/classic_scores_hard.cvs",
            (Mode.FallingLetters, Difficulty.Easy): "./data/savefiles/falling_scores_easy.cvs",
            (Mode.FallingLetters, Difficulty.Medium): "./data/savefiles/falling_scores_medium.cvs",
            (Mode.FallingLetters, Difficulty.Hard): "./data/savefiles/falling_scores_hard.cvs",
            (Mode.Training, Difficulty.Easy): "./data/savefiles/training_scores_easy.cvs",
            (Mode.Training, Difficulty.Medium): "./data/savefiles/training_scores_medium.cvs",
            (Mode.Training, Difficulty.Hard): "./data/savefiles/training_scores_hard.cvs"
        }

    def save_player_scores(self, scores: List[Score], mode: Mode, diff: Difficulty) -> bool:
        """
        Saves passed list of scores
        :param scores: list of scores
        :param mode: game mode
        :param diff: game difficulty
        :return: True if successful, False otherwise
        """
        try:
            filename = self._score_path_list[(mode, diff)]

            f = open(filename, 'w')
            for score in scores:
                f.write(score.toCSV() + '\n')

        except Exception as e:
            print(f"Error saving player scores: {e}")
            return False

        f.close()
        return True

    def load_player_scores(self, mode: Mode, diff: Difficulty) -> List[Score]:
        """
        Returns list of saved scores
        :param mode: game mode
        :param diff: game difficulty
        :return: list of saved scores
        """
        try:
            filename = self._score_path_list[(mode, diff)]
            with open(filename, 'r') as f:

                lines: list[str] = f.readlines()
                scores: list[Score] = []

                for line in lines:
                    data = [item.strip() for item in line.split(',')]
                    scores.append(Score(int(data[2]), data[1], int(data[0]), float(data[3]), Mode(int(data[4])),
                                        Difficulty(int(data[5]))))

                return scores
        except Exception as e:
            return []


    def load_quotes(self, diff: Difficulty, mode: Mode) -> bool:
        """
        Load quotes from file
        :return: true if successfully loaded quotes
        """
        try:
            filename = self._quotes_path_list[diff]
            with open(filename, 'r', encoding='utf-8') as f:
                self._quotes[diff] = [line.strip() for line in f if line.strip()]
            return True
        except Exception as e:
            return False

    def get_quotes(self, diff: Difficulty, mode: Mode) -> List[str]:
        """
        Returns list of quotes, loads quotes if not loaded
        :param diff: difficulty
        :param mode: game mode
        :return: list of quotes
        """
        if diff not in self._quotes:
            self.load_quotes(diff, mode)
        return self._quotes[diff]
