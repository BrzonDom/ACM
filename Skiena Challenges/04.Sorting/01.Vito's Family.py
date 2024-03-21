"""

Vito's Family

    The famous gangster Vito Deadstone is moving to New York. He has a very big
    family there, all of them living on Lamafia Avenue. Since he will visit all his relatives
    very often, he wants to find a house close to them.
    Indeed, Vito wants to minimize the total distance to all of his relatives and has
    blackmailed you to write a program that solves his problem.

    Input:
        The input consists of several test cases. The first line contains the number of test cases.
        For each test case you will be given the integer number of relatives r (0 < r < 500) and
        the street numbers (also integers) s_1, s_2, ..., s_i, ..., s_r where they live (0 < si < 30, 000).
        Note that several relatives might live at the same street number.

    Output:
        For each test case, your program must write the minimal sum of distances from the
        optimal Vito’s house to each one of his relatives. The distance between two street
        numbers s_i and s_j is d_ij = |s_i − s_j|.


    Sample:

        2
        2 2 4
        3 2 4 6
            =>  2
                4

"""

InputRaw_Str = """
2
2 2 4
3 2 4 6
"""

Cases = int(InputRaw_Str[1])

for case in range(Cases):
    Input_Str = InputRaw_Str.split("\n")[case+2]
    Input = list(map(int, Input_Str.split()))

    print(f"Input: {Input}\n")

    RelatNum = Input[0]
    HousLst = Input[1:]

    print(f"\tRelatives: {RelatNum}")
    print(f"\tHouse numbers: {HousLst}")
    print()

    HousLst = sorted(HousLst)

    if RelatNum % 2 == 0:
        Median = HousLst[RelatNum // 2 - 1] + HousLst[RelatNum // 2]

        Median = Median / 2
        print(f"\t\tMedian: {Median}")
        # print(f"\t\t\t")

    else:
        Median = HousLst[(RelatNum - 1) // 2]
        print(f"\t\tMedian: {Median}")

    print("\n")