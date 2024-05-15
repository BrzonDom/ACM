"""
825 - Walking on the Safe Side
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=766

        Square City is a very easy place for people to walk around. The two-way streets run North-South or
    East-West dividing the city into regular blocks. Most street intersections are safe for pedestrians to
    cross. In some of them, however, crossing is not safe and pedestrians are forced to use the available
    underground passages. Such intersections are avoided by walkers. The entry to the city park is on the
    North-West corner of town, whereas the railway station is on the South-East corner.
        Suppose you want to go from the park to the railway station, and do not want to walk more than
    the required number of blocks. You also want to make your way avoiding the underground passages,
    that would introduce extra delay. Your task is to determine the number of different paths that you can
    follow from the park to the station, satisfying both requirements.

    Input:
            The input begins with a single positive integer on a line by itself indicating the number
        of the cases following, each of them as described below. This line is followed by a blank
        line, and there is also a blank line between two consecutive inputs.
            The first line of the input contains the number of East-West streets W and the number of North-
        South streets N . Each one of the following W lines starts with the number of an East-West street,
        followed by zero or more numbers of the North-South crossings which are unsafe. Streets are numbered
        from 1.

    Output:
            For each test case, the output must follow the description below. The outputs of two
        consecutive cases will be separated by a blank line.
        The number of different minimal paths from the park to the station avoiding underground passages.


    Sample:
        1

        4 5
        1
        2 2
        3 3 5
        4
            =>  4

"""

InputOrg_Raw = """
1

4 5
1
2 2
3 3 5
4
"""

InputTst1_Raw = """
8

1 1
1

1 8
1

1 8
1 4

8 1
1
2
3
4
5
6
7
8

8 1
1
2
3
4 1
5
6
7
8

4 4
1
2
3
4

8 8
1
2
3 5
4 1 4
5 3 6
6 2 7
7 8
8

8 8
1
2 6
3 2
4 5
5 1
6 3
7 5 8
8 5

"""

InputTst2_Raw = """
2

4 5
1
2 2
3 3 5
4

8 8
1
2
3 5
4 1 4
5 3 6
6 2 7
7 8
8
"""

