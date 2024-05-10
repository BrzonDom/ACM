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

InputOrg_Raw = InputOrg_Raw[1:-1]
InputTst1_Raw = InputTst1_Raw[1:-1]
InputTst2_Raw = InputTst2_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputTst1_Raw, InputTst2_Raw]

InputRaw = InputRaw_Lst[2]


class Walk:
    def __init__(self, pos, dstnc, vstd, prvWlk):
        self.pos = pos
        self.dstnc = dstnc
        self.vstd = vstd
        self.prvWlk = prvWlk


def fndPath_Rec(cWlk, dim, city):

    cPos = cWlk.pos
    cRw, cCl = cPos[0], cPos[1]

    rwDm, clDm = dim[0], dim[1]

    if [cRw, cCl] == [rwDm - 1, clDm - 1]:
        cWlk.dstnc += 1

        return cWlk

    mvs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for mvR, mvC in mvs:
        nRw = cRw + mvR
        nCl = cCl + mvC
        nPos = (nRw, nCl)

        if 0 <= nRw < rwDm and 0 <= nCl < clDm and nPos not in cWlk.vstd and city[nRw][nCl]:

            nDstnc = cWlk.dstnc + 1
            nVstd = cWlk.vstd
            nVstd.append(nPos)

            nWlk = Walk(nPos, nDstnc, nVstd, cWlk)

            return fndPath_Rec(nWlk, dim, city)


if __name__ == '__main__':

    print("Input:")
    print(InputRaw)
    print()

    InputLines = InputRaw.split("\n")
    # print(InputLines)

    caseNum = int(InputLines.pop(0))
    # print(InputLines)

    print(f"\tCases: {caseNum}")
    print()

    for case in range(caseNum):

        InputLines.pop(0)

        print(f"\t\tCase: {case+1}")
        print()

        dimRow, dimCol = list(map(int, InputLines.pop(0).split()))

        print(f"\t\t\tEast-West:   {dimRow}")
        print(f"\t\t\tNorth-South: {dimCol}")
        print()

        cross = {}

        for row in range(dimRow):
            strt = list(map(int, InputLines.pop(0).split()))

            cross[row+1] = strt[1:]

            if strt[1:]:
                print(f"\t\t\t\t{row+1}.Street: {strt[1:]}")
        print()

        city = [[1 for c in range(dimCol)] for r in range(dimRow)]

        for row in cross:
            for col in cross[row]:

                city[row-1][col-1] = 0

        for row in city:
            print(f"\t\t\t\t  {row}")
        print()

            # Walk(self, pos, dstnc, vstd, prvWlk)
        strWlk = Walk((0, 0), 0, [(0, 0)], None)

            # fndPath_Rec(cWlk, dim, city)
        endWlk = fndPath_Rec(strWlk, (dimRow, dimCol), city)

        print(f"\t\t\tDistance: {endWlk.dstnc}")
        print("\t\t\tPath:", end="\n\t\t\t\t")

        for p, pth in enumerate(endWlk.vstd):
            print(pth, end=" ")

            if (p+1) % 5 == 0 and (p+1) != endWlk.dstnc:
                print("\n\t\t\t\t", end="")
        print()

        # for path in minPaths:
        #     print(f"\t\t\t\t{path}")
        # print()

        if (case+1) < caseNum:
            print()


"""__Output__"""
"""
Input:
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

	Cases: 2

		Case: 1

			East-West:   4
			North-South: 5

				2.Street: [2]
				3.Street: [3, 5]

				  [1, 1, 1, 1, 1]
				  [1, 0, 1, 1, 1]
				  [1, 1, 0, 1, 0]
				  [1, 1, 1, 1, 1]

			Distance: 8
			Path:
				(0, 0) (1, 0) (2, 0) (3, 0) (3, 1) 
				(3, 2) (3, 3) (3, 4) 

		Case: 2

			East-West:   8
			North-South: 8

				3.Street: [5]
				4.Street: [1, 4]
				5.Street: [3, 6]
				6.Street: [2, 7]
				7.Street: [8]

				  [1, 1, 1, 1, 1, 1, 1, 1]
				  [1, 1, 1, 1, 1, 1, 1, 1]
				  [1, 1, 1, 1, 0, 1, 1, 1]
				  [0, 1, 1, 0, 1, 1, 1, 1]
				  [1, 1, 0, 1, 1, 0, 1, 1]
				  [1, 0, 1, 1, 1, 1, 0, 1]
				  [1, 1, 1, 1, 1, 1, 1, 0]
				  [1, 1, 1, 1, 1, 1, 1, 1]

			Distance: 17
			Path:
				(0, 0) (1, 0) (2, 0) (2, 1) (3, 1) 
				(4, 1) (4, 0) (5, 0) (6, 0) (7, 0) 
				(7, 1) (7, 2) (7, 3) (7, 4) (7, 5) 
				(7, 6) (7, 7) 

Process finished with exit code 0

"""