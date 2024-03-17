"""

Poker Hands

    A poker deck contains 52 cards. Each card has a suit of either clubs (♣), diamonds (♦),
    hearts (♥) or spades (♠), (denoted C, D, H, S in the input data). Each card also has a value
    of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A)

    Ranking of hands:

        1. High card
            Highest value, then next highest and so on

        2. Pair
            Highest value of pair, then sum of the rest

        3. Two Pair
            Highest value of pair, then other pair value, then the last

        4. Three of a Kind
            Highest value of three

        5. Straight
            Highest card  of a straight

        6. Flush
            Highest value of flush, then next highest value of flush and so on till end of flush

        7. Full House
            Highest value of three

        8. Four of a Kind
            Highest card of four

        9. Straight Flush
            Highest card in hand


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

def modify(strHand):

    hand = []

    for card in strHand:
        hand.append((cardDict[card[0]], card[1]))

    return hand


def rank(hand):
    pair_Tbl = [0]

    color_Dct = {'C': 0, 'D': 0, 'H': 0, 'S': 0}
    card_Srt = [0, 0, 0, 0, 0]

    sortCard = []
    mtch = 0

    for crd, card in enumerate(hand):

        card_Srt[crd] = card[0]

        color_Dct[card[1]] += 1

        if mtch > crd:
            continue

        if pair_Tbl[-1]:
            pair_Tbl.append(0)

        for pair in hand[crd + 1:]:
            if pair[0] == card[0]:
                pair_Tbl[-1] += 1
                mtch += 1

        mtch += 1

    if pair_Tbl[-1] == 0:
        pair_Tbl = pair_Tbl[:-1]

    card_Srt.sort(reverse=True)

    return pair_Tbl, card_Srt


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

    tstHands_Lst = [
                    # 0.       High card
                    ["2H", "4D", "KS", "3C", "6D"],
                    # 1.       Pair
                    ["2H", "KD", "3S", "3C", "5D"],
                    # 2.       Two Pair
                    ["2H", "2D", "JS", "3C", "3D"],
                    # 3.       Three of a Kind
                    ["2H", "2D", "2S", "3C", "5D"],
                    # 4.       Full House
                    ["2H", "2D", "2S", "5C", "5D"],
                    # 5.       Four of a Kind
                    ["2H", "3D", "3S", "3C", "5D"],
                    # 6.       Straight
                    ["2H", "6D", "4S", "3C", "5D"],
                    # 7.       Flush
                    ["2H", "4H", "KH", "3H", "6H"]]


    # strHand_test = tstHands_Lst[0]
    # strHand_test = ["2H", "2D", "2S", "5C", "5D"]


    """
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
    """

    for strHand_test in tstHands_Lst:

        # print("Test: ", end="")
        # hand = []
        #
        # for card in strHand_test:
        #     print(card, end=" ")
        #
        #     hand.append((cardDict[card[0]], card[1]))

        print(f"Test: {strHand_test}")

        hand_test = modify(strHand_test)

        print(f"\t\t{hand_test}")

        pair_Tbl = [0]

        color_Dct = {'C': 0, 'D': 0, 'H': 0, 'S': 0}
        card_Srt = [0, 0, 0, 0, 0]

        sortCard = []
        mtch = 0



        for crd, card in enumerate(hand_test):

            card_Srt[crd] = card[0]

            color_Dct[card[1]] += 1

            if mtch > crd:
                continue

            # for s, srt in enumerate(card_Srt):
            #     if card[0] > srt:
            #         str = card[0]

            if pair_Tbl[-1]:
                pair_Tbl.append(0)

            for pair in hand_test[crd+1:]:
                if pair[0] == card[0]:

                    pair_Tbl[-1] += 1
                    mtch += 1

                # else:
                #     if pair[0] == card[0] + 1 and up:
                #         flsh += 1
                #         down = False
                #
                #     elif pair[0] == card[0] - 1 and down:
                #         flsh += 1
                #         up = False
                #
                #     else:
                #         flsh = 0

            mtch += 1

        if pair_Tbl[-1] == 0:
            pair_Tbl = pair_Tbl[:-1]

        card_Srt.sort(reverse=True)

        flsh = 0

        prev = card_Srt[0]

        for nxt in card_Srt[1:]:
            if nxt == prev - 1:
                flsh += 1
                prev = nxt

            else:
                break

        # pair_Tbl, card_Srt = rank(hand_test)

        if len(pair_Tbl) == 1:
            if pair_Tbl[0] == 2:
               print(f"\n\tPlayer has Three of a Kind")

            # elif pair_Tbl[0] == 1:
            else:
                print(f"\n\tPlayer has a Pair")


            # else:
            #     print(f"\n\tPlayer has a High Card")


        elif len(pair_Tbl) == 2:
            if 1 in pair_Tbl and 2 in pair_Tbl:
                print("\n\tPlayer has a FUll House")

            # elif pair_Tbl[0] == 1 and pair_Tbl[1] == 1:
            else:
                print("\n\tPlayer has Two Pairs")

        # elif len(pair_Tbl) == 0:
        else:

            if max(color_Dct.values()) >= 5:
                print("\n\tPlayer has a Flush")

            elif flsh >= 4:
                print("\n\tPlayer has a Straight")

            else:
                print(f"\n\tPlayer has a High Card")

        print(f"\t\t\tPair table: {pair_Tbl}")
        print(f"\t\tHigh Card: {card_Srt[0]}")
        print(f"\t\t\tSorted cards: {card_Srt}")
        print(f"\t\t", end="\t")
        for color in color_Dct:
            if color_Dct[color]:
                print(f"{color_Dct[color]}{color}", end="  ")
        print("\n")