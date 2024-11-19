import itertools
import random

color = {"S", "H", "D", "C"}
value = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
combination = itertools.product(color, value)

deck = [''.join(x) for x in combination]


def get_cards():

    selected_cards = []
    deck_temp = deck.copy()

    for x in range(51):

        card_drawn = random.choice(deck_temp)
        selected_cards.append(card_drawn)
        deck_temp.remove(card_drawn)

    cards_string = " ".join(selected_cards)

    return cards_string


def missing_card(cards):

    for card in deck:
        if card not in cards:
            return card


if __name__ == "__main__":
    selected_cards = get_cards()
    print("---"*40)
    print(f"the selected cards are: {selected_cards}")
    print(f"the missing card is: {missing_card(selected_cards)}")
    print("---"*40)
