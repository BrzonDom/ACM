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

cardsPrnt = {
    '2' : '2 ',
    '3' : '3 ',
    '4' : '4 ',
    '5' : '5 ',
    '6' : '6 ',
    '7' : '7 ',
    '8' : '8 ',
    '9' : '9 ',
    '0' : '10 ',
    'J' : 'Jack ',
    'Q' : 'Queen ',
    'K' : 'King ',
    'A' : 'Ace ',
    'C' : 'of Clubs',
    'D' : 'of Diamonds',
    'H' : 'of Hearts',
    'S' : 'of Spades'
}

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

    shfflAll = []

    while len(shfflAll) < shfflNum * 52:
        shfflAll += list(map(int, InputStr_Lst.pop(0).split()))

    # shfflLst = [[] for _ in range(shfflNum)]

    shfflLst = []

    for s in range(shfflNum):
        shfflLst.append(shfflAll[s * 52: (s+1) * 52])
        print(f"\t\t\t{s + 1}.:\t{shfflLst[s]}")

    # for shffl in range(shfflNum):
    #     shfflLst[shffl] = list(map(int, InputStr_Lst.pop(0).split()))
    #     shfflLst[shffl] += list(map(int, InputStr_Lst.pop(0).split()))
    #     print(f"\t\t\t{shffl+1}.:\t{shfflLst[shffl]}")
    print()

    moveLst = []

    while InputStr_Lst[0] != '':
        moveLst.append(int(InputStr_Lst.pop(0)))

    print(f"\t\tUsed shuffles: {moveLst}\n")

    prev_Cards = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC', 'AC',
                  '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD', 'AD',
                  '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH', 'AH',
                  '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS', 'AS']

    next_Cards = copy.deepcopy(prev_Cards)

    for move in moveLst:

        for to, frm in enumerate(shfflLst[move - 1]):

            next_Cards[to] = prev_Cards[frm-1]

        prev_Cards = copy.deepcopy(next_Cards)

    print(f"\t\tShuffled cards:", end="\n\n\t\t\t")

    for c, card in enumerate(next_Cards):

        if (c+1) % 13 == 0:
            print(card, end="\n\t\t\t")

        else:
            print(card, end=" ")
    print()

    for card in next_Cards:
        print(f"\t\t\t{cardsPrnt[card[0]]}{cardsPrnt[card[1]]}")
        # print(f"\t\t{card}")

    print("\n")

# print(InputStr_Lst)

"""
Input = list(map(int, InputRaw_Str.split()))
print("Input string: ", end="\n\"\"\"")
print(InputRaw_Str, end="\"\"\"\n\n")
print(f"Input: {Input}\n")

Cases = [[] for _ in range(Input[0])]
Input = Input[1:]

ShfflCnt = Input[0]
Input = Input[1:]

Shffls = [[] for _ in range(ShfflCnt)]

for c in range(ShfflCnt):

    Shffls[c] = Input[c*52: 52 + c*52]

Moves = Input[ShfflCnt * 52:]

print("Moves:")

for m in Moves:
    print(f"\t{m:2}: {Shffls[m-1]}")

print("\n")

Prev_Cards = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
              '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
              '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
              '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']

Next_Cards = copy.deepcopy(Prev_Cards)

for m in Moves:

    for p, n in enumerate(Shffls[m-1]):

        Next_Cards[p] = Prev_Cards[n-1]

    Prev_Cards = copy.deepcopy(Next_Cards)

print("Shuffled cards:", end="\n\t")

for c, card in enumerate(Next_Cards):
    if (c+1) % 13 == 0:
        print(f"{card}\n", end="\t")

    else:
        print(card, end=", ")

print("\n\n")

Positions = {
     1 :  1,
     2 :  2,
     3 :  3,
     4 :  4,
     5 :  5,
     6 :  6,
     7 :  7,
     8 :  8,
     9 :  9,
    10 : 10,
    11 : 11,
    12 : 12,
    13 : 13,
    14 : 14,
    15 : 15,
    16 : 16,
    17 : 17,
    18 : 18,
    19 : 19,
    20 : 20,
    21 : 21,
    22 : 22,
    23 : 23,
    24 : 24,
    25 : 25,
    26 : 26,
    27 : 27,
    28 : 28,
    29 : 29,
    30 : 30,
    31 : 31,
    32 : 32,
    33 : 33,
    34 : 34,
    35 : 35,
    36 : 36,
    37 : 37,
    38 : 38,
    39 : 39,
    40 : 40,
    41 : 41,
    42 : 42,
    43 : 43,
    44 : 44,
    45 : 45,
    46 : 46,
    47 : 47,
    48 : 48,
    49 : 49,
    50 : 50,
    51 : 51,
    52 : 52
}

Org_Cards = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
             '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
             '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
             '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']


# Positions = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13,
#              14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
#              27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
#              40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

# print()
# for pos in range(1, 53):
#     Positions[pos] = pos
#     print(f"{pos:2} : {pos:>2},")

# print(Positions)

for m in Moves:

    for pos in Positions:

        prvPos = Positions[pos] - 1
        nxtPos = Shffls[m-1][prvPos]

        Positions[pos] = nxtPos

print(Positions)
# """

"""__Output__"""
"""
['2', '', '2', '2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26', '27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51', '52 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26', '27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 1', '1', '2', '', '1', '2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26', '27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 52 51', '1', '']

Num. of cases: 2

	1.Case:

		Num. of shuffles: 2

			1.:	[2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 51]
			2.:	[52, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 1]

		Used shuffles: [1, 2]

		Shuffled cards:

			KS 2C 4C 5C 6C 7C 8C 9C 0C JC QC KC AC
			2D 3D 4D 5D 6D 7D 8D 9D 0D JD QD KD AD
			2H 3H 4H 5H 6H 7H 8H 9H 0H JH QH KH AH
			2S 3S 4S 5S 6S 7S 8S 9S 0S JS QS AS 3C
			
			King of Spades
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


	2.Case:

		Num. of shuffles: 1

			1.:	[2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 51]

		Used shuffles: [1]

		Shuffled cards:

			3C 2C 4C 5C 6C 7C 8C 9C 0C JC QC KC AC
			2D 3D 4D 5D 6D 7D 8D 9D 0D JD QD KD AD
			2H 3H 4H 5H 6H 7H 8H 9H 0H JH QH KH AH
			2S 3S 4S 5S 6S 7S 8S 9S 0S JS QS AS KS
			
			3 of Clubs
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
			King of Spades



Process finished with exit code 0

"""