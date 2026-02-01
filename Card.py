from Enums import Suit, Rank

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self._suit = suit
        self._rank = rank
    
    def __str__(self):
        return f"{self._rank.name.title()} of {self._suit.name.title()}"
    
    def __repr__(self):
        return f"{self._rank.name.title()} of {self._suit.name.title()}"

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