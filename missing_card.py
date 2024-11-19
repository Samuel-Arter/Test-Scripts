import itertools


def missing_card(cards):

    color = {"S", "H", "D", "C"}
    value = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}
    combination = itertools.product(color, value)

    deck = [''.join(x) for x in combination]

    for card in deck:
        if card not in cards:
            return card

print(missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"))
