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
    DRAW = 0
    DRAW_REPLACE = 1
    DRAW_PLAY = 2
    LOOK_AT_CARD = 3
    SWAP_CARDS = 4

    TAKE_FROM_DISCARD = 5

    MATCH = 6
    MATCH_GIVE_CARD = 7
    
    CAMBIO = 8
    PASS_CAMBIO = 9

class States(Enum):
    WAITING_FOR_TURN = 0
    WAITING_FOR_REPLACE_OR_PLAY = 1
    WAITING_FOR_PICK_CARD_LOOK = 2
    WAITING_FOR_PICK_CARD_SWAP = 3
    WAITING_FOR_MATCH_GIVE_CARD = 4
    WAITING_FOR_CAMBIO = 5
