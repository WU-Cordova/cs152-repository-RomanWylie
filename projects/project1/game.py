from random import choice
from projects.project1.deck import Deck
from projects.project1.card import Card, CardFace, CardSuit

class Game:
    def __init__(self):
        self.__multiplier = (2,4,6,8)
        
    def play_game(self):
        self.__play_round()
        game_end = False
        while game_end == False:
            new_round = input("Play again? [y/n]")
            match new_round:
                case "y" | "Y" | "yes"| "YES"|"Yes":
                    self.__play_round()
                case "n"|"N"|"no"|"NO"|"No":
                    game_end = True
                    print("Thank you for playing!")
                    break


    def __play_round(self):
        self.player_score: int=0
        self.player_hand: list[Card]= []
        self.dealer_score: int=0
        self.dealer_hand: list[Card] = []
        self.turn = 1
        self.round_deck = Deck(choice(self.__multiplier))
        for i in range(2):
            dealt_card : Card = choice(self.round_deck.distinct_items())
            self.player_hand.append(dealt_card)
            self.__score_add(dealt_card)
            self.round_deck.remove(dealt_card)
        self.turn = 2
        for i in range(2):
            dealt_card : Card = choice(self.round_deck.distinct_items())
            self.dealer_hand.append(dealt_card)
            self.__score_add(dealt_card)
            self.round_deck.remove(dealt_card)
        print(f"Player hand: {str(self.player_hand[0])}{str(self.player_hand[1])} | Score: {self.player_score}")
        print (f"Dealer hand: {str(self.dealer_hand[0])}[??] | Score: {self.dealer_hand[0].card_face.face_value()}")
        self.turn = 1
        while self.turn == 1 :
            hit_query = input("Would you like to hit [H] or stay [S]?")
            match hit_query:
                case "S"|"stay"|"s"|"STAY"|"Stay":
                    self.turn=2
                    break
                case "H"|"hit"|"h"|"HIT"|"Hit":
                    self.__deal()
                    print(f"Player Hand:{"".join(str(self.player_hand[i]) for i in range(len(self.player_hand)))} | Score: {self.player_score}")
                case _: 
                    raise ValueError("Player must hit or stay")
            if self.player_score > 21:
                for card in self.player_hand:
                    if card.card_face.face_value==11:
                        self.player_score -= 10
                        break
                if self.player_score > 21:
                    self.turn = 2
                    print("Bust! Player loses")
        print(f"Dealer Hand: {str(self.dealer_hand[0])}{str(self.dealer_hand[1])} | Score: {self.dealer_score}")
        while self.turn == 2 and self.dealer_score < 17:
            self.__deal()
            print(f"Dealer Hand: {"".join(str(self.dealer_hand[i]) for i in range(len(self.dealer_hand)))}  | Score: {self.dealer_score}")
            if self.dealer_score > 21:
                print("Bust! Dealer loses")
        end_var=self.__end_round()
        print(end_var)

    def __end_round(self):
        if self.player_score > 21 and self.dealer_score > 21:
            return("No Winner")
        elif self.player_score > 21:
            return("Dealer Wins")
        elif self.dealer_score > 21:
            return("Player Wins")
        elif self.player_score >= self.dealer_score:
            return("Player Wins")
        elif self.dealer_score>=self.player_score:
            return("Dealer Wins")
        
        
        
                
    def __score_add(self, card:Card):
        if self.turn==1:
            card_score=int(card.card_face.face_value())
            self.player_score = self.player_score + card_score
        else:
            card_score=int(card.card_face.face_value())
            self.dealer_score = self.dealer_score + card_score

    def __deal(self):
        match self.turn: 
            case 1: 
                dealt_card : Card = choice(self.round_deck.distinct_items())
                self.player_hand.append(dealt_card)
                self.__score_add(dealt_card)
                self.round_deck.remove(dealt_card)
            case 2: 
                dealt_card : Card = choice(self.round_deck.distinct_items())
                self.dealer_hand.append(dealt_card)
                self.__score_add(dealt_card)
                self.round_deck.remove(dealt_card)


            


        


