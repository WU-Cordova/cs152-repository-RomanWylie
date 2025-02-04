import random
from card import Card, CardFace, CardSuit

def main():
    cards = list()
    for suit in list(CardSuit):
        for face in list(CardFace):
            match face.name:
                case "ACE":
                    point_value = 1
                case "JACK" | "QUEEN" | "KING":
                    point_value = 10
                case _:
                    point_value = int(face.value)
            new_card = Card(card_face=face.value, card_suit=suit.value, card_value=point_value)
            cards.append(f"{new_card.card_face}{new_card.card_suit} worth {f"{new_card.card_value} or 11" if new_card.card_value==1 else new_card.card_value} in BagJack")
    print(random.choice(cards))



if __name__ == '__main__':
    main()
