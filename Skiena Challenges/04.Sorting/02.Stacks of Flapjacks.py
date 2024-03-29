"""

Stacks of Flapjacks

    Cooking the perfect stack of pancakes on a grill is a tricky business, because no matter
    how hard you try all pancakes in any stack have different diameters. For neatness’s sake,
    however, you can sort the stack by size such that each pancake is smaller than all the
    pancakes below it. The size of a pancake is given by its diameter.
        Sorting a stack is done by a sequence of pancake “flips.” A flip consists of inserting
    a spatula between two pancakes in a stack and flipping (reversing) all the pancakes on
    the spatula (reversing the sub-stack). A flip is specified by giving the position of the
    pancake on the bottom of the sub-stack to be flipped relative to the entire stack. The
    bottom pancake has position 1, while the top pancake on a stack of n pancakes has
    position n.
        A stack is specified by giving the diameter of each pancake in the stack in the order
    in which the pancakes appear. For example, consider the three stacks of pancakes below
    in which pancake 8 is the top-most pancake of the left stack:

            8   7   2
            4   6   5
            6   4   8
            7   8   4
            5   5   6
            2   2   7

        The stack on the left can be transformed to the stack in the middle via flip(3). The
    middle stack can be transformed into the right stack via the command flip(1).

    Input:
            The input consists of a sequence of stacks of pancakes. Each stack will consist of between
        1 and 30 pancakes and each pancake will have an integer diameter between 1 and 100.
        The input is terminated by end-of-file. Each stack is given as a single line of input with
        the top pancake on a stack appearing first on a line, the bottom pancake appearing
        last, and all pancakes separated by a space.

    Output:
            For each stack of pancakes, your program should echo the original stack on one line,
        followed by a sequence of flips that results in sorting the stack of pancakes so that the
        largest pancake is on the bottom and the smallest on top. The sequence of flips for each
        stack should be terminated by a 0, indicating no more flips necessary. Once a stack is
        sorted, no more flips should be made.


    Sample:

        1 2 3 4 5
        5 4 3 2 1
        5 1 2 3 4
            =>  1 2 3 4 5
                0
                5 4 3 2 1
                1 0
                5 1 2 3 4
                1 2 0

"""

import copy


class TowerCls:

    def __init__(self, state, action = None, match = 0, previous = None):
        self.state = copy.deepcopy(state)
        self.action = action
        self.match = match
        self.previous = previous


def flip(lst, indx):

    revLst = lst[:indx+1]
    revLst = revLst[::-1]

    return revLst + lst[indx+1:]


def sortSmpl_Prt(Twr):

    print(f"\tTower: {Twr}\n")

    twrLen = len(Twr)

    # twrSort = sorted(Twr, reverse=True)
    twrSol = sorted(Twr)

    # print(f"\t\tSorted:    {twrSort}")
    print(f"\t\tSolution:  {twrSol}")
    print()

    StpCnt = 0
    MtchCnt = twrLen

    FlipRec = []

    for num in twrSol[::-1]:

        MtchCnt -= 1

        if Twr == twrSol:
            break

        elif Twr.index(num) == twrSol.index(num):
            continue

        numPos = Twr.index(num)
        StpCnt += 1

        print(f"\t\t{StpCnt:2}.Step:")

        Twr = flip(Twr, numPos)
        print(f"\t\t\t{Twr} = flip(Twr, {numPos})")

        Twr = flip(Twr, MtchCnt)
        print(f"\t\t\t{Twr} = flip(Twr, {MtchCnt})")
        print()

        FlipRec += [numPos, MtchCnt]

    print(f"\n\t\tSolved: {Twr}")
    FlipRec.append(0)
    print(f"\t\t\tFlips: {FlipRec}")

    return FlipRec


