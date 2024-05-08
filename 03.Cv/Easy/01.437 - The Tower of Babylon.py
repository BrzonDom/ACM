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


def buildTower(Twr, maxTwr):

    if Twr.sds:

        usedSds = set()

        for sd in Twr.sds:

            if sd in usedSds:
                continue

            usedSds.update(posSides[str(sd)])

            nxtBld = Twr.bld + [sd]
            nxtSds = posSides[str(sd)]
            nxtHgh = Twr.hgh + sd[2]

            nxtTwr = Tower(nxtBld, nxtSds, nxtHgh)

            buildTower(nxtTwr, maxTwr)

    else:
        maxTwr = checkMaxTwr(Twr, maxTwr)

        return maxTwr


def checkMaxTwr(Twr, maxTwr):

    if Twr.hgh > maxTwr.hgh:
        maxTwr.bld = Twr.bld
        maxTwr.sds = Twr.sds
        maxTwr.hgh = Twr.hgh

    elif Twr.hgh == maxTwr.hgh:
        if type(maxTwr.bld[0]) == list:
            maxTwr.bld += [Twr.bld]

        else:
            maxTwr.bld = [maxTwr.bld] + [Twr.bld]

    return maxTwr


def extractBlocks_Prt(InputLines, blckNum):

    print("\t\tBlocks:")
    Blocks = []

    for b in range(blckNum):

        blck = list(map(int, InputLines.pop(0).split()))
        Blocks.append(blck)

        print(f"\t\t\t{b + 1}. {blck}")
    print()

    blckNum = int(InputLines.pop(0))

    return Blocks, blckNum


def extractSides(Blocks):

    Sides = []

    for blck in Blocks:
        Sides += list(set(permutations(blck, 3)))

    return Sides


def prntSides(Sides):

    print(f"\t\tSides:\n\t\t\t", end="")

    for s, sd in enumerate(Sides):
        print(sd, end=" ")

        if (s + 1) % 5 == 0 and (s + 1) != len(Sides):
            print("\n\t\t\t", end="")
    print("\n")


def prntSidesPosNum(Sides, posSides):

    print(f"\t\tPossible sides:")

    for sd in Sides:

        if len(posSides[str(sd)]) == 0:
            break

        print(f"\t\t\t{sd} : {len(posSides[str(sd)])}")
    print()


def findPosSides_Prt(Sides):

    print(f"\t\tPossible sides:")
    posSides = {}

    for sd in Sides:
        print(f"\t\t\tSide: {sd} ")

        posSides[str(sd)] = []

        for nxtSd in Sides:
            if nxtSd[0] < sd[0] and nxtSd[1] < sd[1]:
                posSides[str(sd)] += [nxtSd]

        if posSides[str(sd)]:
            print(f"\t\t\t\tNum. of pos. sides: {len(posSides[str(sd)])}")
            print("\t\t\t\t\t", end="")

            for s, psSd in enumerate(posSides[str(sd)]):
                print(psSd, end=" ")

                if (s + 1) % 5 == 0 and (s + 1) != len(posSides[str(sd)]):
                    print("\n\t\t\t\t\t", end="")
            print("\n")
        else:
            print()
    print()

    Sides.sort(key=lambda key: len(posSides[str(key)]), reverse=True)

    return posSides, Sides


def findPosSides(Sides):

    posSides = {}

    for sd in Sides:

        posSides[str(sd)] = []

        for nxtSd in Sides:
            if nxtSd[0] < sd[0] and nxtSd[1] < sd[1]:
                posSides[str(sd)] += [nxtSd]

    Sides.sort(key=lambda key: len(posSides[str(key)]), reverse=True)

    return posSides, Sides


def sortPosSides_Prt(posSides):

    for orgSd in posSides:
        print(f"\t\tSide: {orgSd}")
        print(f"\t\t\tUnsorted: {posSides[orgSd]}")

        posSds = posSides[orgSd]
        posSds.sort(key=lambda key: len(posSides[str(key)]), reverse=True)

        posSides[orgSd] = posSds

        print(f"\t\t\tSorted:   {posSides[orgSd]}")
        print()

    return posSides


def sortPosSides(posSides):

    for orgSd in posSides:

        posSds = posSides[orgSd]
        posSds.sort(key=lambda key: len(posSides[str(key)]), reverse=True)

        posSides[orgSd] = posSds

    return posSides


