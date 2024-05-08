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
        for sd in Twr.sds:

            nxtBld = Twr.bld + [sd]
            nxtSds = posSides[str(sd)]
            nxtHgh = Twr.hgh + sd[2]

            nxtTwr = Tower(nxtBld, nxtSds, nxtHgh)

            buildTower(nxtTwr, maxTwr)

    else:
        # print(f"\t\tTower:  {Twr.bld}")
        # print(f"\t\tHeight: {Twr.hgh}")
        # print()

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
7
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
0
"""

InputStr = InputRaw_Str[1:-1]
# InputStr = InputTst_Str[1:-1]

if __name__ == '__main__':

    print("Input:")
    print(InputStr)
    print()

    InputLines = InputStr.split("\n")

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
            print(f"\t\t\tSide: {sd} ")
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
                print(f"\t\t\t\tNum. of pos. sides: {len(posSides[str(sd)])}")
                print("\t\t\t\t", end="")
                for s, psSd in enumerate(posSides[str(sd)]):
                    print(psSd, end=" ")

                    if (s+1) % 5 == 0 and (s+1) != len(posSides[str(sd)]):
                        print("\n\t\t\t\t", end="")
                print("\n")
            else:
                print()
        print()

        Sides.sort(key=lambda key: len(posSides[str(key)]), reverse=True)

        for sd in Sides:

            if len(posSides[str(sd)]) == 0:
                break

            print(f"\t\t\t{sd} : {len(posSides[str(sd)])}")
        print()

        maxTwr = Tower([], Sides, 0)
        usedSides = set()

        # print(type(posSides["(7, 7, 7)"]))
        # print(type(set(posSides["(7, 7, 7)"])))

        for sd in Sides:

            if sd in usedSides:
                continue

            usedSides.update(posSides[str(sd)])

            Twr = Tower([sd], posSides[str(sd)], sd[2])

            if Twr.hgh > maxTwr.hgh:
                maxTwr.bld = Twr.bld
                maxTwr.sds = Twr.sds
                maxTwr.hgh = Twr.hgh

            elif Twr.hgh == maxTwr.hgh:
                if type(maxTwr.bld[0]) == list:
                    maxTwr.bld += [Twr.bld]

                else:
                    maxTwr.bld = [maxTwr.bld] + [Twr.bld]

            buildTower(Twr, maxTwr)

        print(f"\t\tMax Tower:")
        print(f"\t\t\tMax build:  {maxTwr.bld}")
        print(f"\t\t\tMax height: {maxTwr.hgh}")

        if blckNum != 0:
            print("\n")


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
				Num. of pos. sides: 1
				(10, 20, 30) 

			Side: (20, 10, 30) 

			Side: (10, 20, 30) 

			Side: (30, 10, 20) 

			Side: (30, 20, 10) 
				Num. of pos. sides: 1
				(20, 10, 30) 


			(20, 30, 10) : 1
			(30, 20, 10) : 1

		Max Tower:
			Max build:  [[(20, 30, 10), (10, 20, 30)], [(30, 20, 10), (20, 10, 30)]]
			Max height: 40


	Case: 2

		1. [6, 8, 10]
		2. [5, 5, 5]

		Sides:
			(6, 8, 10) (10, 6, 8) (8, 6, 10) (10, 8, 6) (6, 10, 8) 
			(8, 10, 6) (5, 5, 5) 

			Side: (6, 8, 10) 
				Num. of pos. sides: 1
				(5, 5, 5) 

			Side: (10, 6, 8) 
				Num. of pos. sides: 1
				(5, 5, 5) 

			Side: (8, 6, 10) 
				Num. of pos. sides: 1
				(5, 5, 5) 

			Side: (10, 8, 6) 
				Num. of pos. sides: 2
				(8, 6, 10) (5, 5, 5) 

			Side: (6, 10, 8) 
				Num. of pos. sides: 1
				(5, 5, 5) 

			Side: (8, 10, 6) 
				Num. of pos. sides: 2
				(6, 8, 10) (5, 5, 5) 

			Side: (5, 5, 5) 


			(10, 8, 6) : 2
			(8, 10, 6) : 2
			(6, 8, 10) : 1
			(10, 6, 8) : 1
			(8, 6, 10) : 1
			(6, 10, 8) : 1

		Max Tower:
			Max build:  [[(10, 8, 6), (8, 6, 10), (5, 5, 5)], [(8, 10, 6), (6, 8, 10), (5, 5, 5)]]
			Max height: 21


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


			(7, 7, 7) : 6
			(6, 6, 6) : 5
			(5, 5, 5) : 4
			(4, 4, 4) : 3
			(3, 3, 3) : 2
			(2, 2, 2) : 1

		Max Tower:
			Max build:  [(7, 7, 7), (6, 6, 6), (5, 5, 5), (4, 4, 4), (3, 3, 3), (2, 2, 2), (1, 1, 1)]
			Max height: 28


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


			(93, 97, 23) : 25
			(97, 93, 23) : 25
			(84, 64, 62) : 17
			(64, 84, 62) : 17
			(62, 84, 64) : 16
			(84, 62, 64) : 16
			(64, 62, 84) : 14
			(62, 64, 84) : 14
			(59, 41, 31) : 5
			(41, 59, 31) : 5
			(58, 53, 26) : 5
			(53, 58, 26) : 5
			(83, 33, 27) : 5
			(33, 83, 27) : 5
			(31, 59, 41) : 3
			(59, 31, 41) : 3
			(83, 27, 33) : 2
			(27, 83, 33) : 2
			(31, 41, 59) : 1
			(41, 31, 59) : 1

		Max Tower:
			Max build:  [[(93, 97, 23), (84, 64, 62), (64, 62, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)], [(93, 97, 23), (84, 64, 62), (64, 62, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)], [(93, 97, 23), (64, 84, 62), (62, 64, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)], [(93, 97, 23), (64, 84, 62), (62, 64, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)], [(97, 93, 23), (84, 64, 62), (64, 62, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)], [(97, 93, 23), (84, 64, 62), (64, 62, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)], [(97, 93, 23), (64, 84, 62), (62, 64, 84), (59, 41, 31), (41, 31, 59), (33, 27, 83)], [(97, 93, 23), (64, 84, 62), (62, 64, 84), (41, 59, 31), (31, 41, 59), (27, 33, 83)]]
			Max height: 342

Process finished with exit code 0

"""
