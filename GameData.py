from Player import Player
from Deck import Deck
from Enums import Moves

class GameData:
    def __init__(self, players: list[Player], playerIdToStart: int, numStartingCards: int = 4, clockwise: bool = True):
        self._players = players
        self._playerToStart: Player = self.getPlayerById(playerIdToStart)
        self._clockwise = clockwise
        self._numStartingCards = numStartingCards

        self._numPlayers = len(players)
        self._matchPlayed: bool = False
        self._cambioCalled: bool = False
        self._currentPlayer: Player = self._playerToStart
        self._deck = Deck()
        self._cards = [[] for _ in range(self._numStartingCards)]

        for _ in range(self._numStartingCards):
            for player in range(self._numPlayers):
                self._cards[player].append(self._deck.pop())
        
    def __str__(self):
        printStatement = ""
        printStatement += f"Current turn: {self._currentPlayer._username}\n"
        printStatement += f"Cambio called: {self._cambioCalled}\n"
        printStatement += f"Match played: {self._matchPlayed}\n"
        for i in range(self._numPlayers):
            printStatement += f"{self._players[i]._username}: {sum(self._cards[i])}\n"
            printStatement += f"    {str(self._cards[i])}\n"
        return printStatement
    
    def getPlayerById(self, id) -> Player:
        for player in self._players:
            if player._id == id:
                return player

    def parsePlay(self, playerId: int, move: Moves, firstCard: int, secondCard:int) -> bool:
        # Cannot match if match already occurred
        if move == Moves.MATCH and self._matchPlayed:
            return False
        elif move == Moves.MATCH:
            return True
        
        if self._currentPlayer._id != playerId:
            return False
        
        if move == Moves.DRAW:
            drawnCard = self._deck.pop()
