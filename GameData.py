from Player import Player
from Deck import Deck

class GameData:
    def __init__(self, players: list[Player], playerToStart: int, numStartingCards: int = 4, clockwise: bool = True):
        self._players = players
        self._playerToStart = playerToStart
        self._clockwise = clockwise
        self._numStartingCards = numStartingCards

        self._numPlayers = len(players)
        self._matchPlayed: bool = False
        self._cambioCalled: bool = False
        self._currentPlayer: int = self._playerToStart
        self._deck = Deck()
        self._cards = [[] for _ in range(self._numStartingCards)]

        for _ in range(self._numStartingCards):
            for player in range(self._numPlayers):
                self._cards[player].append(self._deck.pop())
        
    def __str__(self):
        printStatement = ""
        printStatement += f"Current turn: {self._players[self._currentPlayer]._username}\n"
        for i in range(self._numPlayers):
            printStatement += self._players[i]._username + "\n"
            printStatement += "    " + str(self._cards[i]) + "\n"
        return printStatement
        