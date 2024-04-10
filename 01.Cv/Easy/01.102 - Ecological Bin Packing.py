"""
102 - Ecological Bin Packing
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=38

    Bin packing, or the placement of objects of certain weights into different bins subject to certain con-
    straints, is an historically interesting problem. Some bin packing problems are NP-complete but are
    amenable to dynamic programming solutions or to approximately optimal heuristic solutions.
        In this problem you will be solving a bin packing problem that deals with recycling glass.
        Recycling glass requires that the glass be separated by color into one of three categories: brown
    glass, green glass, and clear glass. In this problem you will be given three recycling bins, each containing
    a specified number of brown, green and clear bottles. In order to be recycled, the bottles will need to
    be moved so that each bin contains bottles of only one color.
        The problem is to minimize the number of bottles that are moved. You may assume that the only
    problem is to minimize the number of movements between boxes.
        For the purposes of this problem, each bin has infinite capacity and the only constraint is moving
    the bottles so that each bin contains bottles of a single color. The total number of bottles will never
    exceed 2^31.

    Input:
            The input consists of a series of lines with each line containing 9 integers. The first three integers on a
        line represent the number of brown, green, and clear bottles (respectively) in bin number 1, the second
        three represent the number of brown, green and clear bottles (respectively) in bin number 2, and the
        last three integers represent the number of brown, green, and clear bottles (respectively) in bin number
        3. For example, the line
            10 15 20 30 12 8 15 8 31
        indicates that there are 20 clear bottles in bin 1, 12 green bottles in bin 2, and 15 brown bottles in bin
        3.
            Integers on a line will be separated by one or more spaces. Your program should process all lines in
        the input file.

    Output:
            For each line of input there will be one line of output indicating what color bottles go in what bin
        to minimize the number of bottle movements. You should also print the minimum number of bottle
        movements.
            The output should consist of a string of the three upper case characters ‘G’, ‘B’, ‘C’ (representing
        the colors green, brown, and clear) representing the color associated with each bin.
            The first character of the string represents the color associated with the first bin, the second character
        of the string represents the color associated with the second bin, and the third character represents the
        color associated with the third bin.
            The integer indicating the minimum number of bottle movements should follow the string.
            If more than one order of brown, green, and clear bins yields the minimum number of movements
        then the alphabetically first string representing a minimal configuration should be printed.


    Sample:
        1 2 3 4 5 6 7 8 9
        5 10 5 20 10 5 10 20 10
            =>  BCG 30
                CBG 50

"""


def showBinInf(binData):

    # print("\t\tBins:")
    for b in range(3):
        print(f"\t\t\t{b + 1}. Bin: Tot: {sum(binData[b]):2}, "
              f"[ {binData[b][0]:2}B, {binData[b][1]:2}G, {binData[b][2]:2}C ]")
    print()


def showBinAddInf(binData):

    colorPos = ['B', 'G', 'C',
                "Brown", "Green", "Clear"]

    for b in range(3):
        maxBot = max(binData[b])
        rstBot = sum(binData[b]) - maxBot
        maxCol = colorPos[binData[b].index(maxBot)]

        print(f"\t\t\t{b + 1}. Bin: Max: {maxBot}{maxCol}, Rest: {rstBot}")
    print()


def showBttlInf(colorCnt):

    # print("\t\tBottles:")
    print(f"\t\t\tBrown: {colorCnt['B']}")
    print(f"\t\t\tGreen: {colorCnt['G']}")
    print(f"\t\t\tClear: {colorCnt['C']}")
    print()


def findPrmt(permColo, binData):

    minTot = sum(binData[0] + binData[1] + binData[2])
    minPer = ""

    for perm in permColo:
        print(f"\t\t\t{perm}")

        totCnt = 0

        for bn, col in enumerate(perm):
            cntCol = binData[bn][convColBin[col]]
            cntRst = sum(binData[bn]) - cntCol

            rstCol = list(perm)
            rstCol.remove(col)
            rstCnt = [binData[bn][convColBin[rstCol[0]]], binData[bn][convColBin[rstCol[0]]]]

            print(f"\t\t\t\t{bn + 1}. {col}: {cntCol:2},\t"
                  f"R: {cntRst:2} [ {rstCnt[0]:2}{rstCol[0]}, {rstCnt[1]:2}{rstCol[1]} ]")

            totCnt += cntRst

        if totCnt < minTot:
            minTot = totCnt
            minPer = perm

        print(f"\t\t\t\t\t\tTotal: {totCnt}")
        print()
    print()

    return minPer, minTot


