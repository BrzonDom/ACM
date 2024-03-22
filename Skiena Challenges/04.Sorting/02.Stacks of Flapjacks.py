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


def flip(lst, indx):

    revLst = lst[:indx]
    revLst = revLst[::-1]

    return revLst + lst[indx:]


def sortSmpl_Prt(Lst):

    print(f"\tList: {Lst}\n")

    LstLen = len(Lst)

    LstSort = sorted(Lst)
    LstSol = sorted(Lst, reverse=True)

    print(f"\t\tSorted:    {LstSort}")
    print(f"\t\tSolution:  {LstSol}")
    print()

    StpCnt = 0
    FlipRec = []

    for n, num in enumerate(LstSort):

        if Lst.index(num) == LstSol.index(num):
            continue

        elif Lst == LstSol:
            break

        numPos = Lst.index(num) + 1
        StpCnt += 1

        print(f"\t\t{StpCnt:2}.StpCnt:")

        Lst = flip(Lst, numPos)
        print(f"\t\t\t{Lst} = flip(Lst, {numPos})")

        Lst = flip(Lst, LstLen-n)
        print(f"\t\t\t{Lst} = flip(Lst, {LstLen-n})")
        print()

        FlipRec += [numPos, LstLen-n]

    print(f"\n\t\tSolved: {Lst}")
    FlipRec.append(0)
    print(f"\t\t\tFlips: {FlipRec}")

    return FlipRec


def sortBFS_Prt(InLst):

    LstSol = sorted(InLst, reverse=True)

    if LstSol == InLst:
        print(f"\t\tSolved: {InLst}")
        # print(f"\t\t\tFlips: [0]")
        return InLst

    LstLen = len(InLst)
    LstSort = sorted(InLst)

    Flips = []
    for f in range(1, LstLen+1):
        Flips += [f]

    StpCnt = 0
    MtchCnt = 0
    FlipRec = []

    Queue = [InLst]

    while Queue:

        Lst = Queue[0]
        Queue = Queue[1:]

        if Lst == LstSol:
            print(f"\t\tSolved: {Lst}")
            return Lst

        for flp in Flips:
            Queue.append(flip(Lst, flp))

    return InLst


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

print("Driver simple solution:\n")

for Lst in InputLst:
    print(f"\tList: {Lst}\n")

    LstLen = len(Lst)

    LstSort = sorted(Lst)
    LstSol = sorted(Lst, reverse=True)

    print(f"\t\tSorted:    {LstSort}")
    print(f"\t\tSolution:  {LstSol}")
    print()

    StpCnt = 0

    FlipRec = []

    for n, num in enumerate(LstSort):

        if Lst.index(num) == LstSol.index(num):
            continue

        elif Lst == LstSol:
            break

        numPos = Lst.index(num) + 1
        StpCnt += 1

        print(f"\t\t{StpCnt:2}.StpCnt:")

        Lst = flip(Lst, numPos)
        print(f"\t\t\t{Lst} = flip(Lst, {numPos})")

        Lst = flip(Lst, LstLen-n)
        print(f"\t\t\t{Lst} = flip(Lst, {LstLen-n})")
        print()

        FlipRec += [numPos, LstLen - n]

    print(f"\n\t\tSolved: {Lst}")
    FlipRec.append(0)
    print(f"\t\t\tFlips: {FlipRec}")

    print("\n")

"""
print("Function simple solution:\n")

InputLst = copy.deepcopy(InputLstOrg)

for Lst in InputLst:

    FlipRec = sortSmpl_Prt(Lst)
    print(f"\t\t\t\tReturn: {FlipRec}")
    print("\n")
"""

print("Driver BFS testing:\n")

InputLst = copy.deepcopy(InputLstOrg)

for Lst in InputLst:

    print(f"\tList: {Lst}\n")

    LstLen = len(Lst)

    LstSol = sorted(Lst, reverse=True)
    LstSort = sorted(Lst)

    Flips = []
    for f in range(1, LstLen+1):
        Flips += [f]

    print(f"\t\tFlips: {Flips}")
    print()

    for flp in Flips:
        # flpLst = flip(Lst, flp)
        print(f"\t\tFlip[{flp}] = {flip(Lst, flp)}")

    # print()
    # for n, num in enumerate(Lst[LstLen::-1]):
    #     print(f"{n}. {num}")

    print("\n")


print("Function BFS solution:\n")

InputLst = copy.deepcopy(InputLstOrg)

for Lst in InputLst:

    print(f"\tList: {Lst}\n")

    LstSol = sortBFS_Prt(Lst)
    print(f"\t\t\tReturn: {LstSol}")
    print("\n")


# print("Example:\n")
#
# expLst = [8, 4, 6, 7, 5, 2]
#
# print(f"\tExample list: \n\t\t{expLst}\n")
#
# expLst = flip(expLst, 4)
# print(f"\tFlip 4:\n\t\t{expLst}\n")
#
# expLst = flip(expLst, 6)
#
# print(f"\tFlip 1:\n\t\t{expLst}\n")


"""__Output__"""
"""
Input:
	1 2 3 4 5
	5 4 3 2 1
	5 1 2 3 4


Driver simple solution:

	List: [1, 2, 3, 4, 5]

		Sorted:    [1, 2, 3, 4, 5]
		Solution:  [5, 4, 3, 2, 1]

		 1.StpCnt:
			[1, 2, 3, 4, 5] = flip(Lst, 1)
			[5, 4, 3, 2, 1] = flip(Lst, 5)


		Solved: [5, 4, 3, 2, 1]
			Flips: [1, 5, 0]


	List: [5, 4, 3, 2, 1]

		Sorted:    [1, 2, 3, 4, 5]
		Solution:  [5, 4, 3, 2, 1]


		Solved: [5, 4, 3, 2, 1]
			Flips: [0]


	List: [5, 1, 2, 3, 4]

		Sorted:    [1, 2, 3, 4, 5]
		Solution:  [5, 4, 3, 2, 1]

		 1.StpCnt:
			[1, 5, 2, 3, 4] = flip(Lst, 2)
			[4, 3, 2, 5, 1] = flip(Lst, 5)

		 2.StpCnt:
			[2, 3, 4, 5, 1] = flip(Lst, 3)
			[5, 4, 3, 2, 1] = flip(Lst, 4)


		Solved: [5, 4, 3, 2, 1]
			Flips: [2, 5, 3, 4, 0]


Function BFS solution:

	List: [1, 2, 3, 4, 5]

	List: [5, 4, 3, 2, 1]

	List: [5, 1, 2, 3, 4]


Process finished with exit code 0

"""