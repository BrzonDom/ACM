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

InputTst_Raw = """
15
M1 3 4
97 3 66 42
29 41 80 10
66 4 67 99
M2 10 10
93 80 11 59 95 54 92 20 2 50
3 55 44 26 71 23 10 33 27 76
76 22 83 21 33 48 92 66 12 36
55 4 15 66 29 76 86 87 63 55
36 32 76 47 58 47 70 68 80 63
44 21 52 26 8 85 41 100 16 19
2 71 91 17 2 86 60 88 73 22
8 75 54 85 21 78 98 58 11 77
87 21 65 38 14 39 89 55 5 4
40 7 75 30 91 77 16 50 31 55
M3 3 1
96
58
90
M4 1 5
87 41 13 30 27
M5 3 2
66 48
100 54
69 4
M6 3 4
11 100 5 2
43 88 18 74
8 23 79 4
M7 10 7
88 83 55 28 96 85 21
29 45 87 44 11 7 12
15 32 21 27 31 94 96
74 47 80 13 56 2 93
60 50 27 47 32 82 75
94 33 62 89 44 49 32
55 22 45 37 54 32 30
51 25 25 92 39 71 4
95 74 97 54 23 23 67
21 72 41 14 71 69 2
M8 4 10
35 2 5 46 39 25 78 69 43 70
60 34 8 97 38 2 70 1 22 59
91 89 46 62 96 26 99 64 29 46
48 30 14 19 42 53 45 19 88 54
M9 8 1
88
63
9
25
31
46
26
19
M10 4 8
7 17 45 69 43 10 33 38
22 47 34 36 66 76 55 77
96 42 30 16 21 17 80 97
9 77 42 1 97 13 18 3
M11 10 9
39 39 6 72 78 28 85 11 64
16 54 18 94 15 26 90 31 13
74 10 9 49 54 52 50 50 31
69 19 27 65 58 66 71 96 43
99 80 21 28 97 75 46 56 90
38 11 20 51 85 98 26 33 51
78 84 0 75 18 86 1 49 44
68 19 39 77 17 19 98 45 82
72 57 37 27 61 48 14 11 100
11 37 32 62 82 82 28 56 66
M12 4 10
14 57 92 100 63 68 16 82 32 27
63 70 50 66 98 10 13 11 88 12
89 92 11 50 39 59 44 61 25 23
85 5 47 76 5 9 10 88 57 42
M13 10 4
78 31 51 75
8 30 52 62
9 40 53 20
56 92 79 100
53 70 90 37
42 36 80 47
45 56 34 68
98 82 19 75
80 70 16 88
66 68 49 75
M14 5 4
61 30 60 6
97 12 76 86
16 17 21 62
30 32 17 31
66 14 12 85
M15 3 8
20 37 45 86 72 61 27 46
29 88 76 55 94 72 34 36
23 50 19 44 11 50 42 95
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputTst_Raw = InputTst_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputTst_Raw]


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


def dataExtract(InLines):

    caseNum = int(InLines.pop(0))

    lstName = []
    lstDim = []
    lstSlopeMat = []

    for case in range(caseNum):

        infLine = InLines.pop(0)

        name = infLine.split()[0]
        dim = list(map(int, infLine.split()[1:]))
        slopeMat = []

        for _ in range(dim[0]):

            lineStr = InLines.pop(0)
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


InputRaw = InputRaw_Lst[0]

if __name__ == '__main__':

    print("Input:")
    print(InputRaw)
    print()

    OutputLst = []

    InLines = InputRaw.split("\n")

    caseNum, lstName, lstDim, lstSlopeMat = dataExtract(InLines)

    print(f"\tCases: {caseNum}")
    print()

    for case in range(caseNum):

        name = lstName[case]
        dim = lstDim[case]

        prntInf(case, name, dim, 3)

        rowDim, colDim = dim[0], dim[1]

        slopeMat = lstSlopeMat[case]
        dstncMat = [[0] * colDim for _ in range(rowDim)]

        print(f"\t\t\t  Slope:")
        prntSlope(dim, slopeMat, 4)

        for r in range(rowDim):
            for c in range(colDim):

                fndPath([r, c], dim, slopeMat, dstncMat)

        print(f"\t\t\t\t  Distances:")
        prntSlope(dim, dstncMat, 5)

        maxDstnc = getMax(dim, dstncMat)

        print(f"\t\t\tMax distance: {maxDstnc}")

        OutputLst.append(f"{name}: {maxDstnc}")

        if (case+1) < caseNum:
            print("\n")

    print("\n")
    print("__Output__:\n")

    for out in OutputLst:
        print(out)


"""__Output__"""
"""
Input:
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

	Cases: 2

		Case: 1

			Name: Feldberg
			Dim: [10, 5]

			  Slope:
				56 14 51 58 88 
				26 94 24 39 41 
				24 16  8 51 51 
				76 72 77 43 10 
				38 50 59 84 81 
				 5 23 37 71 77 
				96 10 93 53 82 
				94 15 96 69  9 
				74  0 62 38 96 
				37 54 55 82 38 

				  Distances:
					 5  1  3  4  5 
					 4  5  2  3  4 
					 3  2  1  4  5 
					 5  4  5  2  1 
					 2  3  4  7  6 
					 1  2  3  4  5 
					 4  1  4  1  6 
					 3  2  5  2  1 
					 2  1  4  1  2 
					 1  2  3  4  1 

			Max distance: 7


		Case: 2

			Name: Spiral
			Dim: [5, 5]

			  Slope:
				 1  2  3  4  5 
				16 17 18 19  6 
				15 24 25 20  7 
				14 23 22 21  8 
				13 12 11 10  9 

				  Distances:
					 1  2  3  4  5 
					16 17 18 19  6 
					15 24 25 20  7 
					14 23 22 21  8 
					13 12 11 10  9 

			Max distance: 25


__Output__:

Feldberg: 7
Spiral: 25

Process finished with exit code 0

"""