InputRaw_Str ="""
1 2 3 4 5 6 7 8 9
5 10 5 20 10 5 10 20 10
"""

# from itertools import permutations
#
# tstPer = permutations([0, 1, 2], 3)
#
# for p, per in enumerate(tstPer):
#     print((p+1), list(per))
#
# quit()


InputRaw_Str = InputRaw_Str[1:-1]

if __name__ == "__main__":

    permColo = ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']

    convColBin = {'B' : 0, 0 : 'B',
                  'G' : 1, 1 : 'G',
                  'C' : 2, 2 : 'C' }

    convFullCol = {'B' : 'Brown',
                   'G' : 'Green',
                   'C' : 'Clear'}

    print("Input:")
    print(InputRaw_Str)
    print()

    InputStr_Lst = InputRaw_Str.split("\n")

    for i, InputStr in enumerate(InputStr_Lst):

        print(f"\t{i+1}.Input line: {InputStr}")
        print()

        binInLst = list(map(int, InputStr.split()))

        # print(f"\t\t{binInLst}")
        # print()

        binData = {0 : binInLst[0:3],
                   1 : binInLst[3:6],
                   2 : binInLst[6:9]}

        # binData[0] = binInLst[0:3]
        # binData[1] = binInLst[3:6]
        # binData[2] = binInLst[6:9]

        print("\t\tBins:")
        showBinInf(binData)

        showBinAddInf(binData)

        # colorPos = ['B', 'G', 'C',
        #             "Brown", "Green", "Clear"]

        # print("\t\tBins:")
        # for b in range(3):
        #     print(f"\t\t\t{b+1}. Bin: Tot: {sum(binData[b]):2}, [ {binData[b][0]:2}B, {binData[b][1]:2}G, {binData[b][2]:2}C ]")
        # print()

        # for b in range(3):
        #     maxBot = max(binData[b])
        #     rstBot = sum(binData[b]) - maxBot
        #     maxCol = colorPos[binData[b].index(maxBot)]
        #     print(f"\t\t\t{b+1}. Bin: Max: {maxBot}{maxCol}, Rest: {rstBot}")
        # print()

        colorCnt = {'B' : binInLst[0] + binInLst[3] + binInLst[6],
                    'G' : binInLst[1] + binInLst[4] + binInLst[7],
                    'C' : binInLst[2] + binInLst[5] + binInLst[8] }

        print("\t\tBottles:")
        showBttlInf(colorCnt)

        # print("\t\tBottles:")
        # print(f"\t\t\tBrown: {colorCnt['B']}")
        # print(f"\t\t\tGreen: {colorCnt['G']}")
        # print(f"\t\t\tClear: {colorCnt['C']}")
        # print()

        print("\t\tPermutations:\n")
        minPer, minTot = findPrmt(permColo, binData)

        # minTot = sum(colorCnt.values())
        # minPer = ""
        #
        # print("\t\tPermutations:\n")
        # for perm in permColo:
        #     print(f"\t\t\t{perm}")
        #
        #     totCnt = 0
        #
        #     for bn, col in enumerate(perm):
        #         cntCol = binData[bn][convColBin[col]]
        #         cntRst = sum(binData[bn]) - cntCol
        #
        #         print(f"\t\t\t\t{bn+1}. {col}: {cntCol:2},\tR: {cntRst:2}")
        #
        #         totCnt += cntRst
        #
        #     if totCnt < minTot:
        #         minTot = totCnt
        #         minPer = perm
        #
        #     print(f"\t\t\t\t\t\tTotal: {totCnt}")
        #     print()
        # print()

        print(f"\t\tFound permutation: {minPer}")
        print(f"\t\t\t\t\tTotal: {minTot}")
        print()

        for bn, col in enumerate(minPer):
            print(f"\t\t\t{bn+1}. {convFullCol[col]} [{col}]: {binData[bn][convColBin[col]]:2}")

        # print(f"\t\t\t{minPer}")

        if i < len(InputStr_Lst) - 1:
            print("\n")


