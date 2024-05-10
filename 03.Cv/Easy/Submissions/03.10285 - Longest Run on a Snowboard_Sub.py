"""
10285 - Longest Run on a Snowboard
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=14&page=show_problem&problem=1226

        Michael likes snowboarding. That’s not very surprising, since snowboarding is really great. The bad
    thing is that in order to gain speed, the area must slide downwards. Another disadvantage is that when
    you’ve reached the bottom of the hill you have to walk up again or wait for the ski-lift.
    Michael would like to know how long the longest run in an area is. That area is given by a grid of
    numbers, defining the heights at those points.
        One can slide down from one point to a connected other one if and only if the height decreases. One
    point is connected to another if it’s at left, at right, above or below it.

    Input:
           The first line contains the number of test cases N . Each test case starts with a line containing the
        name (it’s a single string), the number of rows R and the number of columns C. After that follow R
        lines with C numbers each, defining the heights. R and C won’t be bigger than 100, N not bigger than
        15 and the heights are always in the range from 0 to 100.

    Output:
            For each test case, print a line containing the name of the area, a colon, a space and the length of the
        longest run one can slide down in that area.


    Sample:
        2
        Feldberg 10 5
        56 14 51 58 88
        26 94 24 39 41
        24 16 8 51 51
        76 72 77 43 10
        38 50 59 84 81
        5 23 37 71 77
        96 10 93 53 82
        94 15 96 69 9
        74 0 62 38 96
        37 54 55 82 38
        Spiral 5 5
        1 2 3 4 5
        16 17 18 19 6
        15 24 25 20 7
        14 23 22 21 8
        13 12 11 10 9
            =>  Feldberg: 7
                Spiral: 25
"""


InputOrg_Raw = """
2
Feldberg 10 5
56 14 51 58 88
26 94 24 39 41
24 16 8 51 51
76 72 77 43 10
38 50 59 84 81
5 23 37 71 77
96 10 93 53 82
94 15 96 69 9
74 0 62 38 96
37 54 55 82 38
Spiral 5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputRaw_Lst = [InputOrg_Raw]

InputRaw = InputRaw_Lst[0]

def prntInf(case, name, dim, indnt):

    print("\t" * (indnt-1) + f"Case: {case + 1}")
    print()

    print("\t" * (indnt) + f"Name: {name}")
    print("\t" * (indnt) + f"Dim: {dim}")
    print()


def prntSlope(dim, slopeMat, indnt):

    rowDim, colDim = dim[0], dim[1]
    indntStr = "\t" * indnt

    for r in range(rowDim):
        print(indntStr, end="")

        for c in range(colDim):
            print(f"{slopeMat[r][c]:2}", end=" ")

        print()
    print()


"""__Code__"""


def fndPath(curPos, dim, slopeMat, dstncMat):

    cRw, cCl = curPos[0], curPos[1]
    rwDm, clDm = dim[0], dim[1]

    if dstncMat[cRw][cCl]:
        return dstncMat[cRw][cCl]

    mvs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    maxDstnc = 1

    for mvR, mvC in mvs:
        nRw, nCl = cRw + mvR, cCl + mvC
        nxtPos = [nRw, nCl]

        if canGo(curPos, nxtPos, dim, slopeMat):

            dstnc = 1 + fndPath(nxtPos, dim, slopeMat, dstncMat)

            maxDstnc = max(dstnc, maxDstnc)

    dstncMat[cRw][cCl] = maxDstnc

    return maxDstnc


def canGo(curPos, nxtPos, dim, slopeMat):

    cRw, cCl = curPos[0], curPos[1]
    nRw, nCl = nxtPos[0], nxtPos[1]
    rwDm, clDm = dim[0], dim[1]

    return 0 <= nRw < rwDm and 0 <= nCl < clDm and slopeMat[nRw][nCl] < slopeMat[cRw][cCl]


def dataExtract():

    # caseNum = int(InLines.pop(0))
    caseNum = int(input())

    lstName = []
    lstDim = []
    lstSlopeMat = []

    for case in range(caseNum):

        infLine = input()

        name = infLine.split()[0]
        dim = list(map(int, infLine.split()[1:]))
        slopeMat = []

        for _ in range(dim[0]):

            lineStr = input()
            line = list(map(int, lineStr.split()))

            slopeMat.append(line)

        lstName.append(name)
        lstDim.append(dim)
        lstSlopeMat.append(slopeMat)

    return caseNum, lstName, lstDim, lstSlopeMat


def getMax(dim, dstncMat):

    rowDim, colDim = dim[0], dim[1]

    maxDstnc = 0

    for r in range(rowDim):
        for c in range(colDim):

            maxDstnc = max(dstncMat[r][c], maxDstnc)

    return maxDstnc


if __name__ == '__main__':

    # print("Input:")
    # print(InputOrg_Raw)
    # print()

    # InLines = InputRaw.split("\n")

    caseNum, lstName, lstDim, lstSlopeMat = dataExtract()

    # print(f"\tCases: {caseNum}")
    # print()

    for case in range(caseNum):

        name = lstName[case]
        dim = lstDim[case]

        # prntInf(case, name, dim, 3)

        rowDim, colDim = dim[0], dim[1]

        slopeMat = lstSlopeMat[case]
        dstncMat = [[0] * colDim for _ in range(rowDim)]

        # print(f"\t\t\t  Slope:")
        # prntSlope(dim, slopeMat, 4)

        for r in range(rowDim):
            for c in range(colDim):

                fndPath([r, c], dim, slopeMat, dstncMat)

        # print(f"\t\t\t\t  Distances:")
        # prntSlope(dim, dstncMat, 5)

        maxDstnc = getMax(dim, dstncMat)

        # print(f"\t\t\tMax distance: {maxDstnc}")
        print(f"{name}: {maxDstnc}")

        # if (case+1) < caseNum:
        #     print("\n")

