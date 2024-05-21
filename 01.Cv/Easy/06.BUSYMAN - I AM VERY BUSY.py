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


# class Act:
#     def __init__(self, tm, ct, fr, ms):
#         self.tm = tm
#         self.ct = ct
#         self.fr = fr
#         self.ms = ms
#
#     def addFr(self, nxtFr):
#         self.fr.append(nxtFr)
#
#     def addMs(self, nxtMs):
#         self.ms.append(nxtMs)


class Table:
    def __init__(self, sch, cnt, frAct, msAct):
        self.sch = sch
        self.cnt = cnt
        self.frAct = frAct
        self.msAct = msAct


def dataRead_Prt(InLines):

    actNum = int(InLines.pop(0))

    print(f"\t\t\tAct. num.: {actNum}")
    print()

    print("\t\t\tActivities:")

    actTimes = []

    for act in range(actNum):
        actTimes.append(tuple(map(int, InLines.pop(0).split())))

        print(f"\t\t\t\t{act + 1}. {actTimes[-1]}")
    print()

    return actTimes, actNum


def dataRead(InLines):

    actNum = int(InLines.pop(0))

    # print(f"\t\t\tAct. num.: {actNum}")
    # print()
    #
    # print("\t\t\tActivities:")

    actTimes = []

    for act in range(actNum):
        actTimes.append(tuple(map(int, InLines.pop(0).split())))

    #     print(f"\t\t\t\t{act + 1}. {actTimes[-1]}")
    # print()

    return actTimes, actNum


def actExtract_Prt(actTimes):

    # ActLst = []

    frdActs = {}
    msdActs = {}

    for curTm in actTimes:

        # curAct = Act(curTm, 0, [], [])

        frdActs[curTm] = []
        msdActs[curTm] = []

        for nxtTm in actTimes:

            if curTm == nxtTm:
                continue

            elif nxtTm[0] >= curTm[1] or nxtTm[1] <= curTm[0]:
                # curAct.ct += 1
                # curAct.addFr(nxtTm)

                frdActs[curTm].append(nxtTm)

            else:
                # curAct.addMs(nxtTm)

                msdActs[curTm].append(nxtTm)

        # ActLst.append(curAct)

        print(f"\t\t\t\tActiv.: {curTm}")
        print(f"\t\t\t\t\tActiv. count  : {len(frdActs[curTm])}")
        print(f"\t\t\t\t\tActiv. free   : {frdActs[curTm]}")
        print(f"\t\t\t\t\tActiv. missed : {msdActs[curTm]}")
        print()

    # return ActLst, frdActs, msdActs
    return frdActs, msdActs


def actExtract(actTimes):

    # ActLst = []

    frdActs = {}
    msdActs = {}

    for curTm in actTimes:

        # curAct = Act(curTm, 0, [], [])

        frdActs[curTm] = []
        msdActs[curTm] = []

        for nxtTm in actTimes:

            if curTm == nxtTm:
                continue

            elif nxtTm[0] >= curTm[1] or nxtTm[1] <= curTm[0]:
                # curAct.ct += 1
                # curAct.addFr(nxtTm)

                frdActs[curTm].append(nxtTm)

            else:
                # curAct.addMs(nxtTm)

                msdActs[curTm].append(nxtTm)

        # ActLst.append(curAct)

    # return ActLst, frdActs, msdActs
    return frdActs, msdActs


def actSort_Prt(actTimes):

    actTimes.sort(key=lambda tm: tm[1])

    actNum = len(actTimes)

    print(f"\t\t\tAct. num.: {actNum}")
    print()

    print("\t\t\tActivities:")

    for a, act in enumerate(actTimes):

        print(f"\t\t\t\t{a+1}. {act}")
    print()

    return actTimes


def fndMaxTable_BFS(curTbl, maxTbl):

    for nxtTm in curTbl.frAct:

        nxtSch = curTbl.sch + [nxtTm]
        nxtCnt = curTbl.cnt + 1
        nxtMsd = list(set(curTbl.msAct) | set(msdActs[nxtTm]))
        nxtFrd = list(set(curTbl.frAct) & set(frdActs[nxtTm]))

        if maxTbl.cnt > nxtCnt + len(nxtFrd):
            return maxTbl

        nxtTbl = Table(nxtSch, nxtCnt, nxtFrd, nxtMsd)

        # print(f"\t\t\t\t\tSched.: {nxtSch}")
        # print(f"\t\t\t\t\t\tActiv. count  : {nxtCnt}")
        # print(f"\t\t\t\t\t\tActiv. free   : {nxtFrd}")
        # print(f"\t\t\t\t\t\tActiv. missed : {nxtMsd}")
        # print()

        return fndMaxTable_BFS(nxtTbl, maxTbl)

    if curTbl.cnt > maxTbl.cnt:
        maxTbl = curTbl

    return maxTbl