# def sortBFS_Cls_Prt(inTwr):
#
#     twrSol = sorted(inTwr, reverse=True)
#     twrLen = len(inTwr)
#
#     print(f"\tTower: {inTwr}\n")
#     print(f"\t\tSolution:  {twrSol}")
#     print()
#
#     Twr = TowerCls(inTwr)
#
#     queueTwr = [Twr]
#
#     while queueTwr:
#
#         cTwr = queueTwr[0]
#         queueTwr = queueTwr[1:]
#
#         if Twr.state == twrSol:
#             break
#
#         for pos in range(Twr.match + 1, twrLen):
#
#             if Twr.state[twrLen - pos] == twrSol[twrLen - pos]:
#                 Twr.match += 1
#
#             else:
#                 break
#
#     return


def sortBFS_Sol(inTwr):

    twrSol = sorted(inTwr)
    twrLen = len(inTwr)

    print(f"\tTower: {inTwr}\n")
    print(f"\t\tSolution:  {twrSol}")
    print()

    queueTwr = [inTwr]

    flpsRec = {}
    flpsRec[str(inTwr)] = []

    while queueTwr:

        cTwr = queueTwr[0]
        queueTwr = queueTwr[1:]

        if cTwr == twrSol:

            flpsRec[str(cTwr)] += [0]

            print(f"\t\tFlips: {flpsRec[str(cTwr)]}")

            return flpsRec[str(cTwr)]

        mtchCnt = match = 0

        for m, mtch in enumerate(twrSol[::-1]):

            if cTwr[twrLen - m - 1] == mtch:
                mtchCnt += 1

            else:
                match = mtch
                break

        for flp in range(1, twrLen - mtchCnt):
            nTwr = flip(cTwr, flp)

            if str(nTwr) not in flpsRec:
                queueTwr += [nTwr]
                flpsRec[str(nTwr)] = flpsRec[str(cTwr)] + [flp]

    return 0



