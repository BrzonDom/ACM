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

        strRow, strCol = list(map(int, InputLines.pop(0).split()))

        print(f"\t\t\tEast-West:   {strRow}")
        print(f"\t\t\tNorth-South: {strCol}")
        print()

        cross = {}

        for row in range(strRow):
            strt = list(map(int, InputLines.pop(0).split()))

            cross[row+1] = strt[1:]

            if strt[1:]:
                print(f"\t\t\t\t{row+1}.Street: {strt[1:]}")
        print()

        city = [[1 for c in range(strCol)] for r in range(strRow)]

        for row in cross:
            for col in cross[row]:

                city[row-1][col-1] = 0

        for row in city:
            print(f"\t\t\t\t  {row}")
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


Process finished with exit code 0

"""