if __name__ == "__main__":

    print("Input:")
    print(InputRaw_Str)
    print()

    InLines = InputRaw_Str.split("\n")

    caseNum = int(InLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    for case in range(caseNum):

        print(f"\t\t{case+1}. Case")
        print()

        actTimes, actNum = dataRead(InLines)

        # ActLst, frdActs, msdActs = actExtract_Prt(actTimes)
        frdActs, msdActs = actExtract(actTimes)

        actTimes = actSort_Prt(actTimes)

        maxTbl = Table([], 0, None, None)

        for curAct in actTimes:

            print(f"\t\t\t\tActiv.: {curAct}")
            # print(f"\t\t\t\t\tActiv. count  : {curAct.ct}")
            print(f"\t\t\t\t\tActiv. free   : {frdActs[curAct]}")
            print(f"\t\t\t\t\tActiv. missed : {msdActs[curAct]}")
            print()

            curTbl = Table([curAct], 1, frdActs[curAct], msdActs[curAct])

            maxTbl = fndMaxTable_BFS(curTbl, maxTbl)

        print()

        print(f"\t\t\tMax Table:")
        print(f"\t\t\t\tSched.: {maxTbl.sch}")
        print(f"\t\t\t\tActiv. count: {maxTbl.cnt}")
        # print(f"\t\t\t\tActiv. free   : {maxTbl.frAct}")
        # print(f"\t\t\t\tActiv. missed : {maxTbl.msAct}")

        if (case+1) < caseNum:
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

	Cases: 3

		1. Case

			Act. num.: 3

			Activities:
				1. (2, 8)
				2. (3, 9)
				3. (6, 9)

				Activ.: (2, 8)
					Activ. free   : []
					Activ. missed : [(3, 9), (6, 9)]

				Activ.: (3, 9)
					Activ. free   : []
					Activ. missed : [(2, 8), (6, 9)]

				Activ.: (6, 9)
					Activ. free   : []
					Activ. missed : [(3, 9), (2, 8)]


			Max Table:
				Sched.: [(2, 8)]
				Activ. count: 1


		2. Case

			Act. num.: 4

			Activities:
				1. (1, 7)
				2. (5, 8)
				3. (7, 8)
				4. (1, 8)

				Activ.: (1, 7)
					Activ. free   : [(7, 8)]
					Activ. missed : [(5, 8), (1, 8)]

				Activ.: (5, 8)
					Activ. free   : []
					Activ. missed : [(1, 7), (7, 8), (1, 8)]

				Activ.: (7, 8)
					Activ. free   : [(1, 7)]
					Activ. missed : [(5, 8), (1, 8)]

				Activ.: (1, 8)
					Activ. free   : []
					Activ. missed : [(1, 7), (5, 8), (7, 8)]


			Max Table:
				Sched.: [(1, 7), (7, 8)]
				Activ. count: 2


		3. Case

			Act. num.: 6

			Activities:
				1. (4, 5)
				2. (5, 7)
				3. (7, 9)
				4. (8, 9)
				5. (0, 10)
				6. (4, 10)

				Activ.: (4, 5)
					Activ. free   : [(7, 9), (8, 9), (5, 7)]
					Activ. missed : [(0, 10), (4, 10)]

				Activ.: (5, 7)
					Activ. free   : [(7, 9), (4, 5), (8, 9)]
					Activ. missed : [(0, 10), (4, 10)]

				Activ.: (7, 9)
					Activ. free   : [(4, 5), (5, 7)]
					Activ. missed : [(0, 10), (8, 9), (4, 10)]

				Activ.: (8, 9)
					Activ. free   : [(4, 5), (5, 7)]
					Activ. missed : [(7, 9), (0, 10), (4, 10)]

				Activ.: (0, 10)
					Activ. free   : []
					Activ. missed : [(7, 9), (4, 5), (8, 9), (4, 10), (5, 7)]

				Activ.: (4, 10)
					Activ. free   : []
					Activ. missed : [(7, 9), (0, 10), (4, 5), (8, 9), (5, 7)]


			Max Table:
				Sched.: [(4, 5), (7, 9), (5, 7)]
				Activ. count: 3

Process finished with exit code 0

"""