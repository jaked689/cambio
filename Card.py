from Enums import Suit, Rank

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self._suit = suit
        self._rank = rank
    
    def __str__(self):
        return self.toString()
    
    def __repr__(self):
        return self.toString()
    
    def toString(self):
        if self._suit == Suit.JOKER and self._rank == Rank.JOKER:
            return "JK"
        if self._suit == Suit.CLUBS:
            suit = "♣"
        elif self._suit == Suit.DIAMONDS:
            suit = "♦"
        elif self._suit == Suit.HEARTS:
            suit = "♥"
        elif self._suit == Suit.SPADES:
            suit = "♠"
        else:
            suit = "?"

        if self._rank == Rank.ACE:
            rank = "A"
        elif self._rank == Rank.KING:
            rank = "K"
        elif self._rank == Rank.QUEEN:
            rank = "Q"
        elif self._rank == Rank.JACK:
            rank = "J"
        else:
            rank = str(self._rank.value)

        return f"{rank}{suit}"


    def isRed(self):
        if self._suit == Suit.HEARTS or self._suit == Suit.DIAMONDS:
            return True
        else:
            return False
        
    def getPointValue(self) -> int:
        value: int = self._rank.value
        if value <= 10:
            return value
        if self._rank == Rank.KING and self.isRed():
            return -1
        return 10