InputTst3_Raw = """
1

8 8
1
2
3 5
4 1 4
5 3 6
6 2 7
7 8
8
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputTst1_Raw = InputTst1_Raw[1:-1]
InputTst2_Raw = InputTst2_Raw[1:-1]
InputTst3_Raw = InputTst3_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputTst1_Raw, InputTst2_Raw, InputTst3_Raw]

InputRaw = InputRaw_Lst[1]


def dataAllExtract_Prt(InputRaw):

    InputLines = InputRaw.split("\n")

    caseNum = int(InputLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    caseLst = []

    for case in range(caseNum):
        InputLines.pop(0)

        dimLine = InputLines.pop(0)
        dimRow, dimCol = list(map(int, dimLine.split()))

        city = [[1 for c in range(dimCol)] for r in range(dimRow)]

        for row in range(dimRow):

            strt = list(map(int, InputLines.pop(0).split()))

            for col in strt[1:]:
                city[row][col-1] = 0

        caseLst.append(((dimRow, dimCol), city))

    return caseNum, caseLst


def prntCity(city):
    # ⬜⬛

    print("\t\t\tCity:", end="")

    for row in city:
        print(f"\n\t\t\t\t", end="")
        for col in row:
            if col:
                print("⬜", end="")
            else:
                print("⬛", end="")
    print("\n")


def fndPathAll_Rec(cWlk, dim, city):

    cPos = cWlk.pos
    cRw, cCl = cPos[0], cPos[1]

    rwDm, clDm = dim[0], dim[1]

    if cPos == (rwDm - 1, clDm - 1):

        return cWlk

    mvs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for mvR, mvC in mvs:
        nRw = cRw + mvR
        nCl = cCl + mvC
        nPos = (nRw, nCl)

        if 0 <= nRw < rwDm and 0 <= nCl < clDm and nPos not in cWlk.pth and city[nRw][nCl]:

            nDst = cWlk.dst + 1
            nPth = cWlk.pth + [nPos]

            nWlk = Walk(nPos, nDst, nPth, cWlk)

            return fndPathAll_Rec(nWlk, dim, city)


def findPathAll_Iter(dim, city):

    rwDm, clDm = dim[0], dim[1]

    minDstnc = 0

        # Walk(self, pos, dstnc, pth, prv)
    strWlk = Walk((0, 0), 0, [(0, 0)], None)

    queuWlk = [[strWlk], []]

    while queuWlk[0]:

        cWlk = queuWlk[0].pop(0)

        cPos = cWlk.pos
        cRw, cCl = cPos[0], cPos[1]

        if (cRw, cCl) == (rwDm - 1, clDm - 1):

            allWlk = [cWlk]
            minDstnc = cWlk.dst

            while queuWlk[0]:

                cWlk = queuWlk[0].pop(0)

                cPos = cWlk.pos
                cRw, cCl = cPos[0], cPos[1]

                if (cRw, cCl) == (rwDm - 1, clDm - 1):
                    allWlk.append(cWlk)

            return minDstnc, allWlk

        else:
            mvs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for mvR, mvC in mvs:
                nRw = cRw + mvR
                nCl = cCl + mvC
                nPos = (nRw, nCl)

                if 0 <= nRw < rwDm and 0 <= nCl < clDm and nPos not in cWlk.pth and city[nRw][nCl]:

                    nDst = cWlk.dst + 1
                    nPth = cWlk.pth + [nPos]

                    nWlk = Walk(nPos, nDst, nPth, cWlk)

                    queuWlk[1].append(nWlk)

        if not queuWlk[0]:
            queuWlk = [queuWlk[1], []]

    return minDstnc, False


"""__CODE__"""


class Walk:
    def __init__(self, pos, dstnc, pth, prv):
        self.pos = pos
        self.dst = dstnc
        self.pth = pth
        self.prv = prv


def dataExtract():

    # InputLines.pop(0)
    input()

    # dimLine = InputLines.pop(0)
    dimLine = input()
    dimRow, dimCol = list(map(int, dimLine.split()))

    city = [[1 for c in range(dimCol)] for r in range(dimRow)]

    for row in range(dimRow):

        # strt = list(map(int, InputLines.pop(0).split()))
        strt = list(map(int, input().split()))

        for col in strt[1:]:
            city[row][col - 1] = 0

    return (dimRow, dimCol), city


def findPath_Iter(dim, city):

    rwDm, clDm = dim[0], dim[1]

    maxDstnc = (rwDm-1) + (clDm-1)
    pathCnt = 0

        # Walk(self, pos, dstnc, pth, prv)
    strWlk = Walk((0, 0), 0, [(0, 0)], None)

    queuWlk = [[strWlk], []]

    while queuWlk[0]:

        cWlk = queuWlk[0].pop(0)

        if cWlk.dst > maxDstnc:
            return False, pathCnt

        cPos = cWlk.pos
        cRw, cCl = cPos[0], cPos[1]

        if (cRw, cCl) == (rwDm - 1, clDm - 1):

            allWlk = [cWlk]
            pathCnt = 1

            while queuWlk[0]:

                cWlk = queuWlk[0].pop(0)
                pathCnt += 1

                cPos = cWlk.pos
                cRw, cCl = cPos[0], cPos[1]

                if (cRw, cCl) == (rwDm - 1, clDm - 1):
                    allWlk.append(cWlk)

            return allWlk, pathCnt

        else:
            mvs = [(1, 0), (0, 1)]

            for mvR, mvC in mvs:
                nRw = cRw + mvR
                nCl = cCl + mvC
                nPos = (nRw, nCl)

                if 0 <= nRw < rwDm and 0 <= nCl < clDm and nPos not in cWlk.pth and city[nRw][nCl]:

                    nDst = cWlk.dst + 1
                    nPth = cWlk.pth + [nPos]

                    nWlk = Walk(nPos, nDst, nPth, cWlk)

                    queuWlk[1].append(nWlk)

        if not queuWlk[0]:
            queuWlk = [queuWlk[1], []]

    return False, pathCnt


if __name__ == '__main__':

    # print("Input:")
    # print(InputRaw)
    # print()

    # caseNum, caseLst = dataAllExtract_Prt(InputRaw)
    #
    # for case, infCase in enumerate(caseLst):
    #
    #     print(f"\t\t{case+1}.Case")
    #
    #     dim = infCase[0]
    #     dimRow, dimCol = dim[0], dim[1]
    #
    #     city = infCase[1]

    # InputLines = InputRaw.split("\n")

    # caseNum = int(InputLines.pop(0))
    caseNum = int(input())

    # print(f"\tCases: {caseNum}")
    # print()

    for case in range(caseNum):

        # print(f"\t\t{case+1}.Case")

        dim, city = dataExtract()

        dimRow, dimCol = dim[0], dim[1]

        # print(f"\t\t\tEast-West:   {dimRow}")
        # print(f"\t\t\tNorth-South: {dimCol}")
        # print()

        # prntCity(city)

        # print("\t\t\tFind path recursively:")
        # print()
        #
        #     # Walk(self, pos, dstnc, pth, prv)
        # strWlk = Walk((0, 0), 0, [(0, 0)], None)
        #
        #     # fndPathAll_Rec(cWlk, dim, city)
        # endWlk = fndPathAll_Rec(strWlk, (dimRow, dimCol), city)
        #
        # print(f"\t\t\t\tDistance: {endWlk.dst}")
        # print("\t\t\t\tPath:", end="\n\t\t\t\t\t")
        #
        # for p, pth in enumerate(endWlk.pth):
        #     print(pth, end=" ")
        #
        #     if (p+1) % 5 == 0 and (p+1) != endWlk.dst:
        #         print("\n\t\t\t\t\t", end="")
        # print("\n")

        # print("\t\t\tFind path iteratively:")
        # print()

        #     # findPathAll_Iter(dim, city)
        # minDstnc, allEndWlk = findPathAll_Iter((dimRow, dimCol), city)

        # if allEndWlk:
        #     print(f"\t\t\t\tDistance: {minDstnc}")
        #     print(f"\t\t\t\tPaths: {len(allEndWlk)}")
        #     print()
        # else:
        #     print(f"\t\t\t\tNo path found")
        #     print()

        allEndWlk, pathNum = findPath_Iter((dimRow, dimCol), city)

        if allEndWlk:
            print(pathNum)


            # print(f"\t\t\t\tDistance: {minDstnc}")
            # print(f"\t\t\t\tPaths: {len(allEndWlk)}")
            # print(f"\t\t\t\tPaths: {pathNum}")
            # print()
        else:
            print(0)


            # print(f"\t\t\t\tNo path found")
            # print()

        # for eCnt, endWlk in enumerate(allEndWlk):
        #
        #     # print(f"\t\t\t\tDistance: {endWlk.dst}")
        #     print(f"\t\t\t\t{eCnt+1}.Path:", end="\n\t\t\t\t\t")
        #
        #     for p, pth in enumerate(endWlk.pth):
        #         print(pth, end=" ")
        #
        #         if (p+1) % 10 == 0 and (p+1) != endWlk.dst:
        #             print("\n\t\t\t\t\t", end="")
        #     print()

        if (case+1) < caseNum:
            print()


"""__Output__"""
"""
Input:
8

