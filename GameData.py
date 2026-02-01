class GameData:
    def __init__(self, numPlayers: int, playerToStart: int, clockwise: bool = True):
        self._numPlayers = numPlayers
        self._playerToStart = playerToStart
        self._clockwise = clockwise