if __name__ == '__main__':

    InputRaw_Str = """
    1 2 3 4 5
    5 4 3 2 1
    5 1 2 3 4
    """

    InputLst_Str = InputRaw_Str.split("\n")[1:-1]

    InputLst = []

    print("Input:")

    for Input in InputLst_Str:
        print(f"\t{Input}")

        InputLst.append(list(map(int, Input.split())))

    InputLstOrg = copy.deepcopy(InputLst)
    print("\n")


    """Driver simple solution"""
    """
    print("Driver simple solution:\n")
    
    for Twr in InputLst:
    
        print(f"\tTower: {Twr}\n")
    
        twrLen = len(Twr)
    
        # twrSort = sorted(Twr, reverse=True)
        twrSol = sorted(Twr)
    
        # print(f"\t\tSorted:    {twrSort}")
        print(f"\t\tSolution:  {twrSol}")
        print()
    
        StpCnt = 0
        MtchCnt = twrLen
    
        FlipRec = []
    
        for num in twrSol[::-1]:
    
            MtchCnt -= 1

            if Twr == twrSol:
                break
    
            elif Twr.index(num) == twrSol.index(num):
                continue
    
            numPos = Twr.index(num)
            StpCnt += 1
    
            print(f"\t\t{StpCnt:2}.Step:")
    
            Twr = flip(Twr, numPos)
            print(f"\t\t\t{Twr} = flip(Twr, {numPos})")
    
            Twr = flip(Twr, MtchCnt)
            print(f"\t\t\t{Twr} = flip(Twr, {MtchCnt})")
            print()
    
            FlipRec += [numPos, MtchCnt]
    
        print(f"\n\t\tSolved: {Twr}")
        FlipRec.append(0)
        print(f"\t\t\tFlips: {FlipRec}")
    
        print("\n")
    # """


    """Function simple solution"""
    """
    print("Function simple solution:\n")
    
    InputLst = copy.deepcopy(InputLstOrg)
    
    for Twr in InputLst:
    
        FlipRec = sortSmpl_Prt(Twr)
    
        print(f"\t\t\t\tReturn: {FlipRec}")
        print("\n")
    # """


    """Driver simple class solution"""
    """
    print("Driver simple class solution:\n")

    for Twr in InputLst:

        orgTwr = Twr

        print(f"\tTower: {Twr}\n")

        Tower = TowerCls(Twr)

        twrLen = len(Twr)

        # twrSort = sorted(Twr)
        twrSol = sorted(Twr)

        # print(f"\t\tSorted:    {twrSort}")
        print(f"\t\tSolution:  {twrSol}")
        print()

        StpCnt = 0
        # MtchCnt = twrLen

        FlipRec = []

        # for n, num in enumerate(twrSort):
        while Tower.state != twrSol:

            # MtchCnt -= 1

            for pos in range(Tower.match, twrLen):

                if Tower.state[twrLen-pos-1] == twrSol[twrLen-pos-1]:
                    Tower.match += 1

                else:
                    break

            StpCnt += 1
            MtchCnt = Tower.match
            Match = twrSol[twrLen - MtchCnt - 1]

            numIndx = Tower.state.index(Match)
            numPos = twrLen - 1 - MtchCnt

            print(f"\t\t{StpCnt:2}.Step:")

            Twr = flip(Twr, numIndx)
            print(f"\t\t\t{Twr} = flip(Twr, {numIndx})")

            Tower = TowerCls(Twr, numIndx, MtchCnt, Tower)

            Twr = flip(Twr, numPos)
            print(f"\t\t\t{Twr} = flip(Twr, {numPos})")
            print()

            Tower = TowerCls(Twr, numPos, Tower.match, Tower)

            FlipRec += [numIndx, numPos]

        print(f"\n\t\tSolved: {Twr}")
        FlipRec.append(0)
        print(f"\t\t\tFlips: {FlipRec}")
        print("\n")

        allTwrs = []
        allFlps = []

        while Tower.action != None:

            allTwrs.append(Tower.state)
            allFlps.append(Tower.action)

            Tower = Tower.previous

        allTwrs = allTwrs[::-1]
        allFlps = allFlps[::-1] + [0]

        print(f"\tTower: {orgTwr}\n")

        for t, pthTwr in enumerate(allTwrs):
            print(f"\t\t{t+1:2}.Step:")

            print(f"\t\t\t{pthTwr} = flip(Twr, {allFlps[t]})")
            print()

        print(f"\n\t\tSolved: {twrSol}")
        print(f"\t\t\tFlips: {allFlps}")

        # print(allTwrs)
        # print(allFlps)

        print("\n\n")
    # """


    """Function BFS solution"""
    # """
    print("Function BFS solution:\n")

    InputLst = copy.deepcopy(InputLstOrg)

    for Twr in InputLst:

        # print(f"\tTower: {Twr}\n")

        twrSol = sortBFS_Sol(Twr)
        print(f"\t\t\tReturn: {twrSol}")
        print("\n")
    # """


    """Flips examples"""
    """
    print("Example:\n")
    
    expLst = [8, 4, 6, 7, 5, 2]
    
    print(f"\tExample list: \n\t\t{expLst}\n")
    
    expLst = flip(expLst, 4)
    print(f"\tFlip 4:\n\t\t{expLst}\n")
    
    expLst = flip(expLst, 6)
    
    print(f"\tFlip 1:\n\t\t{expLst}\n")
    # """

"""__Output__"""
"""
Input:
	    1 2 3 4 5
	    5 4 3 2 1
	    5 1 2 3 4


Function BFS solution:

	Tower: [1, 2, 3, 4, 5]

		Solution:  [1, 2, 3, 4, 5]

		Flips: [0]
			Return: [0]


	Tower: [5, 4, 3, 2, 1]

		Solution:  [1, 2, 3, 4, 5]

		Flips: [4, 0]
			Return: [4, 0]


	Tower: [5, 1, 2, 3, 4]

		Solution:  [1, 2, 3, 4, 5]

		Flips: [4, 3, 0]
			Return: [4, 3, 0]



Process finished with exit code 0

"""