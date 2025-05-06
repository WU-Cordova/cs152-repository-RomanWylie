from datastructures.bag import Bag
from projects.project1.card import Card, CardFace, CardSuit



def Deck(multi):
    deck = Bag()
    for i in range(multi):
        for suit in list(CardSuit):
            for face in list(CardFace):
                deck.add(Card(card_face=face,  card_suit=suit))
    return(deck)
    
    




              




   

