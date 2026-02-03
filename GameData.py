from Player import Player
from Deck import Deck
from Enums import Moves, States
from Card import Card

class GameData:
    def __init__(self, players: list[Player], playerIdToStart: int, numStartingCards: int = 4, clockwise: bool = True):
        self._players = players
        self._playerToStart: Player = self.getPlayerById(playerIdToStart)
        self._clockwise = clockwise
        self._numStartingCards = numStartingCards
        
        self._state = States.WAITING_FOR_TURN
        self._numPlayers = len(players)
        self._matchPlayed: bool = False
        self._cambioCalled: bool = False
        self._currentPlayer: Player = self._playerToStart
        self._deck = Deck()
        self._hands = [[] for _ in range(self._numStartingCards)]
        self._matchPlayerId = None
        for _ in range(self._numStartingCards):
            for player in range(self._numPlayers):
                self._hands[player].append(self._deck.pop())

        self._mostRecentDiscard: Card = self._deck.pop()
        self._playerWaitingOnId = self._playerToStart._id

        self._stateBeforeMatch = None
        self._playerIndexToSendToMatch = None
        self._cardIndexToSendToMatch = None
        
    def __str__(self):
        printStatement = ""
        printStatement += f"Current turn: {self._currentPlayer._username}\n"
        printStatement += f"Current state: {self._state}\n"
        printStatement += f"Cambio called: {self._cambioCalled}\n"
        printStatement += f"Match played: {self._matchPlayed}\n"
        printStatement += f"Discard: {self._mostRecentDiscard}\n"
        for i in range(self._numPlayers):
            printStatement += f"{self._players[i]._username}: {sum(self._hands[i])}\n"
            printStatement += f"    {str(self._hands[i])}\n"
        return printStatement
    
    def getPlayerById(self, id) -> Player:
        for player in self._players:
            if player._id == id:
                return player
    
    def getHandIndexByPlayerId(self, id) -> int:
        for i in range(len(self._players)):
            if self._players[i]._id == id:
                return i

    def getCardByPlacement(self, card) -> Card:
        card -= 1 # Decrease by 1 for zero indexing
        for hand in self._hands:
            if len(hand) <= card:
                card -= len(hand)
            else:
                return hand[card]
        return -1
    
    def getCardIndexByPlacement(self, card) -> Card:
        card -= 1 # Decrease by 1 for zero indexing
        for hand in self._hands:
            if len(hand) <= card:
                card -= len(hand)
            else:
                return card
        return -1
    
    def getHandIndexByPlacement(self, card) -> Card:
        card -= 1 # Decrease by 1 for zero indexing
        for i in range(len(self._hands)):
            hand = self._hands[i]
            if len(hand) <= card:
                card -= len(hand)
            else:
                return i
        return -1

    def iterateTurn(self):
        currentPlayerIndex = self.getHandIndexByPlayerId(self._currentPlayer._id)
        if self._clockwise:
            self._currentPlayer = ( self._players[currentPlayerIndex] + 1 ) % self._numPlayers
        else:
            self._currentPlayer = ( self._players[currentPlayerIndex] - 1 ) % self._numPlayers
        self._playerWaitingOnId = self._currentPlayer._id
        self._state = States.WAITING_FOR_TURN


    def parsePlay(self, playerId: int, move: Moves, firstCard: int = -1, secondCard: int = -1) -> bool:
        # Can't do anything unless its your turn!
        if playerId != self._playerWaitingOnId and move != Moves.MATCH:
            return False
        
        # Cannot match if match already occurred
        if move == Moves.MATCH and self._matchPlayed:
            return False
        elif move == Moves.MATCH:
            # if correct match
            if self._mostRecentDiscard._rank == self.getCardByPlacement(firstCard)._rank:
                self._matchPlayed = True
                cardIndex = self.getCardIndexByPlacement(firstCard)
                handIndex = self.getHandIndexByPlacement(firstCard)
                self._mostRecentDiscard = self._hands[handIndex].pop(cardIndex)
                # if pulled from someone elses hand
                if self._players[handIndex]._id != playerId:
                    self._stateBeforeMatch = self._state
                    self._playerIndexToSendToMatch = handIndex
                    self._cardIndexToSendToMatch = cardIndex
                    self._state = States.WAITING_FOR_MATCH_GIVE_CARD
                    self._playerWaitingOnId = playerId
                return True
            else:
                index = self.getHandIndexByPlayerId(playerId)
                self._hands[index].append(self._deck.pop())
            return True
        elif self._state == States.WAITING_FOR_MATCH_GIVE_CARD and move == Moves.MATCH_GIVE_CARD:
            playerIndex = self.getHandIndexByPlacement(firstCard)
            cardIndex = self.getCardIndexByPlacement(firstCard)
            # if trying to give card not in hand
            if playerId != self._players[playerIndex]._id:
                return False
            cardToSwap = self._hands[playerIndex].pop(cardIndex)
            self._hands[self._playerIndexToSendToMatch].insert(self._cardIndexToSendToMatch, cardToSwap)
            self._playerWaitingOnId = self._currentPlayer._id
            self._state = self._stateBeforeMatch
            
            return True
        
        self._matchPlayed = False
        if self._state == States.WAITING_FOR_TURN:
            if move == Moves.DRAW:
                cardFromTop = self._deck.pop()
                print(f"{self.getPlayerById(playerId)._username} saw {cardFromTop}")
                self._state == States.WAITING_FOR_REPLACE_OR_PLAY
                return True
            elif move == Moves.TAKE_FROM_DISCARD:
                playerIndex = self.getHandIndexByPlacement(firstCard)
                cardIndex = self.getCardIndexByPlacement(firstCard)   
                if playerId != self._players[playerIndex]._id:
                    return False
                self._hands[playerIndex][cardIndex], self._mostRecentDiscard = (
                    self._mostRecentDiscard,
                    self._hands[playerIndex][cardIndex],
                )
                if not self._cambioCalled:
                    self._state = States.WAITING_FOR_CAMBIO
                else: 
                    self.iterateTurn()
                return True
            else: return False
        elif self._state == States.WAITING_FOR_CAMBIO:
            if move == Moves.CAMBIO:
                self._cambioCalled = True
                self.iterateTurn()
                return True
            elif move == Moves.PASS_CAMBIO:
                self.iterateTurn()
                return True
            else: return False

        else: return False