"""__Output__"""
"""
Input:
1 2 3 4 5 6 7 8 9
5 10 5 20 10 5 10 20 10

	1.Input line: 1 2 3 4 5 6 7 8 9

		Bins:
			1. Bin: Tot:  6, [  1B,  2G,  3C ]
			2. Bin: Tot: 15, [  4B,  5G,  6C ]
			3. Bin: Tot: 24, [  7B,  8G,  9C ]

			1. Bin: Max: 3C, Rest: 3
			2. Bin: Max: 6C, Rest: 9
			3. Bin: Max: 9C, Rest: 15

		Bottles:
			Brown: 12
			Green: 15
			Clear: 18

		Permutations:

			BCG
				1. B:  1,	R:  5 [  3C,  3G ]
				2. C:  6,	R:  9 [  4B,  4G ]
				3. G:  8,	R: 16 [  7B,  7C ]
						Total: 30

			BGC
				1. B:  1,	R:  5 [  2G,  2C ]
				2. G:  5,	R: 10 [  4B,  4C ]
				3. C:  9,	R: 15 [  7B,  7G ]
						Total: 30

			CBG
				1. C:  3,	R:  3 [  1B,  1G ]
				2. B:  4,	R: 11 [  6C,  6G ]
				3. G:  8,	R: 16 [  9C,  9B ]
						Total: 30

			CGB
				1. C:  3,	R:  3 [  2G,  2B ]
				2. G:  5,	R: 10 [  6C,  6B ]
				3. B:  7,	R: 17 [  9C,  9G ]
						Total: 30

			GBC
				1. G:  2,	R:  4 [  1B,  1C ]
				2. B:  4,	R: 11 [  5G,  5C ]
				3. C:  9,	R: 15 [  8G,  8B ]
						Total: 30

			GCB
				1. G:  2,	R:  4 [  3C,  3B ]
				2. C:  6,	R:  9 [  5G,  5B ]
				3. B:  7,	R: 17 [  8G,  8C ]
						Total: 30


		Found permutation: BCG
					Total: 30

			1. Brown [B]:  1
			2. Clear [C]:  6
			3. Green [G]:  8


	2.Input line: 5 10 5 20 10 5 10 20 10

		Bins:
			1. Bin: Tot: 20, [  5B, 10G,  5C ]
			2. Bin: Tot: 35, [ 20B, 10G,  5C ]
			3. Bin: Tot: 40, [ 10B, 20G, 10C ]

			1. Bin: Max: 10G, Rest: 10
			2. Bin: Max: 20B, Rest: 15
			3. Bin: Max: 20G, Rest: 20

		Bottles:
			Brown: 35
			Green: 40
			Clear: 20

		Permutations:

			BCG
				1. B:  5,	R: 15 [  5C,  5G ]
				2. C:  5,	R: 30 [ 20B, 20G ]
				3. G: 20,	R: 20 [ 10B, 10C ]
						Total: 65

			BGC
				1. B:  5,	R: 15 [ 10G, 10C ]
				2. G: 10,	R: 25 [ 20B, 20C ]
				3. C: 10,	R: 30 [ 10B, 10G ]
						Total: 70

			CBG
				1. C:  5,	R: 15 [  5B,  5G ]
				2. B: 20,	R: 15 [  5C,  5G ]
				3. G: 20,	R: 20 [ 10C, 10B ]
						Total: 50

			CGB
				1. C:  5,	R: 15 [ 10G, 10B ]
				2. G: 10,	R: 25 [  5C,  5B ]
				3. B: 10,	R: 30 [ 10C, 10G ]
						Total: 70

			GBC
				1. G: 10,	R: 10 [  5B,  5C ]
				2. B: 20,	R: 15 [ 10G, 10C ]
				3. C: 10,	R: 30 [ 20G, 20B ]
						Total: 55

			GCB
				1. G: 10,	R: 10 [  5C,  5B ]
				2. C:  5,	R: 30 [ 10G, 10B ]
				3. B: 10,	R: 30 [ 20G, 20C ]
						Total: 70


		Found permutation: CBG
					Total: 50

			1. Clear [C]:  5
			2. Brown [B]: 20
			3. Green [G]: 20

Process finished with exit code 0

"""