"""
BUSYMAN - I AM VERY BUSY
https://www.spoj.com/problems/BUSYMAN/

    In the given figure, if you go to date with crush, you cannot participate in the coding contest
    and you can’t watch the movie. Also if you play DotA, you can’t study for the exam. If you study
    for the exam you can’t sleep peacefully. The maximum number of activities that you can do for
    this schedule is 3.
    Either you can
      -  watch movie, play DotA and sleep peacefully (or)
      -  date with crush, play DotA and sleep peacefully

    Input:
            The first line consists of an integer T, the number of test cases. For each test case the
        first line consists of an integer N, the number of activities. Then the next N lines contains
        two integers m and n, the start and end time of each activity.

    Output:
            For each test case find the maximum number of activities that you can do.

    Constraints:
        1 <= T <=10
        1 <= N <= 100000
        0 <= start < end <= 1000000


    Sample:
        3
        3
        3 9
        2 8
        6 9
        4
        1 7
        5 8
        7 8
        1 8
        6
        7 9
        0 10
        4 5
        8 9
        4 10
        5 7
            =>  1
                2
                3

"""
import copy

InputRaw_Str = """
3
3
3 9
2 8
6 9
4
1 7
5 8
7 8
1 8
6
7 9
0 10
4 5
8 9
4 10
5 7
"""

InputRaw_Str = InputRaw_Str[1:-1]

print("Input:")
print(InputRaw_Str)
print()

InputStr_Lst = InputRaw_Str.split("\n")
# print(InputStr_Lst)
# print()

InputOrg_Lst = copy.deepcopy(InputStr_Lst)

caseNum = int(InputStr_Lst.pop(0))

for case in range(caseNum):

    actNum = int(InputStr_Lst.pop(0))

    print(f"\tAct. num.: {actNum}")
    print()

    actTimes = []

    for act in range(actNum):

        actTimes.append(tuple(map(int, InputStr_Lst.pop(0).split())))
        print(f"\t\t{act+1}. {actTimes[-1]}")

    print()

    freeAct = {}
    freeMss = {}
    freeCnt = {}

    for curTm in actTimes:

        freeAct[curTm] = []
        freeMss[curTm] = []
        freeCnt[curTm] = 1

        for nxtTm in actTimes:

            if curTm == nxtTm:
                continue

            elif nxtTm[0] >= curTm[1] or nxtTm[1] <= curTm[0]:

                freeCnt[curTm] += 1
                freeAct[curTm] += [nxtTm]

            else:
                freeMss[curTm] += [nxtTm]

        # print(f"\t\t{str(curTm):8} [{freeCnt[curTm]}] : {freeAct[curTm]}")

        print(f"\t\tActiv.: {curTm}")
        print(f"\t\t\tActiv. count  : {freeCnt[curTm]}")
        print(f"\t\t\tActiv. free   : {freeAct[curTm]}")
        print(f"\t\t\tActiv. missed : {freeMss[curTm]}")
        print()

    # print()

    # allAct = {}
    #
    # for curTm in actTimes:
    #
    #     allAct[curTm] = [curTm]
    #
    #     for nxtTm in freeAct[curTm]:
    #
    #         if nxtTm not in allAct[curTm]:
    #             allAct[curTm] += [nxtTm]
    #
    #     print(f"\t\t{allAct[curTm]}")

    print("\n")


"""__Output__"""
"""
Input:
3
3
3 9
2 8
6 9
4
1 7
5 8
7 8
1 8
6
7 9
0 10
4 5
8 9
4 10
5 7

	Act. num.: 3

		1. (3, 9)
		2. (2, 8)
		3. (6, 9)

		Activ.: (3, 9)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(2, 8), (6, 9)]

		Activ.: (2, 8)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(3, 9), (6, 9)]

		Activ.: (6, 9)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(3, 9), (2, 8)]



	Act. num.: 4

		1. (1, 7)
		2. (5, 8)
		3. (7, 8)
		4. (1, 8)

		Activ.: (1, 7)
			Activ. count  : 2
			Activ. free   : [(7, 8)]
			Activ. missed : [(5, 8), (1, 8)]

		Activ.: (5, 8)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(1, 7), (7, 8), (1, 8)]

		Activ.: (7, 8)
			Activ. count  : 2
			Activ. free   : [(1, 7)]
			Activ. missed : [(5, 8), (1, 8)]

		Activ.: (1, 8)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(1, 7), (5, 8), (7, 8)]



	Act. num.: 6

		1. (7, 9)
		2. (0, 10)
		3. (4, 5)
		4. (8, 9)
		5. (4, 10)
		6. (5, 7)

		Activ.: (7, 9)
			Activ. count  : 3
			Activ. free   : [(4, 5), (5, 7)]
			Activ. missed : [(0, 10), (8, 9), (4, 10)]

		Activ.: (0, 10)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(7, 9), (4, 5), (8, 9), (4, 10), (5, 7)]

		Activ.: (4, 5)
			Activ. count  : 4
			Activ. free   : [(7, 9), (8, 9), (5, 7)]
			Activ. missed : [(0, 10), (4, 10)]

		Activ.: (8, 9)
			Activ. count  : 3
			Activ. free   : [(4, 5), (5, 7)]
			Activ. missed : [(7, 9), (0, 10), (4, 10)]

		Activ.: (4, 10)
			Activ. count  : 1
			Activ. free   : []
			Activ. missed : [(7, 9), (0, 10), (4, 5), (8, 9), (5, 7)]

		Activ.: (5, 7)
			Activ. count  : 4
			Activ. free   : [(7, 9), (4, 5), (8, 9)]
			Activ. missed : [(0, 10), (4, 10)]




Process finished with exit code 0

"""