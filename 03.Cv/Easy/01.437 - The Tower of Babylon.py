"""
437 - The Tower of Babylon
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=6&page=show_problem&problem=378

        Perhaps you have heard of the legend of the Tower of Babylon. Nowadays many details of this tale
    have been forgotten. So now, in line with the educational nature of this contest, we will tell you the
    whole story:

            The babylonians had n types of blocks, and an unlimited supply of blocks of each type.
        Each type-i block was a rectangular solid with linear dimensions (x_i, y_i, z_i). A block could
        be reoriented so that any two of its three dimensions determined the dimensions of the base
        and the other dimension was the height.
            They wanted to construct the tallest tower possible by stacking blocks. The problem was
        that, in building a tower, one block could only be placed on top of another block as long as
        the two base dimensions of the upper block were both strictly smaller than the corresponding
        base dimensions of the lower block. This meant, for example, that blocks oriented to have
        equal-sized bases couldn’t be stacked.

        Your job is to write a program that determines the height of the tallest tower the babylonians can
    build with a given set of blocks.

    Input:
            The input file will contain one or more test cases. The first line of each test case contains an integer n,
        representing the number of different blocks in the following data set. The maximum value for n is 30.
        Each of the next n lines contains three integers representing the values x_i, y_i and z_i.
        Input is terminated by a value of zero (0) for n.

    Output:
            For each test case, print one line containing the case number (they are numbered sequentially starting
        from 1) and the height of the tallest possible tower in the format
        "Case case: maximum height = height"


    Sample:
        1
        10 20 30
        2
        6 8 10
        5 5 5
        7
        1 1 1
        2 2 2
        3 3 3
        4 4 4
        5 5 5
        6 6 6
        7 7 7
        5
        31 41 59
        26 53 58
        97 93 23
        84 62 64
        33 83 27
        0
            =>  Case 1: maximum height = 40
                Case 2: maximum height = 21
                Case 3: maximum height = 28
                Case 4: maximum height = 342

"""
from itertools import permutations

class Tower:
    def __init__(self, bld, sds, hgh):
        self.bld = bld
        self.sds = sds
        self.hgh = hgh


def buildTower(Twr):

    for sd in Twr.sds:

        nxtBld = Twr.bld + [sd]
        nxtSds = posSides[str(sd)]
        nxtHgh = Twr.hgh + sd[2]

        nxtTwr = Tower(nxtBld, nxtSds, nxtHgh)

        if nxtSds:
            buildTower(nxtTwr)

        else:
            print(f"\t\tTower:  {nxtBld}")
            print(f"\t\tHeight: {nxtHgh}")
            print()

            return nxtTwr


InputRaw_Str = """
1
10 20 30
2
6 8 10
5 5 5
7
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
5
31 41 59
26 53 58
97 93 23
84 62 64
33 83 27
0
"""

InputRaw_Str = InputRaw_Str[1:-1]

if __name__ == '__main__':

    print("Input:")
    print(InputRaw_Str)
    print()

    InputLines = InputRaw_Str.split("\n")

    blckNum = int(InputLines.pop(0))
    caseCnt = 1

    while blckNum > 0:

        print(f"\tCase: {caseCnt}")
        print()

        Blocks = []
        Sides = []

        for b in range(blckNum):

            blck = list(map(int, InputLines.pop(0).split()))
            Blocks.append(blck)

            print(f"\t\t{b+1}. {blck}")

            curSides = list(set(permutations(blck, 3)))
            Sides += curSides

            # for side in Sides[str(blck)]:
            #     # print(f"\t\t\t{b+1}. {side}")
            #     print(f"\t\t\t\tSurface: {side[0]} * {side[1]} = {side[0] * side[1]}")
            #     print(f"\t\t\t\tHeight:  {side[2]}")
            #     print()

        print()

        caseCnt += 1
        blckNum = int(InputLines.pop(0))

        print(f"\t\tSides:\n\t\t\t", end="")
        for s, sd in enumerate(Sides):
            print(sd, end=" ")

            if (s+1) % 5 == 0 and (s+1) != len(Sides):
                print("\n\t\t\t", end="")
        print("\n")

        posSides = {}

        for sd in Sides:
            print(f"\t\t\tSide: {sd}")
            # print(f"\t\t\tPossible sides:")
            # print()

            posSides[str(sd)] = []

            for nxtSd in Sides:
                if nxtSd[0] < sd[0] and nxtSd[1] < sd[1]:
                    # print(f"\t\t\t{nxtSd}")

                    posSides[str(sd)] += [nxtSd]
            # print()

            # for posSd in posSides:
            #     nxtTwr = Tower([sd, posSd], posSides, sd[2] + posSd[2])
            #
            #     print(f"\t\t\tTower:  {nxtTwr.bld}")
            #     print(f"\t\t\tHeight: {nxtTwr.hgh}")
            #     print(f"\t\t\tSides:  {nxtTwr.sds}")
            #     print()

            # print(f"\t\t\tPossible sides:\n\t\t\t\t", end="")

            if posSides[str(sd)]:
                print("\t\t\t\t", end="")
                for s, psSd in enumerate(posSides[str(sd)]):
                    print(psSd, end=" ")

                    if (s+1) % 5 == 0 and (s+1) != len(posSides[str(sd)]):
                        print("\n\t\t\t\t", end="")
                print("\n")
            else:
                print()

        print("\n")

        for sd in Sides:

            Twr = Tower([sd], posSides[str(sd)], sd[2])
            buildTower(Twr)


        if blckNum != 0:
            print()


