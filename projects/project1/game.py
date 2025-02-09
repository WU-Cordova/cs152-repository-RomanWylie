from random import choice
from deck import Deck

class Game:
    def __init__(self):
        self.__playerhand : list=()
        self.__dealerhand : list=()
        self.__multiplier = (2,4,6,8)
    
    def round_start(self):
        turn: int = 0
        player_score: int=0
        dealer_score: int=0
        stay: bool=False
        round_deck = Deck(choice(self.__multiplier))
        for i in range(2):
            self.__playerhand.append(round_deck.deal)
        for i in range(2):
            self.__dealerhand.append(round_deck.deal)

            


        


