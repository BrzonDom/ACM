"""
GERGOVIA - Wine trading in Gergovia
https://www.spoj.com/problems/GERGOVIA/

        Gergovia consists of one street, and every inhabitant of the city is a wine salesman. Everyone buys wine from
    other inhabitants of the city. Every day each inhabitant decides how much wine he wants to buy or sell.
    Interestingly, demand and supply is always the same, so that each inhabitant gets what he wants.
        There is one problem, however: Transporting wine from one house to another results in work. Since all wines
    are equally good, the inhabitants of Gergovia don't care which persons they are doing trade with, they are only
    interested in selling or buying a specific amount of wine.
        In this problem you are asked to reconstruct the trading during one day in Gergovia. For simplicity we will
    assume that the houses are built along a straight line with equal distance between adjacent houses. Transporting
    one bottle of wine from one house to an adjacent house results in one unit of work.

    Input:
            The input consists of several test cases.
        Each test case starts with the number of inhabitants N (2 ≤ N ≤ 100000).
        The following line contains n integers a_i (-1000 ≤ a_i ≤ 1000).
        If a_i ≥ 0, it means that the inhabitant living in the i^th house wants to buy a_i bottles of wine.
        If a_i < 0, he wants to sell -a_i bottles of wine.
        You may assume that the numbers a_i sum up to 0.
        The last test case is followed by a line containing 0.

    Output:
            For each test case print the minimum amount of work units needed so that every inhabitant has his
        demand fulfilled.


    Sample:
        5
        5 -4 1 -3 1
        6
        -1000 -1000 -1000 1000 1000 1000
        0
            =>  9
                9000


"""


"""33077268 	2024-05-21 12:08:00 	BrzonDom	Wine trading in Gergovia	accepted edit    ideone it 	0.22 	21M 	PYTHON3"""


import copy

InputRaw_Str = """
5
5 -4 1 -3 1
6
-1000 -1000 -1000 1000 1000 1000
7
5 -4 1 -3 2 -5 4
0
"""

InputRaw_Str = InputRaw_Str[1:-1]

def mvsHs(BuySell):

    cntMvs = 0

    while not all(hs == 0 for hs in BuySell):

        for h, hs in enumerate(BuySell):

            if hs > 0:

                lftHs = sum(BuySell[:h])
                rgtHs = sum(BuySell[h + 1:])

                if lftHs > rgtHs:
                    move = min(-rgtHs, hs)

                    BuySell[h] -= move
                    BuySell[h + 1] += move
                    cntMvs += move

                elif lftHs < rgtHs:
                    move = min(-lftHs, hs)

                    BuySell[h] -= move
                    BuySell[h - 1] += move
                    cntMvs += move

                else:
                    move = hs // 2

                    BuySell[h] -= 2 * move
                    BuySell[h - 1] += move
                    BuySell[h + 1] += move
                    cntMvs += 2 * move

    return cntMvs


"""__Code__"""


def cntMvsHs(BuySell, hsNum):

    cntMvs = 0

    for hs in range(1, hsNum):

        cntMvs += abs(BuySell[hs-1])

        BuySell[hs] += BuySell[hs-1]
        BuySell[hs-1] = 0

    return cntMvs


if __name__ == "__main__":

    # print("Input:")
    # print(InputRaw_Str)
    # print()

    hsNum = int(input())

    # caseCnt = 1

    while hsNum != 0:

        BuySell = list(map(int, input().split()))

        # print()
        #
        # print(f"\tNum. of people: {hsNum}")
        #
        # print(f"\tBuy Sell list: {BuySell}")
        # print()

        # cntMvs = mvsHs(BuySell)
        cntMvs = cntMvsHs(BuySell, hsNum)

        # print(f"\t\tNeeded moves: {cntMvs}")
        # print("\n")

        print(cntMvs)

        hsNum = int(input())

        # caseCnt += 1
