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


"""29495547 	10763 	Foreign Exchange 	Accepted 	PYTH3 	0.540 	2024-05-20 22:26:02"""


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


def inDataExtract_Lst(InLines, candNum):
    """
            Reads input data for a case and sorts
        them into a list (Candid)
            While extracting data into dictionaries,
        a dictionary From (DataFr)
        and a dictionary to (DataTo)
    """

    Candid = []

    DataFr = {}
    DataTo = {}

    for cnd in range(candNum):
        cand = (list(map(int, InLines.pop(0).split())))

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


def inDataExtract_DataFrTo_In(candNum):
    """
            Reads input data for a case and sorts
        them into a list (Candid)
            While extracting data into dictionaries,
        a dictionary From (DataFr)
        and a dictionary to (DataTo)
    """

    Candid = []

    DataFr = defaultdict(int)
    DataTo = defaultdict(int)

    for cnd in range(candNum):
        fr, to = map(int, sys.stdin.readline().split())

        DataFr[fr] += 1
        DataTo[to] += 1

        Candid.append((fr, to))

    return Candid, DataFr, DataTo


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


"""__Code__"""


import sys
from collections import defaultdict


def inDataExtract_DataAll_In(candNum):
    """
            Reads input data for a case and
        extracts the into a single dictionary (DataAll)
    """

    DataAll = defaultdict(int)

    for cnd in range(candNum):
        fr, to = map(int, sys.stdin.readline().split())

        DataAll[fr] += 1
        DataAll[to] -= 1

    return DataAll


def checkExchPlaces_DataAll(DataAll):
    """
            Checks if there are differences between From and To
    """

    return all(candid == 0 for candid in DataAll.values())


if __name__ == '__main__':

    # print("Input:")
    # print(InputRaw)

    # InLines = InputRaw.split("\n")

    candNum = int(sys.stdin.readline())

    # caseCnt = 1

    while candNum != 0:
        # print("\n")

        # Candid, DataFr, DataTo = inDataExtract_DataFrTo_In(candNum)

        DataAll = inDataExtract_DataAll_In(candNum)

        # print(f"\t\t{caseCnt}. Case")
        # print()
        # caseCnt += 1

        # inDataPrint(Candid, candNum)
        # print()

        # extDataPrint(DataFr, DataTo)
        # print()

        # NoPlace = checkExchPlaces_DataFrToCnt(DataFr, DataTo)

        # if NoPlace:
        #     # print("\t\t\tNO, not enough exchange places found")
        #
        #     print("NO")
        # else:
        #     # print("\t\t\tYES, enough exchange places found")
        #
        #     print("YES")

        Place = checkExchPlaces_DataAll(DataAll)

        if Place:
            # print("\t\t\tYES, enough exchange places found")

            print("YES")
        else:
            # print("\t\t\tNO, not enough exchange places found")

            print("NO")

        candNum = int(sys.stdin.readline())
