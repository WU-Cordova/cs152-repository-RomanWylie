from enum import Enum
from dataclasses import dataclass

class CardSuit(Enum):
    SPADES = "♠️"
    HEARTS = "♥️"
    CLUBS = "♣️"
    DIAMONDS = "♦️"

class CardFace(Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"    
    KING = "K"

@dataclass
class Card:
    card_face : CardFace
    point_value : int
    card_suit : CardSuit