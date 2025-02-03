from datastructures.bag import Bag
from card import Card, CardFace, CardSuit   


class Deck(Bag):
    def __init__(self):
        for suit in list(CardSuit):
            for face in list(CardFace):
                match face.name:
                    case "ACE":
                        card_value = 1
                    case "JACK" | "QUEEN" | "KING":
                        card_value = 10
                    case _:
                        card_value = face.value
                self.add(Card(card_face=face, point_value=card_value, card_suit=suit))




   

