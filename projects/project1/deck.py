from datastructures.bag import Bag
from card import Card, CardFace, CardSuit
from random import choice   


class Deck(Bag):
    def __init__(self, multi:int = 1):
        for i in range(multi):
            for suit in list(CardSuit):
                for face in list(CardFace):
                    match face.name:
                        case "ACE":
                            point_value = 1
                        case "JACK" | "QUEEN" | "KING":
                            point_value = 10
                        case _:
                            point_value = int(face.value)
                    self.add(Card(card_face=face, card_value=point_value, card_suit=suit))
    
    def deal(self):
        dealt_card = choice(list(self))
        self.remove(dealt_card)
        return dealt_card




              




   