def prntMaxTwr(maxTwr, caseCnt):

    print(f"\t\tMax Tower:")

    if type(maxTwr.bld[0]) == list:
        print(f"\t\t\tMax builds: {maxTwr.bld[0]}")

        for maxBld in maxTwr.bld[1:]:
            print(f"\t\t\t\t\t\t{maxBld}")
    else:
        print(f"\t\t\tMax build:  {maxTwr.bld}")

    print(f"\t\t\tMax height: {maxTwr.hgh}")
    print()
    print(f"\t\tCase {caseCnt}: maximum height = {maxTwr.hgh}")


"""__Input__"""
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

InputTst_Str = """
5
31 41 59
26 53 58
97 93 23
84 62 64
33 83 27
20
10 19 18
18 19 22
23 33 34
19 21 22
32 32 31
10 90 10
10 80 10
22 22 29
29 28 27
26 25 24
19 80  1
22 21 31
29 28 55
58 42 39
48 78 32
2   2 90
3  99 33
54 44 44
57 13 33
10 29 80
5
1  1  1
1  2  1
1  3  1
1  4  1 
1  5  1
5
2  3 100
3  4 200
4  6  50
6  8 100
5  5  75
1
80 90 100
6
15 19 3
44 33 21
88 33 57
31 29 20
99 88 1
52 26 5
2
100 100 100
102  98 100
10
1 2 3
4 5 6
7 8 9
10 11 12
13 14 15
16 17 18
19 20 21
22 23 24
25 26 27
28 29 30
8
10 16 1
5  8  2
20 32 2
10 16 2
16 10 2
32 20 2
8  5  2
16 10 1
0
"""

