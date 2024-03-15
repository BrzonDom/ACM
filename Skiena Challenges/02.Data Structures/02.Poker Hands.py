"""

Poker Hands

    A poker deck contains 52 cards. Each card has a suit of either clubs (♣), diamonds (♦),
    hearts (♥) or spades (♠), (denoted C, D, H, S in the input data). Each card also has a value
    of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A)

    Ranking of hands:

        1. High card

        2. Pair

        3. Two Pair

        4. Three of a Kind

        5. Straight

        6. Flush

        7. Full House

        8. Four of a Kind

        9. Straight Flush


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


# def Rank(hand):
#
#     rank1 = False
#     rank2 = False
#     rank3 = False
#
#     cnt = [0]
#
#     for c, card in enumerate(hand):
#
#         cnt = [0]
#
#         for pair in hand[c:]:
#             if card[0] == card[0]:
#                 cnt[-1] += 1




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

    tst_hand = ["2H", "2D", "2S", "5C", "5D"]



    # print("Black: ", end="")
    # hand_black = []
    #
    # for card in org_hands[0:5]:
    #     print(card, end=" ")
    #     hand_black.append((cardDict[card[0]], card[1]))
    #
    # print(f"\n\t\t{hand_black}")
    #
    # print("\n")
    #
    # print("White: ", end="")
    # hand_white = []
    #
    # for card in org_hands[5:10]:
    #     print(card, end=" ")
    #
    #     hand_white.append((cardDict[card[0]], card[1]))
    #
    # print(f"\n\t\t{hand_white}")


    print("Test: ", end="")
    hand_test = []

    for card in tst_hand:
        print(card, end=" ")

        hand_test.append((cardDict[card[0]], card[1]))

    print(f"\n\t\t{hand_test}")

    cnt = [0]
    mtch = 0

    for crd, card in enumerate(hand_test):

        if mtch > crd:
            continue

        if cnt[-1]:
            cnt.append(0)

        for pair in hand_test[crd+1:]:
            if pair[0] == card[0]:
                cnt[-1] += 1
                mtch += 1

        mtch += 1

    print(cnt)