1 1
1

1 8
1

1 8
1 4

8 1
1
2
3
4
5
6
7
8

8 1
1
2
3
4 1
5
6
7
8

4 4
1
2
3
4

8 8
1
2
3 5
4 1 4
5 3 6
6 2 7
7 8
8

8 8
1
2 6
3 2
4 5
5 1
6 3
7 5 8
8 5


	Cases: 8

		1.Case
			East-West:   1
			North-South: 1

			City:
				⬜

			Find path iteratively:

				Paths: 1


		2.Case
			East-West:   1
			North-South: 8

			City:
				⬜⬜⬜⬜⬜⬜⬜⬜

			Find path iteratively:

				Paths: 1


		3.Case
			East-West:   1
			North-South: 8

			City:
				⬜⬜⬜⬛⬜⬜⬜⬜

			Find path iteratively:

				No path found


		4.Case
			East-West:   8
			North-South: 1

			City:
				⬜
				⬜
				⬜
				⬜
				⬜
				⬜
				⬜
				⬜

			Find path iteratively:

				Paths: 1


		5.Case
			East-West:   8
			North-South: 1

			City:
				⬜
				⬜
				⬜
				⬛
				⬜
				⬜
				⬜
				⬜

			Find path iteratively:

				No path found


		6.Case
			East-West:   4
			North-South: 4

			City:
				⬜⬜⬜⬜
				⬜⬜⬜⬜
				⬜⬜⬜⬜
				⬜⬜⬜⬜

			Find path iteratively:

				Paths: 20


		7.Case
			East-West:   8
			North-South: 8

			City:
				⬜⬜⬜⬜⬜⬜⬜⬜
				⬜⬜⬜⬜⬜⬜⬜⬜
				⬜⬜⬜⬜⬛⬜⬜⬜
				⬛⬜⬜⬛⬜⬜⬜⬜
				⬜⬜⬛⬜⬜⬛⬜⬜
				⬜⬛⬜⬜⬜⬜⬛⬜
				⬜⬜⬜⬜⬜⬜⬜⬛
				⬜⬜⬜⬜⬜⬜⬜⬜

			Find path iteratively:

				No path found


		8.Case
			East-West:   8
			North-South: 8

			City:
				⬜⬜⬜⬜⬜⬜⬜⬜
				⬜⬜⬜⬜⬜⬛⬜⬜
				⬜⬛⬜⬜⬜⬜⬜⬜
				⬜⬜⬜⬜⬛⬜⬜⬜
				⬛⬜⬜⬜⬜⬜⬜⬜
				⬜⬜⬛⬜⬜⬜⬜⬜
				⬜⬜⬜⬜⬛⬜⬜⬛
				⬜⬜⬜⬜⬛⬜⬜⬜

			Find path iteratively:

				Paths: 233


Process finished with exit code 0

"""
