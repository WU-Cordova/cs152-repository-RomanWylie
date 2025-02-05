from random import choice
from deck import Deck

class Game:
    def __init__(self):
        self.__playerhand = ()
        self.__dealerhand = ()
        self.__multiplier = (2,4,6,8)
    
    def round_start(self):
        round_deck = Deck(choice(self.__multiplier))


