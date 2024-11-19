import itertools
import random

color = {"S", "H", "D", "C"}
value = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
combination = itertools.product(color, value)

deck = [''.join(x) for x in combination]


def get_cards():

    selected_cards = []

    for x in range(51):
        selected_cards.append(random.choice(deck))

    cards_string = " ".join(selected_cards)

    return cards_string


def missing_card(cards):

    for card in deck:
        if card not in cards:
            return card

if __name__ == "__main__":
    print(get_cards())
