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

"""29372490 	102 	Ecological Bin Packing 	Accepted 	PYTH3 	0.980 	2024-04-10 13:57:46"""

InputRaw_Str ="""
1 2 3 4 5 6 7 8 9
5 10 5 20 10 5 10 20 10
"""

InputRaw_Str = InputRaw_Str[1:-1]


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
        # print(f"\t\t\t{perm}")

        totCnt = 0

        for bn, col in enumerate(perm):
            cntCol = binData[bn][convColBin[col]]
            cntRst = sum(binData[bn]) - cntCol

            # print(f"\t\t\t\t{bn + 1}. {col}: {cntCol:2},\tR: {cntRst:2}")

            totCnt += cntRst

        if totCnt < minTot:
            minTot = totCnt
            minPer = perm

    #     print(f"\t\t\t\t\t\tTotal: {totCnt}")
    #     print()
    # print()

    return minPer, minTot


if __name__ == "__main__":

    permColo = ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']

    convColBin = {'B' : 0, 0 : 'B',
                  'G' : 1, 1 : 'G',
                  'C' : 2, 2 : 'C' }

    # convFullCol = {'B' : 'Brown',
    #                'G' : 'Green',
    #                'C' : 'Clear'}

    # inCnt = 0

    while True:

        try:
            InputStr = input()

        except EOFError:
            break

        # inCnt += 1

        # print(f"\t{inCnt+1}.Input line: {InputStr}")
        # print()

        binInLst = list(map(int, InputStr.split()))

        binData = {0 : binInLst[0:3],
                   1 : binInLst[3:6],
                   2 : binInLst[6:9]}

        # print("\t\tBins:")
        # showBinInf(binData)

        # showBinAddInf(binData)

        colorCnt = {'B' : binInLst[0] + binInLst[3] + binInLst[6],
                    'G' : binInLst[1] + binInLst[4] + binInLst[7],
                    'C' : binInLst[2] + binInLst[5] + binInLst[8] }

        # print("\t\tBottles:")
        # showBttlInf(colorCnt)

        # print("\t\tPermutations:\n")
        minPer, minTot = findPrmt(permColo, binData)

        # print(f"\t\tFound permutation: {minPer}")
        # print(f"\t\t\t\t\tTotal: {minTot}")
        # print()
        #
        # for bn, col in enumerate(minPer):
        #     print(f"\t\t\t{bn+1}. {convFullCol[col]} [{col}]: {binData[bn][convColBin[col]]:2}")
        #
        # print("\n")

        print(f"{minPer} {minTot}")