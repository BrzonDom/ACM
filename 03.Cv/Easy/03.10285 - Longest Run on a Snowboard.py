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


def findPath(curPos, dim, slopeMat, dstncMat):

    cRw, cCl = curPos[0], curPos[1]
    rwDm, clDm = dim[0], dim[1]

    if dstncMat[cRw][cCl]:
        return dstncMat[cRw][cCl]

    mvs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    maxDstnc = 0

    for mvR, mvC in mvs:
        nRw, nCl = cRw + mvR, cCl + mvC
        nxtPos = [nRw, nCl]

        if canGo(curPos, nxtPos, dim, slopeMat):

            maxDstnc = max(maxDstnc, 1 + findPath(nxtPos, dim, slopeMat, dstncMat))

    dstncMat[cRw][cCl] = maxDstnc

    return maxDstnc


def canGo(curPos, nxtPos, dim, slopeMat):

    cRw, cCl = curPos[0], curPos[1]
    nRw, nCl = nxtPos[0], nxtPos[1]
    rwDm, clDm = dim[0], dim[1]

    return 0 <= nRw < rwDm and 0 <= nCl < clDm and slopeMat[nRw][nCl] < slopeMat[cRw][cCl]


InputRaw_Str = """
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

InputRaw_Str = InputRaw_Str[1:-1]

if __name__ == '__main__':

    print("Input:")
    print(InputRaw_Str)
    print()

    InputLines = InputRaw_Str.split("\n")

    caseNum = int(InputLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    for case in range(caseNum):

        print(f"\t\tCase: {case+1}")
        print()

        infLine = InputLines.pop(0)

        name = infLine.split()[0]
        dim = list(map(int, infLine.split()[1:]))

        print(f"\t\t\tName: {name}")
        print(f"\t\t\tDim: {dim}")
        print()

        rowDim, colDim = dim[0], dim[1]

        slopeMat = []
        dstncMat = [[0] * colDim for _ in range(rowDim)]

        for r in range(rowDim):

            rowStr = InputLines.pop(0)
            # print(f"\t\t\t{rowStr}")

            row = list(map(int, rowStr.split()))
            slopeMat.append(row)
        # print()

        # strHgh = 0
        # strCrd = []

        for r in range(rowDim):
            print(f"\t\t\t\t", end="")
            for c in range(colDim):
                print(f"{slopeMat[r][c]:2}", end=" ")

                # if slopeMat[r][c] > strHgh:
                #     strHgh = slopeMat[r][c]
                #     strCrd = [r, c]
            print()
        print()

        # print(f"\t\t\tStart: {strCrd}")
        # print()

        for r in range(rowDim):
            for c in range(colDim):

                findPath([r, c], dim, slopeMat, dstncMat)

                # print(f"\t\t\t{[r, c]}: {path[str((r, c))]}")

        maxDstnc = 0

        print(f"\t\t\t\tDistances:")
        for r in range(rowDim):
            print(f"\t\t\t\t\t", end="")
            for c in range(colDim):

                dstncMat[r][c] += 1
                print(f"{dstncMat[r][c]:2}", end=" ")

                if dstncMat[r][c] > maxDstnc:
                    maxDstnc = dstncMat[r][c]
            print()
        print()

        print(f"\t\t\tMax distance: {maxDstnc}")

        if (case+1) < caseNum:
            print("\n")


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

Process finished with exit code 0

"""
