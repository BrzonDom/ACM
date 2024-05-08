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
    def __init__(self, twr, sds, mxH):
        self.twr = twr
        self.sds = sds
        self.mxH = mxH


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
            # Sides[str(blck)] = [[blck[0], blck[1], blck[2]], [blck[1], blck[2], blck[0]], [blck[2], blck[0], blck[1]]]

            print(f"\t\t{b+1}. {blck}")

            curSides = list(set(permutations(blck, 3)))
            Sides += curSides

            print(f"\t\t\t{curSides}")

            # for side in Sides[str(blck)]:
            #     # print(f"\t\t\t{b+1}. {side}")
            #     print(f"\t\t\t\tSurface: {side[0]} * {side[1]} = {side[0] * side[1]}")
            #     print(f"\t\t\t\tHeight:  {side[2]}")
            #     print()

            print()
        print()
        print(f"\tSides: {Sides}")
        print()

        caseCnt += 1
        blckNum = int(InputLines.pop(0))

        for sd in Sides:
            print(f"\t\tSide: {sd}")
            # print(f"\t\tPossible sides:")
            print()

            posSides = []

            for nxtSd in Sides:
                if nxtSd[0] < sd[0] and nxtSd[1] < sd[1]:
                    # print(f"\t\t\t{nxtSd}")

                    posSides.append(nxtSd)
            # print()

            # for posSd in posSides:
            #     print(f"\t\t\tpos: {posSd}")
                # print(f"\t\t\tTower:  {[sd, posSd]}")
                # print(f"\t\t\tHeight: {sd[2] + posSd[2]}")
                # print(f"\t\t\tSides:  {[s for s in posSides if s != posSd]}")
                # print()
            # print()

            for posSd in posSides:
                nxtTwr = Tower([sd, posSd], posSides, sd[2] + posSd[2])

                print(f"\t\t\tTower: {nxtTwr.twr}")
                print(f"\t\t\tHeiht: {nxtTwr.mxH}")
                print(f"\t\t\tSides: {nxtTwr.sds}")
                print()

