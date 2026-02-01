import random
from Card import Card, Suit, Rank

class Deck:
    def __init__(self):
        self.populate()

    def __str__(self):
        return f"{self._deck}"
    
    def populate(self):
        self._deck = []
        for suit in Suit:
            for rank in Rank:
                if suit != Suit.JOKER and rank != Rank.JOKER:
                    self._deck.append(Card(suit, rank))
        self._deck.append(Card(Suit.JOKER, Rank.JOKER))
        self._deck.append(Card(Suit.JOKER, Rank.JOKER))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._deck)

    def pop(self) -> Card:
        return self._deck.pop(0)
