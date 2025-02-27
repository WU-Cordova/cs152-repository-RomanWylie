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

    def face_value(self) -> int:
        match self:
            case CardFace.JACK | CardFace.QUEEN | CardFace.KING:
                return int(10)
            case CardFace.ACE:
                return int(11)
            case _:
                return int(self.value)

@dataclass
class Card:
    card_face : CardFace
    card_suit : CardSuit
    def __hash__(self) -> int:
        return hash(self.card_face.name) * hash(self.card_suit.name)

    def __str__(self) -> str:
        return f"[{self.card_face.value}{self.card_suit.value}]"