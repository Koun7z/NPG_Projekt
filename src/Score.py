from src.Enumerators import Mode, Difficulty


class Score:
    value: int
    player_name: str
    ranking: int
    time: float
    mode: Mode
    difficulty: Difficulty

    def __init__(self, value: int = 0, player_name: str = "", ranking: int = -1, time: float = -1, mode: Mode = Mode.Classic, difficulty: Difficulty = Difficulty.Easy):
        self.value = value
        self.player_name = player_name
        self.ranking = ranking
        self.time = time
        self.mode = mode
        self.difficulty = difficulty

