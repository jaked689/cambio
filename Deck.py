import random
from Card import Card, Suit, Rank

class Deck:
    def __init__(self):
        self._deck = []
        for suit in Suit:
            for rank in Rank:
                self._deck.append(Card(suit, rank))
        self.shuffle()

    def __str__(self):
        return f"{self._deck}"

    def shuffle(self):
        random.shuffle(self._deck)
