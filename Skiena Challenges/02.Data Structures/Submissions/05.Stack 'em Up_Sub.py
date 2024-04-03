"""

Stack 'em Up

    Input:
        The input begins with a single positive integer on a line by itself indicating the number
        of test cases, followed by a blank line. There is also a blank line between two consecutive
        inputs.
        Each case consists of an integer n ≤ 100, the number of shuffles that the dealer knows.
        Then follow n sets of 52 integers, each comprising all the integers from 1 to 52 in some
        order. Within each set of 52 integers, i in position j means that the shuffle moves the
        ith card in the deck to position j.
        Several lines follow, each containing an integer k between 1 and n. These indicate
        that you have observed the dealer applying the kth shuffle given in the input

    Output:
        For each test case, assume the dealer starts with a new deck ordered as described above.
        After all the shuffles had been performed, give the names of the cards in the deck, in
        the new order. The output of two consecutive cases will be separated by a blank line.


    Sample:

        1

        2
        2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
        27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51
        52 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
        27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 1
        1
        2
            =>  King of Spades
                2 of Clubs
                4 of Clubs
                5 of Clubs
                6 of Clubs
                7 of Clubs
                8 of Clubs
                9 of Clubs
                10 of Clubs
                Jack of Clubs
                Queen of Clubs
                King of Clubs
                Ace of Clubs
                2 of Diamonds
                3 of Diamonds
                4 of Diamonds
                5 of Diamonds
                6 of Diamonds
                7 of Diamonds
                8 of Diamonds
                9 of Diamonds
                10 of Diamonds
                Jack of Diamonds
                Queen of Diamonds
                King of Diamonds
                Ace of Diamonds
                2 of Hearts
                3 of Hearts
                4 of Hearts
                5 of Hearts
                6 of Hearts
                7 of Hearts
                8 of Hearts
                9 of Hearts
                10 of Hearts
                Jack of Hearts
                Queen of Hearts
                King of Hearts
                Ace of Hearts
                2 of Spades
                3 of Spades
                4 of Spades
                5 of Spades
                6 of Spades
                7 of Spades
                8 of Spades
                9 of Spades
                10 of Spades
                Jack of Spades
                Queen of Spades
                Ace of Spades
                3 of Clubs

"""
import copy
from sys import stdin

caseNum = int(stdin.readline())
skipLine = stdin.readline()

for case in range(caseNum):

    # print(f"\t{case+1}.Case:\n")

    shfflNum = int(stdin.readline())

    shfflAll = []

    while len(shfflAll) < shfflNum * 52:
        shfflAll += list(map(int, stdin.readline().split()))

    # print(f"\t\tNum. of shuffles: {shfflNum}\n")

    shfflLst = []

    for s in range(shfflNum):
        shfflLst.append(shfflAll[s * 52: (s + 1) * 52])

    # shfflLst = [[] for _ in range(shfflNum)]

    # for shffl in range(shfflNum):
    #     shfflLst[shffl] = list(map(int, stdin.readline().split()))
    #     shfflLst[shffl] += list(map(int, stdin.readline().split()))
    #     print(f"\t\t\t{shffl+1}.:\t{shfflLst[shffl]}")

    # print()

    moveLst = []

    moveLine = stdin.readline()

    while moveLine != '\n' and moveLine != '':

        moveLst.append(int(moveLine))

        moveLine = stdin.readline()

    # print(f"\t\tUsed shuffles: {moveLst}\n")

    prev_Cards = [
        "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs",
        "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",

        "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds",
        "8 of Diamonds",
        "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
        "Ace of Diamonds",

        "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts",
        "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",

        "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades",
        "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades"
    ]

    next_Cards = copy.deepcopy(prev_Cards)

    for move in moveLst:

        for to, frm in enumerate(shfflLst[move - 1]):

            next_Cards[to] = prev_Cards[frm-1]

        prev_Cards = copy.deepcopy(next_Cards)

    # print(f"\t\tShuffled cards:\n")

    for c, card in enumerate(next_Cards):

        # print("\t\t\t", card)
        print(card)

    if case + 1 < caseNum:
        print("")

    # print("\n")


quit()

InputRaw_Str = """
2

2
2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51
52 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 1
1
2

1
2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51
1
"""


InputStr_Lst = InputRaw_Str[1:].split("\n")
print(InputStr_Lst)
print()

caseNum = int(InputStr_Lst.pop(0))

print(f"Num. of cases: {caseNum}\n")

for case in range(caseNum):
    print(f"\t{case+1}.Case:\n")

    shfflNum = int(InputStr_Lst[1])
    InputStr_Lst = InputStr_Lst[2:]

    print(f"\t\tNum. of shuffles: {shfflNum}\n")

    shfflLst = [[] for _ in range(shfflNum)]

    # print(InputStr_Lst.pop(0) + '\n' + InputStr_Lst.pop(0))

    for shffl in range(shfflNum):
        shfflLst[shffl] = list(map(int, InputStr_Lst.pop(0).split()))
        shfflLst[shffl] += list(map(int, InputStr_Lst.pop(0).split()))
        print(f"\t\t\t{shffl+1}.:\t{shfflLst[shffl]}")
    print()

    moveLst = []

    while InputStr_Lst[0] != '':
        moveLst.append(int(InputStr_Lst.pop(0)))

    print(f"\t\tUsed shuffles: {moveLst}\n")

    prev_Cards = [
        "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs",
        "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",

        "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds",
        "8 of Diamonds",
        "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
        "Ace of Diamonds",

        "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts",
        "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",

        "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades",
        "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades"
    ]

    next_Cards = copy.deepcopy(prev_Cards)

    for move in moveLst:

        for to, frm in enumerate(shfflLst[move - 1]):

            next_Cards[to] = prev_Cards[frm-1]

        prev_Cards = copy.deepcopy(next_Cards)

    # print(f"\t\tShuffled cards:", end="\n\n\t\t\t")
    print(f"\t\tShuffled cards:\n")

    for c, card in enumerate(next_Cards):

        print("\t\t\t", card)

    print("\n")