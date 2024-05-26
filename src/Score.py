from src.Enumerators import Mode, Difficulty


class Score:
    value: int
    player_name: str
    ranking: int
    time: float
    mode: Mode
    difficulty: Difficulty

    def __init__(self, value: int, player_name: str, ranking: int, time: float, mode: Mode, difficulty: Difficulty):
        self.value = value
        self.player_name = player_name
        self.ranking = ranking
        self.time = time
        self.mode = mode
        self.difficulty = difficulty
