"""

Bridge

        A group of n people wish to cross a bridge at night. At most two people may cross at
    any time, and each group must have a flashlight. Only one flashlight is available among
    the n people, so some sort of shuttle arrangement must be arranged in order to return
    the flashlight so that more people may cross.
        Each person has a different crossing speed; the speed of a group is determined by the
    speed of the slower member. Your job is to determine a strategy that gets all n people
    across the bridge in the minimum time.

    Input:
            The input begins with a single positive integer on a line by itself indicating the number
        of test cases, followed by a blank line. There is also a blank line between each two
        consecutive inputs.
            The first line of each case contains n, followed by n lines giving the crossing times
        for each of the people. There are not more than 1,000 people and nobody takes more
        than 100 seconds to cross the bridge.

    Output:
            For each test case, the first line of output must report the total number of seconds
        required for all n people to cross the bridge. Subsequent lines give a strategy for achiev-
        ing this time. Each line contains either one or two integers, indicating which person
        or people form the next group to cross. Each person is indicated by the crossing time
        specified in the input. Although many people may have the same crossing time, this
        ambiguity is of no consequence.
            Note that the crossings alternate directions, as it is necessary to return the flashlight
        so that more may cross. If more than one strategy yields the minimal time, any one
        will do.
        The output of two consecutive cases must be separated by a blank line.


    Sample:
        1

        4
        1
        2
        5
        10
            =>  17
                1 2
                1
                5 10
                2
                1 2

"""
import copy
from itertools import combinations

class Table:

    # def __init__(self, there, rest, end, time):
    #     self.there = there
    #     self.back = min(there)
    #     self.start = rest + self.back
    #     self.end = max(there)
    #     self.time = sum(there)

    def __init__(self, there = None, back = None, start = None, end = None, time = 0, previous = None):
        self.there = there
        self.back = back
        self.start = start
        self.end = end
        self.time = time
        self.previous = previous


InputRaw_Str = """
1

4
1
2
5
10
"""

InputLst_Str = InputRaw_Str.split("\n")[1:-1]

print(InputLst_Str)
print()

InputLst = []

for Input in InputLst_Str[1:]:

    if Input.isnumeric():

        InputLst.append(int(Input))

print(f"Input: {InputLst}\n")

pplNum = InputLst[0]

print(f"\tNumber of people: {pplNum}")

spdLst = InputLst[1: pplNum + 1]
print(f"\tSpeed of people:  {spdLst}")
print("\n")

strtPlc = copy.deepcopy(spdLst)
endPlc = []

# torch = True
time = 0

coupleLst = combinations(spdLst, 2)

"""
for couple in coupleLst:
    # print(list(couple))

    print(f"Group: {list(couple)}")

    rest = copy.deepcopy(spdLst)
    rest.remove(couple[0])
    rest.remove(couple[1])

    print(f"Rest:  {rest}")
    print()

    print(f"\tTime:   {sum(couple)}")
    print(f"\tTime of the group:   {max(couple)}")
    print(f"\tTime of the return:  {min(couple)}")
    print()
    print(f"\tStart:  {rest + [min(couple)]}")
    print(f"\tEnd:    {max(couple)}")
    print("\n")
# """


for couple in coupleLst:

    # (self, there, back, start, end, time, previous):

    rest = copy.deepcopy(spdLst)
    rest.remove(couple[0])
    rest.remove(couple[1])

    there = couple

    end = endPlc + list(couple)

    back = min(end)

    time = max(couple) + min(end)

    end.remove(back)

    start = rest + [back]

    curTbl = Table(there, back, start, end, time, None)

    print(f"\tThere: {curTbl.there}")
    print(f"\tTime:  {curTbl.time}")
    print()
    print(f"\t\tBack:  {curTbl.back}")
    print()
    print(f"\t\tStart: {curTbl.start}")
    print(f"\t\tEnd:   {curTbl.end}")
    print()
    print("\n")

    # print(f"Rest:  {rest}")
    # print()
    #
    # print(f"\tTime:   {sum(couple)}")
    # print(f"\tTime of the group:   {max(couple)}")
    # print(f"\tTime of the return:  {min(couple)}")
    # print()
    # print(f"\tStart:  {rest + [min(couple)]}")
    # print(f"\tEnd:    {max(couple)}")
    # print("\n")

# while strtPlc:
#
#     coupleLst = combinations(strtPlc, 2)
#


"""
while strtPlc:

    if torch:

        strtPlc.sort()

        endPlc += strtPlc[:2]
        time += max(strtPlc[:2])

        strtPlc = strtPlc[2:]

        torch = False

        print(f"Time: {time}")
        print(f"\t\t{strtPlc} ________ {endPlc}")
        print()

    else:

        endPlc.sort()

        strtPlc += [endPlc[0]]
        time += endPlc[0]

        endPlc = endPlc[1:]

        torch = True

        print(f"Time: {time}")
        print(f"\t\t{strtPlc} ________ {endPlc}")
        print()
# """


"""__Output__"""
"""
['1', '', '4', '1', '2', '5', '10']

Input: [4, 1, 2, 5, 10]

	Number of people: 4
	Speed of people:  [1, 2, 5, 10]


	There: (1, 2)
	Time:  3

		Back:  1

		Start: [5, 10, 1]
		End:   [2]



	There: (1, 5)
	Time:  6

		Back:  1

		Start: [2, 10, 1]
		End:   [5]



	There: (1, 10)
	Time:  11

		Back:  1

		Start: [2, 5, 1]
		End:   [10]



	There: (2, 5)
	Time:  7

		Back:  2

		Start: [1, 10, 2]
		End:   [5]



	There: (2, 10)
	Time:  12

		Back:  2

		Start: [1, 5, 2]
		End:   [10]



	There: (5, 10)
	Time:  15

		Back:  5

		Start: [1, 2, 5]
		End:   [10]




Process finished with exit code 0

"""


