from enum import Enum, auto

class Suit(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()
    JOKER = auto()

class Rank(Enum):
    JOKER = 0
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Moves(Enum):
    DRAW = 1
    DRAW_PLAY_7_8 = 2
    DRAW_PLAY_9_10 = 3
    DRAW_PLAY_J = 4
    DRAW_PLAY_Q = 5
    DRAW_PLAY_K = 6
    LOOK_AT_CARD = 7
    SWAP_CARDS = 8

    TAKE_FROM_DISCARD = 9

    MATCH = 10
    
    CAMBIO = 11
    PASS_CAMBIO = 12