import json
from typing import Dict, List
from Enumerators import Difficulty


class StorageManager:
    _instance = None
    _player_scores: Dict[str, int]
    _path_list: Dict[str, str]
    _quotes: List[str]
    _diff: Difficulty

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self._player_scores = {}
        self._quotes = []
        self._path_list = {"1": "../resources/texts/easy_qutes.json", "2": "../resources/texts//medium_qutes.json",
                           "3": "../resources/texts//hard_qutes.json", "player": "../resources/players/scores.json"}
        self._diff = Difficulty.Easy

    def change_difficulty(self, diff: Difficulty):
        self._diff = diff

    def add_player_score(self, player_name: str, score: int) -> bool:
        self._player_scores[player_name] = score * self._diff.value
        return True

    def get_player_score(self, player_name: str) -> int:
        return self._player_scores.get(player_name, 0)

    # CHYBA TRZEBA BD NOWY KATALOG NA PLIKI DO ZAPISU ALBO W DOCS JE WRZUCAĆ
    def save_player_scores(self) -> bool:
        try:
            filename = self._path_list["player"]
            with open(filename, 'w') as f:
                json.dump(self._player_scores, f)
            return True
        except Exception as e:
            print(f"Error saving player scores: {e}")
            return False

    def load_player_scores(self) -> bool:
        try:
            filename = self._path_list["player"]
            with open(filename, 'r') as f:
                self._player_scores = json.load(f)
            return True
        except Exception as e:
            print(f"Error loading player scores: {e}")
            return False

    def load_quotes(self) -> bool:
        # GRUBA UWAGA JEŚLI JA BYM NIE ROBIŁ W line.strip() trzeba podawać odpowiednio czym rozdzielamy linie albo jakie znaki chcemy usunąć niepotrzebne
        # TU BYM SIĘ ZASTANOWIŁ CZY NIE LEPIEJ PO ANG TE CYTATY PISAĆ
        try:
            filename = self._path_list[str(self._diff)]
            with open(filename, 'r', encoding='utf-8') as f:
                self._quotes = [line.strip() for line in f if line.strip()]
            return True
        except Exception as e:
            print(f"Error loading quotes: {e}")
            return False

    def get_quotes(self) -> List[str]:
        if self._quotes is None or len(self._quotes) == 0:
            print("There are no quotes to load :(")
            self.load_quotes()
        return self._quotes
