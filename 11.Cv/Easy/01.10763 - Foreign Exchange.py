"""
10763 - Foreign Exchange
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=315&page=show_problem&problem=1704

    Your non-profit organization (iCORE - international Confederation of Revolver Enthusiasts) coor-
    dinates a very successful foreign student exchange program. Over the last few years, demand has
    sky-rocketed and now you need assistance with your task.
    The program your organization runs works as follows: All candidates are asked for their original
    location and the location they would like to go to. The program works out only if every student has a
    suitable exchange partner. In other words, if a student wants to go from A to B, there must be another
    student who wants to go from B to A. This was an easy task when there were only about 50 candidates,
    however now there are up to 500000 candidates!

    Input:
            The input file contains multiple cases. Each test case will consist of a line containing n – the number
        of candidates (1 ≤ n ≤ 500000), followed by n lines representing the exchange information for each
        candidate. Each of these lines will contain 2 integers, separated by a single space, representing the
        candidate’s original location and the candidate’s target location respectively. Locations will be repre-
        sented by nonnegative integer numbers. You may assume that no candidate will have his or her original
        location being the same as his or her target location as this would fall into the domestic exchange
        program. The input is terminated by a case where n = 0; this case should not be processed.

    Output:
            For each test case, print ‘YES’ on a single line if there is a way for the exchange program to work out,
        otherwise print ‘NO’

    Sample:
        10
        1 2
        2 1
        3 4
        4 3
        100 200
        200 100
        57 2
        2 57
        1 2
        2 1
        10
        1 2
        3 4
        5 6
        7 8
        9 10
        11 12
        13 14
        15 16
        17 18
        19 20
        0
            =>  YES
                NO

"""

InputOrg_Raw = """
10
1 2
2 1
3 4
4 3
100 200
200 100
57 2
2 57
1 2
2 1
10
1 2
3 4
5 6
7 8
9 10
11 12
13 14
15 16
17 18
19 20
0
"""

