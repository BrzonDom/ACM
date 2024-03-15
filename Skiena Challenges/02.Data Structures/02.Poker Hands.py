"""

Poker Hands

    A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts,
    or spades (denoted C, D, H, S in the input data). Each card also has a value of either 2
    through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A)


    Input:
        The input file contains several lines, each containing the designation of ten cards: the
        first five cards are the hand for the player named “Black” and the next five cards are
        the hand for the player named “White”

    Output:
        For each line of input, print a line containing one of the following:

            Black wins.
            White wins.
            Tie.


    Sample:

        2H 3D 5S 9C KD
        2C 3H 4S 8C AH
            => White wins

        2H 4S 4C 2D 4H
        2S 8S AS QS 3S
            => Black wins

        2H 3D 5S 9C KD
        2C 3H 4S 8C KH
            => Black wins

        2H 3D 5S 9C KD
        2D 3H 5C 9S KH
            => Tie

"""


if __name__ == '__main__':

    cardDict = {
        '2' :  2,
        '3' :  3,
        '4' :  4,
        '5' :  5,
        '6' :  6,
        '7' :  7,
        '8' :  8,
        '9' :  9,
        'T' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }

    org_hands = ["2H", "3D", "5S", "9C", "KD",
             "2C", "3H", "4S", "8C", "AH"]

    print("Black: ", end="")
    for card in org_hands[0:5]:
        print(card, end=" ")
    print("\n")

    print("White: ", end="")
    for card in org_hands[5:10]:
        print(card, end=" ")