"""__Output__"""
"""
Input:
1
10 20 30
2
6 8 10
5 5 5
7
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
5
31 41 59
26 53 58
97 93 23
84 62 64
33 83 27
0

	Case: 1

		1. [10, 20, 30]

		Sides:
			(10, 30, 20) (20, 30, 10) (20, 10, 30) (10, 20, 30) (30, 10, 20) 
			(30, 20, 10) 

			Side: (10, 30, 20)

			Side: (20, 30, 10)
				(10, 20, 30) 

			Side: (20, 10, 30)

			Side: (10, 20, 30)

			Side: (30, 10, 20)

			Side: (30, 20, 10)
				(20, 10, 30) 



		Tower:  [(20, 30, 10), (10, 20, 30)]
		Height: 40

		Tower:  [(30, 20, 10), (20, 10, 30)]
		Height: 40


	Case: 2

		1. [6, 8, 10]
		2. [5, 5, 5]

		Sides:
			(6, 8, 10) (10, 6, 8) (8, 6, 10) (10, 8, 6) (6, 10, 8) 
			(8, 10, 6) (5, 5, 5) 

			Side: (6, 8, 10)
				(5, 5, 5) 

			Side: (10, 6, 8)
				(5, 5, 5) 

			Side: (8, 6, 10)
				(5, 5, 5) 

			Side: (10, 8, 6)
				(8, 6, 10) (5, 5, 5) 

			Side: (6, 10, 8)
				(5, 5, 5) 

			Side: (8, 10, 6)
				(6, 8, 10) (5, 5, 5) 

			Side: (5, 5, 5)



		Tower:  [(6, 8, 10), (5, 5, 5)]
		Height: 15

		Tower:  [(10, 6, 8), (5, 5, 5)]
		Height: 13

		Tower:  [(8, 6, 10), (5, 5, 5)]
		Height: 15

		Tower:  [(10, 8, 6), (8, 6, 10), (5, 5, 5)]
		Height: 21

		Tower:  [(10, 8, 6), (5, 5, 5)]
		Height: 11

		Tower:  [(6, 10, 8), (5, 5, 5)]
		Height: 13

		Tower:  [(8, 10, 6), (6, 8, 10), (5, 5, 5)]
		Height: 21

		Tower:  [(8, 10, 6), (5, 5, 5)]
		Height: 11


	Case: 3

		1. [1, 1, 1]
		2. [2, 2, 2]
		3. [3, 3, 3]
		4. [4, 4, 4]
		5. [5, 5, 5]
		6. [6, 6, 6]
		7. [7, 7, 7]

		Sides:
			(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) (5, 5, 5) 
			(6, 6, 6) (7, 7, 7) 

			Side: (1, 1, 1)

			Side: (2, 2, 2)
				(1, 1, 1) 

			Side: (3, 3, 3)
				(1, 1, 1) (2, 2, 2) 

			Side: (4, 4, 4)
				(1, 1, 1) (2, 2, 2) (3, 3, 3) 

			Side: (5, 5, 5)
				(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) 

			Side: (6, 6, 6)
				(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) (5, 5, 5) 

			Side: (7, 7, 7)
				(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) (5, 5, 5) 
				(6, 6, 6) 



		Tower:  [(2, 2, 2), (1, 1, 1)]
		Height: 3

		Tower:  [(3, 3, 3), (1, 1, 1)]
		Height: 4

		Tower:  [(4, 4, 4), (1, 1, 1)]
		Height: 5

		Tower:  [(5, 5, 5), (1, 1, 1)]
		Height: 6

		Tower:  [(6, 6, 6), (1, 1, 1)]
		Height: 7

		Tower:  [(7, 7, 7), (1, 1, 1)]
		Height: 8


	Case: 4

		1. [31, 41, 59]
		2. [26, 53, 58]
		3. [97, 93, 23]
		4. [84, 62, 64]
		5. [33, 83, 27]

		Sides:
			(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
			(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
			(26, 58, 53) (53, 26, 58) (93, 23, 97) (93, 97, 23) (97, 93, 23) 
			(23, 93, 97) (97, 23, 93) (23, 97, 93) (84, 64, 62) (64, 62, 84) 
			(62, 84, 64) (62, 64, 84) (64, 84, 62) (84, 62, 64) (83, 27, 33) 
			(83, 33, 27) (33, 27, 83) (33, 83, 27) (27, 83, 33) (27, 33, 83) 

			Side: (31, 59, 41)
				(26, 53, 58) (26, 58, 53) (27, 33, 83) 

			Side: (59, 31, 41)
				(58, 26, 53) (53, 26, 58) (33, 27, 83) 

			Side: (59, 41, 31)
				(41, 31, 59) (58, 26, 53) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (41, 59, 31)
				(31, 41, 59) (26, 53, 58) (26, 58, 53) (33, 27, 83) (27, 33, 83) 

			Side: (31, 41, 59)
				(27, 33, 83) 

			Side: (41, 31, 59)
				(33, 27, 83) 

			Side: (58, 26, 53)

			Side: (58, 53, 26)
				(31, 41, 59) (41, 31, 59) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (26, 53, 58)

			Side: (53, 58, 26)
				(31, 41, 59) (41, 31, 59) (26, 53, 58) (33, 27, 83) (27, 33, 83) 

			Side: (26, 58, 53)

			Side: (53, 26, 58)

			Side: (93, 23, 97)

			Side: (93, 97, 23)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (23, 93, 97) (84, 64, 62) (64, 62, 84) 
				(62, 84, 64) (62, 64, 84) (64, 84, 62) (84, 62, 64) (83, 27, 33) 
				(83, 33, 27) (33, 27, 83) (33, 83, 27) (27, 83, 33) (27, 33, 83) 

			Side: (97, 93, 23)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (93, 23, 97) (84, 64, 62) (64, 62, 84) 
				(62, 84, 64) (62, 64, 84) (64, 84, 62) (84, 62, 64) (83, 27, 33) 
				(83, 33, 27) (33, 27, 83) (33, 83, 27) (27, 83, 33) (27, 33, 83) 

			Side: (23, 93, 97)

			Side: (97, 23, 93)

			Side: (23, 97, 93)

			Side: (84, 64, 62)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (64, 62, 84) (83, 27, 33) (83, 33, 27) 
				(33, 27, 83) (27, 33, 83) 

			Side: (64, 62, 84)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (62, 84, 64)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (33, 27, 83) (33, 83, 27) (27, 83, 33) 
				(27, 33, 83) 

			Side: (62, 64, 84)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (64, 84, 62)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (62, 64, 84) (33, 27, 83) (33, 83, 27) 
				(27, 83, 33) (27, 33, 83) 

			Side: (84, 62, 64)
				(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
				(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
				(26, 58, 53) (53, 26, 58) (83, 27, 33) (83, 33, 27) (33, 27, 83) 
				(27, 33, 83) 

			Side: (83, 27, 33)
				(58, 26, 53) (53, 26, 58) 

			Side: (83, 33, 27)
				(59, 31, 41) (41, 31, 59) (58, 26, 53) (53, 26, 58) (33, 27, 83) 

			Side: (33, 27, 83)

			Side: (33, 83, 27)
				(31, 59, 41) (31, 41, 59) (26, 53, 58) (26, 58, 53) (27, 33, 83) 

			Side: (27, 83, 33)
				(26, 53, 58) (26, 58, 53) 

			Side: (27, 33, 83)



		Tower:  [(31, 59, 41), (26, 53, 58)]
		Height: 99

		Tower:  [(59, 31, 41), (58, 26, 53)]
		Height: 94

		Tower:  [(59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 173

		Tower:  [(59, 41, 31), (58, 26, 53)]
		Height: 84

		Tower:  [(41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 173

		Tower:  [(41, 59, 31), (26, 53, 58)]
		Height: 89

		Tower:  [(31, 41, 59), (27, 33, 83)]
		Height: 142

		Tower:  [(41, 31, 59), (33, 27, 83)]
		Height: 142

		Tower:  [(58, 53, 26), (31, 41, 59), (27, 33, 83)]
		Height: 168

		Tower:  [(58, 53, 26), (41, 31, 59), (33, 27, 83)]
		Height: 168

		Tower:  [(58, 53, 26), (53, 26, 58)]
		Height: 84

		Tower:  [(53, 58, 26), (31, 41, 59), (27, 33, 83)]
		Height: 168

		Tower:  [(53, 58, 26), (41, 31, 59), (33, 27, 83)]
		Height: 168

		Tower:  [(53, 58, 26), (26, 53, 58)]
		Height: 84

		Tower:  [(93, 97, 23), (31, 59, 41), (26, 53, 58)]
		Height: 122

		Tower:  [(93, 97, 23), (59, 31, 41), (58, 26, 53)]
		Height: 117

		Tower:  [(93, 97, 23), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 196

		Tower:  [(93, 97, 23), (59, 41, 31), (58, 26, 53)]
		Height: 107

		Tower:  [(93, 97, 23), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 196

		Tower:  [(93, 97, 23), (41, 59, 31), (26, 53, 58)]
		Height: 112

		Tower:  [(93, 97, 23), (31, 41, 59), (27, 33, 83)]
		Height: 165

		Tower:  [(93, 97, 23), (41, 31, 59), (33, 27, 83)]
		Height: 165

		Tower:  [(93, 97, 23), (58, 26, 53)]
		Height: 76

		Tower:  [(97, 93, 23), (31, 59, 41), (26, 53, 58)]
		Height: 122

		Tower:  [(97, 93, 23), (59, 31, 41), (58, 26, 53)]
		Height: 117

		Tower:  [(97, 93, 23), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 196

		Tower:  [(97, 93, 23), (59, 41, 31), (58, 26, 53)]
		Height: 107

		Tower:  [(97, 93, 23), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 196

		Tower:  [(97, 93, 23), (41, 59, 31), (26, 53, 58)]
		Height: 112

		Tower:  [(97, 93, 23), (31, 41, 59), (27, 33, 83)]
		Height: 165

		Tower:  [(97, 93, 23), (41, 31, 59), (33, 27, 83)]
		Height: 165

		Tower:  [(97, 93, 23), (58, 26, 53)]
		Height: 76

		Tower:  [(84, 64, 62), (31, 59, 41), (26, 53, 58)]
		Height: 161

		Tower:  [(84, 64, 62), (59, 31, 41), (58, 26, 53)]
		Height: 156

		Tower:  [(84, 64, 62), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 235

		Tower:  [(84, 64, 62), (59, 41, 31), (58, 26, 53)]
		Height: 146

		Tower:  [(84, 64, 62), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 235

		Tower:  [(84, 64, 62), (41, 59, 31), (26, 53, 58)]
		Height: 151

		Tower:  [(84, 64, 62), (31, 41, 59), (27, 33, 83)]
		Height: 204

		Tower:  [(84, 64, 62), (41, 31, 59), (33, 27, 83)]
		Height: 204

		Tower:  [(84, 64, 62), (58, 26, 53)]
		Height: 115

		Tower:  [(64, 62, 84), (31, 59, 41), (26, 53, 58)]
		Height: 183

		Tower:  [(64, 62, 84), (59, 31, 41), (58, 26, 53)]
		Height: 178

		Tower:  [(64, 62, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 257

		Tower:  [(64, 62, 84), (59, 41, 31), (58, 26, 53)]
		Height: 168

		Tower:  [(64, 62, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 257

		Tower:  [(64, 62, 84), (41, 59, 31), (26, 53, 58)]
		Height: 173

		Tower:  [(64, 62, 84), (31, 41, 59), (27, 33, 83)]
		Height: 226

		Tower:  [(64, 62, 84), (41, 31, 59), (33, 27, 83)]
		Height: 226

		Tower:  [(64, 62, 84), (58, 26, 53)]
		Height: 137

		Tower:  [(62, 84, 64), (31, 59, 41), (26, 53, 58)]
		Height: 163

		Tower:  [(62, 84, 64), (59, 31, 41), (58, 26, 53)]
		Height: 158

		Tower:  [(62, 84, 64), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 237

		Tower:  [(62, 84, 64), (59, 41, 31), (58, 26, 53)]
		Height: 148

		Tower:  [(62, 84, 64), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 237

		Tower:  [(62, 84, 64), (41, 59, 31), (26, 53, 58)]
		Height: 153

		Tower:  [(62, 84, 64), (31, 41, 59), (27, 33, 83)]
		Height: 206

		Tower:  [(62, 84, 64), (41, 31, 59), (33, 27, 83)]
		Height: 206

		Tower:  [(62, 84, 64), (58, 26, 53)]
		Height: 117

		Tower:  [(62, 64, 84), (31, 59, 41), (26, 53, 58)]
		Height: 183

		Tower:  [(62, 64, 84), (59, 31, 41), (58, 26, 53)]
		Height: 178

		Tower:  [(62, 64, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 257

		Tower:  [(62, 64, 84), (59, 41, 31), (58, 26, 53)]
		Height: 168

		Tower:  [(62, 64, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 257

		Tower:  [(62, 64, 84), (41, 59, 31), (26, 53, 58)]
		Height: 173

		Tower:  [(62, 64, 84), (31, 41, 59), (27, 33, 83)]
		Height: 226

		Tower:  [(62, 64, 84), (41, 31, 59), (33, 27, 83)]
		Height: 226

		Tower:  [(62, 64, 84), (58, 26, 53)]
		Height: 137

		Tower:  [(64, 84, 62), (31, 59, 41), (26, 53, 58)]
		Height: 161

		Tower:  [(64, 84, 62), (59, 31, 41), (58, 26, 53)]
		Height: 156

		Tower:  [(64, 84, 62), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 235

		Tower:  [(64, 84, 62), (59, 41, 31), (58, 26, 53)]
		Height: 146

		Tower:  [(64, 84, 62), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 235

		Tower:  [(64, 84, 62), (41, 59, 31), (26, 53, 58)]
		Height: 151

		Tower:  [(64, 84, 62), (31, 41, 59), (27, 33, 83)]
		Height: 204

		Tower:  [(64, 84, 62), (41, 31, 59), (33, 27, 83)]
		Height: 204

		Tower:  [(64, 84, 62), (58, 26, 53)]
		Height: 115

		Tower:  [(84, 62, 64), (31, 59, 41), (26, 53, 58)]
		Height: 163

		Tower:  [(84, 62, 64), (59, 31, 41), (58, 26, 53)]
		Height: 158

		Tower:  [(84, 62, 64), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
		Height: 237

		Tower:  [(84, 62, 64), (59, 41, 31), (58, 26, 53)]
		Height: 148

		Tower:  [(84, 62, 64), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
		Height: 237

		Tower:  [(84, 62, 64), (41, 59, 31), (26, 53, 58)]
		Height: 153

		Tower:  [(84, 62, 64), (31, 41, 59), (27, 33, 83)]
		Height: 206

		Tower:  [(84, 62, 64), (41, 31, 59), (33, 27, 83)]
		Height: 206

		Tower:  [(84, 62, 64), (58, 26, 53)]
		Height: 117

		Tower:  [(83, 27, 33), (58, 26, 53)]
		Height: 86

		Tower:  [(83, 33, 27), (59, 31, 41), (58, 26, 53)]
		Height: 121

		Tower:  [(83, 33, 27), (41, 31, 59), (33, 27, 83)]
		Height: 169

		Tower:  [(83, 33, 27), (58, 26, 53)]
		Height: 80

		Tower:  [(33, 83, 27), (31, 59, 41), (26, 53, 58)]
		Height: 126

		Tower:  [(33, 83, 27), (31, 41, 59), (27, 33, 83)]
		Height: 169

		Tower:  [(33, 83, 27), (26, 53, 58)]
		Height: 85

		Tower:  [(27, 83, 33), (26, 53, 58)]
		Height: 91


Process finished with exit code 0

"""
