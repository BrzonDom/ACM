"""

Poker Hands

    A poker deck contains 52 cards. Each card has a suit of either clubs (♣), diamonds (♦),
    hearts (♥) or spades (♠), (denoted C, D, H, S in the input data). Each card also has a value
    of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A)

    Ranking of hands:

        1. High card
            Highest value, then next highest and so on

        2. Pair
            Highest value of pair, then highest value of the rest and so on

        3. Two Pair
            Highest value of pair, then other pair value, then the last card

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
                    ["2H", "3D", "3S", "3C", "3D"],
                    # 6.       Straight
                    ["2H", "6D", "4S", "3C", "5D"],
                    # 7.       Flush
                    ["2H", "4H", "KH", "3H", "6H"],
                    # 8.       Straight Flush
                    ["2D", "6D", "4D", "3D", "5D"]]


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

        color_Dct = {'C': [], 'D': [], 'H': [], 'S': []}
        card_Srt = [0, 0, 0, 0, 0]

        cards = {}

        # pairs = set()
        # threes = 0
        # fours = 0
        # rest = []

        sortCard = []
        mtch = 0

        for crd, card in enumerate(hand_test):

            # card_Srt[crd] = card[0]

            if card[0] not in cards:
                cards[card[0]] = 1

            else:
                cards[card[0]] += 1

            color_Dct[card[1]].append(card[0])

        # if pair_Tbl[-1] == 0:
        #     pair_Tbl = pair_Tbl[:-1]

        # card_Srt.sort(reverse=True)

        strght = 0

        # prev = card_Srt[0]
        #
        # for nxt in card_Srt[1:]:
        #     if nxt == prev - 1:
        #         strght += 1
        #         prev = nxt
        #
        #     else:
        #         break

        prev = sorted(cards.keys())[0]

        for nxt in sorted(cards.keys())[1:]:
            if nxt == prev + 1:
                strght += 1
                prev = nxt

            else:
                break

        # pair_Tbl, card_Srt = rank(hand_test)
        if len(max(color_Dct.values(), key=len)) == 5:

            if strght == 4:
                print("\n\tStraight Flush")
                print(f"\t\tCards: {sorted(cards.keys(), reverse=True)}")

            else:
                print("\n\tFlush")
                print(f"\t\tCards: {sorted(cards.keys(), reverse=True)}")

        elif len(cards) == 5:

            if strght == 4:
                print("\n\tStraight")
                print(f"\t\tCards: {sorted(cards.keys(), reverse=True)}")

            else:
                print(f"\n\tHigh Card")
                print(f"\t\tCards: {sorted(cards.keys(), reverse=True)}")

        elif len(cards) == 4:
            print(f"\n\tPair")

            pair = list(cards.keys())[list(cards.values()).index(2)]
            rest = list(cards.keys())
            rest.remove(pair)
            rest.sort(reverse=True)

            print(f"\t\tPair: {pair}")
            print(f"\t\tRest: {rest}")


        elif len(cards) == 3:

            if 3 in cards.values():
                print(f"\n\tThree of a Kind")

                three = list(cards.keys())[list(cards.values()).index(3)]
                rest = list(cards.keys())
                rest.remove(three)
                rest.sort(reverse=True)

                print(f"\t\tThree: {three}")
                print(f"\t\tRest:  {rest}")

            else:
                print("\n\tTwo Pairs")

                ind = list(cards.values()).index(2)

                pairs = [list(cards.keys())[ind]]
                pairs.append(list(cards.keys())[list(cards.values()).index(2, ind+1)])

                rest = list(cards.keys())
                rest.remove(pairs[0])
                rest.remove(pairs[1])

                print(f"\t\tPairs: {pairs}")
                print(f"\t\tRest:  {rest[0]}")

        elif len(cards) == 2:

            if 3 in cards.values():
                print("\n\tFull House")

                pair = list(cards.keys())[list(cards.values()).index(2)]
                three = list(cards.keys())[list(cards.values()).index(3)]

                print(f"\t\tThree: {three}")
                print(f"\t\tPair:  {pair}")

            else:
                print("\n\tFour of a Kind")

                four = list(cards.keys())[list(cards.values()).index(4)]
                rest = list(cards.keys())
                rest.remove(four)

                print(f"\t\tFour: {four}")
                print(f"\t\tRest: {rest[0]}")



        """
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
                print("\n\tPlayer has a Full House")

            # elif pair_Tbl[0] == 1 and pair_Tbl[1] == 1:
            else:
                print("\n\tPlayer has Two Pairs")

        # elif len(pair_Tbl) == 0:
        else:

            if len(max(color_Dct.values(), key=len)) >= 5:

                if strght >= 4:
                    print("\n\tPlayer has a Straight Flush")

                else:
                    print("\n\tPlayer has a Flush")

            elif strght >= 4:
                print("\n\tPlayer has a Straight")

            else:
                print(f"\n\tPlayer has a High Card")
        """

        # print(f"\t{sorted(cards, reverse=True)}")

        # print(f"\t\t\tPair table: {pair_Tbl}")
        # print(f"\t\tHigh Card: {card_Srt[0]}")
        # print(f"\t\t\tSorted cards: {card_Srt}")
        # print(f"\t\t", end="\t")
        # for color in color_Dct:
        #     if color_Dct[color]:
        #         print(f"{sorted(color_Dct[color], reverse=True)} {color}", end="  ")
        print("\n")


"""__Output__"""
"""
Test: ['2H', '4D', 'KS', '3C', '6D']
		[(2, 'H'), (4, 'D'), (13, 'S'), (3, 'C'), (6, 'D')]

	High Card
		Cards: [13, 6, 4, 3, 2]


Test: ['2H', 'KD', '3S', '3C', '5D']
		[(2, 'H'), (13, 'D'), (3, 'S'), (3, 'C'), (5, 'D')]

	Pair
		Pair: 3
		Rest: [13, 5, 2]


Test: ['2H', '2D', 'JS', '3C', '3D']
		[(2, 'H'), (2, 'D'), (11, 'S'), (3, 'C'), (3, 'D')]

	Two Pairs
		Pairs: [2, 3]
		Rest:  11


Test: ['2H', '2D', '2S', '3C', '5D']
		[(2, 'H'), (2, 'D'), (2, 'S'), (3, 'C'), (5, 'D')]

	Three of a Kind
		Three: 2
		Rest:  [5, 3]


Test: ['2H', '2D', '2S', '5C', '5D']
		[(2, 'H'), (2, 'D'), (2, 'S'), (5, 'C'), (5, 'D')]

	Full House
		Three: 2
		Pair:  5


Test: ['2H', '3D', '3S', '3C', '3D']
		[(2, 'H'), (3, 'D'), (3, 'S'), (3, 'C'), (3, 'D')]

	Four of a Kind
		Four: 3
		Rest: 2


Test: ['2H', '6D', '4S', '3C', '5D']
		[(2, 'H'), (6, 'D'), (4, 'S'), (3, 'C'), (5, 'D')]

	Straight
		Cards: [6, 5, 4, 3, 2]


Test: ['2H', '4H', 'KH', '3H', '6H']
		[(2, 'H'), (4, 'H'), (13, 'H'), (3, 'H'), (6, 'H')]

	Flush
		Cards: [13, 6, 4, 3, 2]


Test: ['2D', '6D', '4D', '3D', '5D']
		[(2, 'D'), (6, 'D'), (4, 'D'), (3, 'D'), (5, 'D')]

	Straight Flush
		Cards: [6, 5, 4, 3, 2]



Process finished with exit code 0

"""