InputUVa_Raw = """
4
1 3
2 4
5 7
14 8
3
1 2
1 2
2 1
0
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputUVa_Raw = InputUVa_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputUVa_Raw]

InputRaw = InputRaw_Lst[0]


def inDataAllRead(InputRaw):
    """
            Reads all the input data and sorts them
        into a list of lists (AllCandid)
    """

    InLines = InputRaw.split("\n")

    candNum = int(InLines.pop(0))
    caseCnt = 0

    AllCandid = []

    while candNum != 0:

        caseCnt += 1
        Candid = []

        # print(f"\tCases: {candNum}")
        # print()

        for cnd in range(candNum):
            cand = tuple(map(int, InLines.pop(0).split()))

            # print(f"\t\t{cand}")

            Candid.append(cand)

        AllCandid.append(Candid)
        candNum = int(InLines.pop(0))

        # print("\n")

    return AllCandid, caseCnt


def inDataRead(InLines, candNum):
    """
            Reads input data for a case and sorts
        them into a list (Candid)
    """

    Candid = []

    for cnd in range(candNum):
        cand = tuple(map(int, InLines.pop(0).split()))

        Candid.append(cand)

    return Candid


def inDataAllExtract(InputRaw):
    """
            Reads all the input data and sorts them
        into a list of lists (AllCandid)
            While extracting the data into dictionaries,
        a list of dictionaries From (AllDataFr)
        and a list of dictionaries To (AllDataTo)
    """

    InLines = InputRaw.split("\n")

    candNum = int(InLines.pop(0))
    caseCnt = 0

    AllCandid = []
    AllDataFr = []
    AllDataTo = []

    while candNum != 0:

        caseCnt += 1
        Candid = []

        DataFr = {}
        DataTo = {}

        # print(f"\tCases: {candNum}")
        # print()

        for cnd in range(candNum):
            cand = tuple(map(int, InLines.pop(0).split()))

            # print(f"\t\t{cand}")

            Candid.append(cand)

            fr, to = cand[0], cand[1]

            if fr in DataFr:
                DataFr[fr] += 1
            else:
                DataFr[fr] = 1

            if to in DataTo:
                DataTo[to] += 1
            else:
                DataTo[to] = 1

        AllCandid.append(Candid)

        AllDataFr.append(DataFr)
        AllDataTo.append(DataTo)

        candNum = int(InLines.pop(0))

        # print("\n")

    return AllCandid, caseCnt, AllDataFr, AllDataTo


def inDataExtract_DataFrTo(InLines, candNum):
    """
            Reads input data for a case and sorts
        them into a list (Candid)
            While extracting data into dictionaries,
        a dictionary From (DataFr)
        and a dictionary To (DataTo)
    """

    Candid = []

    DataFr = {}
    DataTo = {}

    for cnd in range(candNum):
        cand = tuple(map(int, InLines.pop(0).split()))

        Candid.append(cand)

        fr, to = cand[0], cand[1]

        if fr in DataFr:
            DataFr[fr] += 1
        else:
            DataFr[fr] = 1

        if to in DataTo:
            DataTo[to] += 1
        else:
            DataTo[to] = 1

    return Candid, DataFr, DataTo


def inDataExtract_DataFrToAll(InLines, candNum):
    """
            Reads input data for a case and sorts
        them into a list (Candid)
            While extracting data into dictionaries,
        a dictionary From (DataFr),
        a dictionary To (DataTo)
        and a dictionary All (DataAll)
    """

    Candid = []

    DataFr = {}
    DataTo = {}
    DataAll = {}

    for cnd in range(candNum):
        cand = tuple(map(int, InLines.pop(0).split()))

        Candid.append(cand)

        fr, to = cand[0], cand[1]

        if fr in DataFr:
            DataFr[fr] += 1
        else:
            DataFr[fr] = 1

        if to in DataTo:
            DataTo[to] += 1
        else:
            DataTo[to] = 1

        if fr in DataAll:
            DataAll[fr] += 1
        else:
            DataAll[fr] = 1

        if to in DataAll:
            DataAll[to] -= 1
        else:
            DataAll[to] = -1


    return Candid, DataFr, DataTo, DataAll


def inDataExtract_DataAll(InLines, candNum):
    """
            Reads input data for a case and
        extracts the into a single dictionary (DataAll)
    """

    DataAll = {}

    for cnd in range(candNum):
        cand = tuple(map(int, input().split()))

        fr, to = cand[0], cand[1]

        if fr in DataAll:
            DataAll[fr] += 1
        else:
            DataAll[fr] = 1

        if to in DataAll:
            DataAll[to] -= 1
        else:
            DataAll[to] = -1

    return DataAll


def inDataAllPrint(AllCandid, caseNum):

    print(f"\tCases: {caseNum}")
    print()

    for caseCnt, Candid in enumerate(AllCandid):

        print(f"\t\t{caseCnt+1}. Case")
        print()

        candNum = len(Candid)
        print(f"\t\t\tCandid. num.: {candNum}")
        print()

        for cnd, cand in enumerate(Candid):
            print(f"\t\t\t\t{cnd+1:2}. {cand}")

        if (caseCnt+1) < caseNum:
            print("\n")


def inDataPrint(Candid, candNum):

    print(f"\t\t\tCandid. num.: {candNum}")
    print()

    for cnd, cand in enumerate(Candid):
        print(f"\t\t\t\t{cnd + 1:2}. {cand}")


def extDataPrint(DataFr, DataTo):

    print("\t\t\t\tFrom/To Data:")
    print()

    FrToKys = set(list(DataFr.keys()) + list(DataTo.keys()))

    for FrTo in FrToKys:

        if FrTo in DataFr:
            if FrTo in DataTo:
                print(f"\t\t\t\t\t{FrTo:3}:  {DataFr[FrTo]:2}  |  {DataTo[FrTo]:2}")

            else:
                print(f"\t\t\t\t\t{FrTo:3}:  {DataFr[FrTo]:2}  |   0")

        else:
            print(f"\t\t\t\t\t{FrTo:3}:   0  |  {DataTo[FrTo]:2}")


def checkExchPlaces_DataFrToCnt(DataFr, DataTo):
    """
            Check if there is place for all
        the exchange candidates
    """

    NoPlace = False

    for FrKys in DataFr.keys():
        for Fr in range(DataFr[FrKys]):

            if FrKys in DataTo:
                if DataTo[FrKys]:
                    DataTo[FrKys] -= 1

                else:
                    NoPlace = True
                    return NoPlace

            else:
                NoPlace = True
                return NoPlace

    return NoPlace


def checkExchPlaces_DataFrToEqual(DataFr, DataTo):
    """
            Checks if the places From equal to places To
    """

    NoPlace = False

    for FrKys in DataFr.keys():

        if FrKys in DataTo:
            if DataFr[FrKys] == DataTo[FrKys]:
                continue
            else:
                NoPlace = True
                return NoPlace
        else:
            NoPlace = True
            return NoPlace

    return NoPlace


if __name__ == '__main__':

    print("Input:")
    print(InputRaw)

    InLines = InputRaw.split("\n")

    candNum = int(InLines.pop(0))
    caseCnt = 1

    while candNum != 0:
        print("\n")

        # Candid = inDataRead(InLines, candNum)
        Candid, DataFr, DataTo, DataAll = inDataExtract_DataFrToAll(InLines, candNum)

        print(f"\t\t{caseCnt}. Case")
        print()
        caseCnt += 1

        inDataPrint(Candid, candNum)
        print()

        extDataPrint(DataFr, DataTo)
        print()

        NoPlace = checkExchPlaces_DataFrToEqual(DataFr, DataTo)

        if NoPlace:
            print("\t\t\tNO, not enough exchange places found")
        else:
            print("\t\t\tYES, enough exchange places found")


        candNum = int(InLines.pop(0))


"""__Output__"""
"""
Input:
10
1 2
2 1
3 4
4 3
100 200
200 100
57 2
2 57
1 2
2 1
10
1 2
3 4
5 6
7 8
9 10
11 12
13 14
15 16
17 18
19 20
0


		1. Case

			Candid. num.: 10

				 1. [1, 2]
				 2. [2, 1]
				 3. [3, 4]
				 4. [4, 3]
				 5. [100, 200]
				 6. [200, 100]
				 7. [57, 2]
				 8. [2, 57]
				 9. [1, 2]
				10. [2, 1]

				From/To Data:

					  1:   2  |   2
					  2:   3  |   3
					  3:   1  |   1
					100:   1  |   1
					  4:   1  |   1
					200:   1  |   1
					 57:   1  |   1

			YES, enough exchange places found


		2. Case

			Candid. num.: 10

				 1. [1, 2]
				 2. [3, 4]
				 3. [5, 6]
				 4. [7, 8]
				 5. [9, 10]
				 6. [11, 12]
				 7. [13, 14]
				 8. [15, 16]
				 9. [17, 18]
				10. [19, 20]

				From/To Data:

					  1:   1  |   0
					  2:   0  |   1
					  3:   1  |   0
					  4:   0  |   1
					  5:   1  |   0
					  6:   0  |   1
					  7:   1  |   0
					  8:   0  |   1
					  9:   1  |   0
					 10:   0  |   1
					 11:   1  |   0
					 12:   0  |   1
					 13:   1  |   0
					 14:   0  |   1
					 15:   1  |   0
					 16:   0  |   1
					 17:   1  |   0
					 18:   0  |   1
					 19:   1  |   0
					 20:   0  |   1

			NO, not enough exchange places found

Process finished with exit code 0

"""