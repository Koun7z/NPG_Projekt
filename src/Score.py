from src.Enumerators import Mode, Difficulty


class Score:
    ranking: int
    player_name: str
    value: int
    time: float
    mode: Mode
    difficulty: Difficulty

    def __init__(self, value: int = 0, player_name: str = "", ranking: int = -1, time: float = -1,
                 mode: Mode = Mode.Classic, difficulty: Difficulty = Difficulty.Easy):
        self.value = value
        self.player_name = player_name
        self.ranking = ranking
        self.time = time
        self.mode = mode
        self.difficulty = difficulty

    def __str__(self) -> str:
        return f"{self.ranking}. Player: {self.player_name} | Score: {self.value} | Time: {self.time // 60}:{self.time % 60} | Mode: {self.mode.name} | Difficulty: {self.difficulty.name}"

    def to_leaderboard(self) -> str:
        return f"{self.ranking}. {self.player_name}:{self.value}"

    def toCSV(self) -> str:
        """
        :return: Score data in CSV format
        """
        return f"{self.ranking}, {self.player_name}, {self.value}, {self.time}, {self.mode.value}, {self.difficulty.value}"