InputPartTst_Str = """
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

# InputStr = InputRaw_Str[1:-1]
InputStr = InputTst_Str[1:-1]
# InputStr = InputPartTst_Str[1:-1]

if __name__ == '__main__':

    print("Input:")
    print(InputStr)
    print()

    InputLines = InputStr.split("\n")

    blckNum = int(InputLines.pop(0))
    caseCnt = 0

    while blckNum > 0:

        caseCnt += 1
        print(f"\tCase: {caseCnt}")
        print()

        Blocks, blckNum = extractBlocks_Prt(InputLines, blckNum)
        Sides = extractSides(Blocks)

        # prntSides(Sides)

        # posSides, Sides = findPosSides_Prt(Sides)
        posSides, Sides = findPosSides(Sides)

        # prntSidesPosNum(Sides, posSides)

        # posSides = sortPosSides_Prt(posSides)
        posSides = sortPosSides(posSides)

        maxTwr = Tower([], Sides, 0)

        usedSides = set()

        for sd in Sides:

            if sd in usedSides:
                continue

            usedSides.update(posSides[str(sd)])

            Twr = Tower([sd], posSides[str(sd)], sd[2])

            maxTwr = checkMaxTwr(Twr, maxTwr)

            buildTower(Twr, maxTwr)

        prntMaxTwr(maxTwr, caseCnt)

        if blckNum != 0:
            print("\n")


"""__Output__"""
"""
Input:
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

		Blocks:
			1. [1, 1, 1]
			2. [2, 2, 2]
			3. [3, 3, 3]
			4. [4, 4, 4]
			5. [5, 5, 5]
			6. [6, 6, 6]
			7. [7, 7, 7]

		Possible sides:
			Side: (1, 1, 1) 

			Side: (2, 2, 2) 
				Num. of pos. sides: 1
					(1, 1, 1) 

			Side: (3, 3, 3) 
				Num. of pos. sides: 2
					(1, 1, 1) (2, 2, 2) 

			Side: (4, 4, 4) 
				Num. of pos. sides: 3
					(1, 1, 1) (2, 2, 2) (3, 3, 3) 

			Side: (5, 5, 5) 
				Num. of pos. sides: 4
					(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) 

			Side: (6, 6, 6) 
				Num. of pos. sides: 5
					(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) (5, 5, 5) 

			Side: (7, 7, 7) 
				Num. of pos. sides: 6
					(1, 1, 1) (2, 2, 2) (3, 3, 3) (4, 4, 4) (5, 5, 5) 
					(6, 6, 6) 


	Side: (1, 1, 1)
		Unsorted: []
		Sorted:   []

	Side: (2, 2, 2)
		Unsorted: [(1, 1, 1)]
		Sorted:   [(1, 1, 1)]

	Side: (3, 3, 3)
		Unsorted: [(1, 1, 1), (2, 2, 2)]
		Sorted:   [(2, 2, 2), (1, 1, 1)]

	Side: (4, 4, 4)
		Unsorted: [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
		Sorted:   [(3, 3, 3), (2, 2, 2), (1, 1, 1)]

	Side: (5, 5, 5)
		Unsorted: [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]
		Sorted:   [(4, 4, 4), (3, 3, 3), (2, 2, 2), (1, 1, 1)]

	Side: (6, 6, 6)
		Unsorted: [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)]
		Sorted:   [(5, 5, 5), (4, 4, 4), (3, 3, 3), (2, 2, 2), (1, 1, 1)]

	Side: (7, 7, 7)
		Unsorted: [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6)]
		Sorted:   [(6, 6, 6), (5, 5, 5), (4, 4, 4), (3, 3, 3), (2, 2, 2), (1, 1, 1)]

		Max Tower:
			Max build:  [(7, 7, 7), (6, 6, 6), (5, 5, 5), (4, 4, 4), (3, 3, 3), (2, 2, 2), (1, 1, 1)]
			Max height: 28

		Case 1: maximum height = 28


	Case: 2

		Blocks:
			1. [31, 41, 59]
			2. [26, 53, 58]
			3. [97, 93, 23]
			4. [84, 62, 64]
			5. [33, 83, 27]

		Possible sides:
			Side: (31, 59, 41) 
				Num. of pos. sides: 3
					(26, 53, 58) (26, 58, 53) (27, 33, 83) 

			Side: (59, 31, 41) 
				Num. of pos. sides: 3
					(58, 26, 53) (53, 26, 58) (33, 27, 83) 

			Side: (59, 41, 31) 
				Num. of pos. sides: 5
					(41, 31, 59) (58, 26, 53) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (41, 59, 31) 
				Num. of pos. sides: 5
					(31, 41, 59) (26, 53, 58) (26, 58, 53) (33, 27, 83) (27, 33, 83) 

			Side: (31, 41, 59) 
				Num. of pos. sides: 1
					(27, 33, 83) 

			Side: (41, 31, 59) 
				Num. of pos. sides: 1
					(33, 27, 83) 

			Side: (58, 26, 53) 

			Side: (58, 53, 26) 
				Num. of pos. sides: 5
					(31, 41, 59) (41, 31, 59) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (26, 53, 58) 

			Side: (53, 58, 26) 
				Num. of pos. sides: 5
					(31, 41, 59) (41, 31, 59) (26, 53, 58) (33, 27, 83) (27, 33, 83) 

			Side: (26, 58, 53) 

			Side: (53, 26, 58) 

			Side: (93, 23, 97) 

			Side: (93, 97, 23) 
				Num. of pos. sides: 25
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (23, 93, 97) (84, 64, 62) (64, 62, 84) 
					(62, 84, 64) (62, 64, 84) (64, 84, 62) (84, 62, 64) (83, 27, 33) 
					(83, 33, 27) (33, 27, 83) (33, 83, 27) (27, 83, 33) (27, 33, 83) 

			Side: (97, 93, 23) 
				Num. of pos. sides: 25
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (93, 23, 97) (84, 64, 62) (64, 62, 84) 
					(62, 84, 64) (62, 64, 84) (64, 84, 62) (84, 62, 64) (83, 27, 33) 
					(83, 33, 27) (33, 27, 83) (33, 83, 27) (27, 83, 33) (27, 33, 83) 

			Side: (23, 93, 97) 

			Side: (97, 23, 93) 

			Side: (23, 97, 93) 

			Side: (84, 64, 62) 
				Num. of pos. sides: 17
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (64, 62, 84) (83, 27, 33) (83, 33, 27) 
					(33, 27, 83) (27, 33, 83) 

			Side: (64, 62, 84) 
				Num. of pos. sides: 14
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (62, 84, 64) 
				Num. of pos. sides: 16
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (33, 27, 83) (33, 83, 27) (27, 83, 33) 
					(27, 33, 83) 

			Side: (62, 64, 84) 
				Num. of pos. sides: 14
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (33, 27, 83) (27, 33, 83) 

			Side: (64, 84, 62) 
				Num. of pos. sides: 17
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (62, 64, 84) (33, 27, 83) (33, 83, 27) 
					(27, 83, 33) (27, 33, 83) 

			Side: (84, 62, 64) 
				Num. of pos. sides: 16
					(31, 59, 41) (59, 31, 41) (59, 41, 31) (41, 59, 31) (31, 41, 59) 
					(41, 31, 59) (58, 26, 53) (58, 53, 26) (26, 53, 58) (53, 58, 26) 
					(26, 58, 53) (53, 26, 58) (83, 27, 33) (83, 33, 27) (33, 27, 83) 
					(27, 33, 83) 

			Side: (83, 27, 33) 
				Num. of pos. sides: 2
					(58, 26, 53) (53, 26, 58) 

			Side: (83, 33, 27) 
				Num. of pos. sides: 5
					(59, 31, 41) (41, 31, 59) (58, 26, 53) (53, 26, 58) (33, 27, 83) 

			Side: (33, 27, 83) 

			Side: (33, 83, 27) 
				Num. of pos. sides: 5
					(31, 59, 41) (31, 41, 59) (26, 53, 58) (26, 58, 53) (27, 33, 83) 

			Side: (27, 83, 33) 
				Num. of pos. sides: 2
					(26, 53, 58) (26, 58, 53) 

			Side: (27, 33, 83) 


	Side: (31, 59, 41)
		Unsorted: [(26, 53, 58), (26, 58, 53), (27, 33, 83)]
		Sorted:   [(26, 53, 58), (26, 58, 53), (27, 33, 83)]

	Side: (59, 31, 41)
		Unsorted: [(58, 26, 53), (53, 26, 58), (33, 27, 83)]
		Sorted:   [(58, 26, 53), (53, 26, 58), (33, 27, 83)]

	Side: (59, 41, 31)
		Unsorted: [(41, 31, 59), (58, 26, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(41, 31, 59), (58, 26, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (41, 59, 31)
		Unsorted: [(31, 41, 59), (26, 53, 58), (26, 58, 53), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(31, 41, 59), (26, 53, 58), (26, 58, 53), (33, 27, 83), (27, 33, 83)]

	Side: (31, 41, 59)
		Unsorted: [(27, 33, 83)]
		Sorted:   [(27, 33, 83)]

	Side: (41, 31, 59)
		Unsorted: [(33, 27, 83)]
		Sorted:   [(33, 27, 83)]

	Side: (58, 26, 53)
		Unsorted: []
		Sorted:   []

	Side: (58, 53, 26)
		Unsorted: [(31, 41, 59), (41, 31, 59), (53, 26, 58), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(31, 41, 59), (41, 31, 59), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (26, 53, 58)
		Unsorted: []
		Sorted:   []

	Side: (53, 58, 26)
		Unsorted: [(31, 41, 59), (41, 31, 59), (26, 53, 58), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(31, 41, 59), (41, 31, 59), (26, 53, 58), (33, 27, 83), (27, 33, 83)]

	Side: (26, 58, 53)
		Unsorted: []
		Sorted:   []

	Side: (53, 26, 58)
		Unsorted: []
		Sorted:   []

	Side: (93, 23, 97)
		Unsorted: []
		Sorted:   []

	Side: (93, 97, 23)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (23, 93, 97), (84, 64, 62), (64, 62, 84), (62, 84, 64), (62, 64, 84), (64, 84, 62), (84, 62, 64), (83, 27, 33), (83, 33, 27), (33, 27, 83), (33, 83, 27), (27, 83, 33), (27, 33, 83)]
		Sorted:   [(84, 64, 62), (64, 84, 62), (62, 84, 64), (84, 62, 64), (64, 62, 84), (62, 64, 84), (59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (83, 33, 27), (33, 83, 27), (31, 59, 41), (59, 31, 41), (83, 27, 33), (27, 83, 33), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (23, 93, 97), (33, 27, 83), (27, 33, 83)]

	Side: (97, 93, 23)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (93, 23, 97), (84, 64, 62), (64, 62, 84), (62, 84, 64), (62, 64, 84), (64, 84, 62), (84, 62, 64), (83, 27, 33), (83, 33, 27), (33, 27, 83), (33, 83, 27), (27, 83, 33), (27, 33, 83)]
		Sorted:   [(84, 64, 62), (64, 84, 62), (62, 84, 64), (84, 62, 64), (64, 62, 84), (62, 64, 84), (59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (83, 33, 27), (33, 83, 27), (31, 59, 41), (59, 31, 41), (83, 27, 33), (27, 83, 33), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (93, 23, 97), (33, 27, 83), (27, 33, 83)]

	Side: (23, 93, 97)
		Unsorted: []
		Sorted:   []

	Side: (97, 23, 93)
		Unsorted: []
		Sorted:   []

	Side: (23, 97, 93)
		Unsorted: []
		Sorted:   []

	Side: (84, 64, 62)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (64, 62, 84), (83, 27, 33), (83, 33, 27), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(64, 62, 84), (59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (83, 33, 27), (31, 59, 41), (59, 31, 41), (83, 27, 33), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (64, 62, 84)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (31, 59, 41), (59, 31, 41), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (62, 84, 64)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (33, 27, 83), (33, 83, 27), (27, 83, 33), (27, 33, 83)]
		Sorted:   [(59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (33, 83, 27), (31, 59, 41), (59, 31, 41), (27, 83, 33), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (62, 64, 84)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (31, 59, 41), (59, 31, 41), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (64, 84, 62)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (62, 64, 84), (33, 27, 83), (33, 83, 27), (27, 83, 33), (27, 33, 83)]
		Sorted:   [(62, 64, 84), (59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (33, 83, 27), (31, 59, 41), (59, 31, 41), (27, 83, 33), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (84, 62, 64)
		Unsorted: [(31, 59, 41), (59, 31, 41), (59, 41, 31), (41, 59, 31), (31, 41, 59), (41, 31, 59), (58, 26, 53), (58, 53, 26), (26, 53, 58), (53, 58, 26), (26, 58, 53), (53, 26, 58), (83, 27, 33), (83, 33, 27), (33, 27, 83), (27, 33, 83)]
		Sorted:   [(59, 41, 31), (41, 59, 31), (58, 53, 26), (53, 58, 26), (83, 33, 27), (31, 59, 41), (59, 31, 41), (83, 27, 33), (31, 41, 59), (41, 31, 59), (58, 26, 53), (26, 53, 58), (26, 58, 53), (53, 26, 58), (33, 27, 83), (27, 33, 83)]

	Side: (83, 27, 33)
		Unsorted: [(58, 26, 53), (53, 26, 58)]
		Sorted:   [(58, 26, 53), (53, 26, 58)]

	Side: (83, 33, 27)
		Unsorted: [(59, 31, 41), (41, 31, 59), (58, 26, 53), (53, 26, 58), (33, 27, 83)]
		Sorted:   [(59, 31, 41), (41, 31, 59), (58, 26, 53), (53, 26, 58), (33, 27, 83)]

	Side: (33, 27, 83)
		Unsorted: []
		Sorted:   []

	Side: (33, 83, 27)
		Unsorted: [(31, 59, 41), (31, 41, 59), (26, 53, 58), (26, 58, 53), (27, 33, 83)]
		Sorted:   [(31, 59, 41), (31, 41, 59), (26, 53, 58), (26, 58, 53), (27, 33, 83)]

	Side: (27, 83, 33)
		Unsorted: [(26, 53, 58), (26, 58, 53)]
		Sorted:   [(26, 53, 58), (26, 58, 53)]

	Side: (27, 33, 83)
		Unsorted: []
		Sorted:   []

		Max Tower:
			Max builds: [(93, 97, 23), (84, 64, 62), (64, 62, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
						[(93, 97, 23), (84, 64, 62), (64, 62, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
						[(93, 97, 23), (64, 84, 62), (62, 64, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
						[(93, 97, 23), (64, 84, 62), (62, 64, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
						[(97, 93, 23), (84, 64, 62), (64, 62, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
						[(97, 93, 23), (84, 64, 62), (64, 62, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
						[(97, 93, 23), (64, 84, 62), (62, 64, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
						[(97, 93, 23), (64, 84, 62), (62, 64, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]
			Max height: 342

		Case 2: maximum height = 342

Process finished with exit code 0

"""
