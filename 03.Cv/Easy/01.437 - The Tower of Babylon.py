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
        # maxTwr = checkAllMaxTwr(Twr, maxTwr)
        maxTwr = checkMaxTwr(Twr, maxTwr)

        return maxTwr


def checkAllMaxTwr(Twr, maxTwr):

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


def checkMaxTwr(Twr, maxTwr):

    if Twr.hgh > maxTwr.hgh:
        maxTwr.bld = Twr.bld
        maxTwr.sds = Twr.sds
        maxTwr.hgh = Twr.hgh

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

            maxTwr = checkAllMaxTwr(Twr, maxTwr)

            buildTower(Twr, maxTwr)

        prntMaxTwr(maxTwr, caseCnt)

        if blckNum != 0:
            print("\n")


"""__Output__"""
"""
Input:
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

	Case: 1

		Blocks:
			1. [31, 41, 59]
			2. [26, 53, 58]
			3. [97, 93, 23]
			4. [84, 62, 64]
			5. [33, 83, 27]

		Max Tower:
			Max build:  [(93, 97, 23), (84, 64, 62), (64, 62, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)]
			Max height: 342

		Case 1: maximum height = 342


	Case: 2

		Blocks:
			1. [10, 19, 18]
			2. [18, 19, 22]
			3. [23, 33, 34]
			4. [19, 21, 22]
			5. [32, 32, 31]
			6. [10, 90, 10]
			7. [10, 80, 10]
			8. [22, 22, 29]
			9. [29, 28, 27]
			10. [26, 25, 24]
			11. [19, 80, 1]
			12. [22, 21, 31]
			13. [29, 28, 55]
			14. [58, 42, 39]
			15. [48, 78, 32]
			16. [2, 2, 90]
			17. [3, 99, 33]
			18. [54, 44, 44]
			19. [57, 13, 33]
			20. [10, 29, 80]

		Max Tower:
			Max build:  [(78, 48, 32), (44, 44, 54), (39, 42, 58), (33, 34, 23), (32, 31, 32), (29, 28, 55), (28, 27, 29), (26, 25, 24), (25, 24, 26), (22, 21, 31), (21, 19, 22), (19, 18, 22), (10, 10, 90), (2, 2, 90)]
			Max height: 588

		Case 2: maximum height = 588


	Case: 3

		Blocks:
			1. [1, 1, 1]
			2. [1, 2, 1]
			3. [1, 3, 1]
			4. [1, 4, 1]
			5. [1, 5, 1]

		Max Tower:
			Max build:  [(1, 1, 5)]
			Max height: 5

		Case 3: maximum height = 5


	Case: 4

		Blocks:
			1. [2, 3, 100]
			2. [3, 4, 200]
			3. [4, 6, 50]
			4. [6, 8, 100]
			5. [5, 5, 75]

		Max Tower:
			Max build:  [(8, 100, 6), (6, 8, 100), (5, 5, 75), (4, 3, 200), (3, 2, 100)]
			Max height: 481

		Case 4: maximum height = 481


	Case: 5

		Blocks:
			1. [80, 90, 100]

		Max Tower:
			Max build:  [(90, 100, 80), (80, 90, 100)]
			Max height: 180

		Case 5: maximum height = 180


	Case: 6

		Blocks:
			1. [15, 19, 3]
			2. [44, 33, 21]
			3. [88, 33, 57]
			4. [31, 29, 20]
			5. [99, 88, 1]
			6. [52, 26, 5]

		Max Tower:
			Max build:  [(99, 88, 1), (88, 57, 33), (57, 33, 88), (52, 26, 5), (33, 21, 44), (29, 20, 31), (26, 5, 52), (15, 3, 19)]
			Max height: 273

		Case 6: maximum height = 273


	Case: 7

		Blocks:
			1. [100, 100, 100]
			2. [102, 98, 100]

		Max Tower:
			Max build:  [(100, 102, 98), (98, 100, 102)]
			Max height: 200

		Case 7: maximum height = 200


	Case: 8

		Blocks:
			1. [1, 2, 3]
			2. [4, 5, 6]
			3. [7, 8, 9]
			4. [10, 11, 12]
			5. [13, 14, 15]
			6. [16, 17, 18]
			7. [19, 20, 21]
			8. [22, 23, 24]
			9. [25, 26, 27]
			10. [28, 29, 30]

		Max Tower:
			Max build:  [(30, 29, 28), (29, 28, 30), (27, 26, 25), (26, 25, 27), (23, 24, 22), (22, 23, 24), (21, 20, 19), (20, 19, 21), (18, 17, 16), (17, 16, 18), (14, 15, 13), (13, 14, 15), (11, 12, 10), (10, 11, 12), (9, 8, 7), (8, 7, 9), (5, 6, 4), (4, 5, 6), (3, 2, 1), (2, 1, 3)]
			Max height: 310

		Case 8: maximum height = 310


	Case: 9

		Blocks:
			1. [10, 16, 1]
			2. [5, 8, 2]
			3. [20, 32, 2]
			4. [10, 16, 2]
			5. [16, 10, 2]
			6. [32, 20, 2]
			7. [8, 5, 2]
			8. [16, 10, 1]

		Max Tower:
			Max build:  [(32, 20, 2), (20, 2, 32), (10, 1, 16)]
			Max height: 50

		Case 9: maximum height = 50

Process finished with exit code 0

"""
