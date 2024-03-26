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

caseLen = 2

caseMem = {}

while caseLen <= pplNum:

    caseTpl = (combinations(spdLst, caseLen))

    caseLst = [list(case) for case in caseTpl]

    # print(caseLst)

    # Table(self, there, back, start, end, time, previous):

    for case in caseLst:

        print(f"\tCase: {case}\n")

        thereTpl = combinations(case, 2)

        thereLst = [list(there) for there in thereTpl]

        frstDec = True

        for there in thereLst:

            rest = [rem for rem in case if rem not in there]

            if rest:

                back = min(there)
                start = sorted(rest + [min(there)])
                end = [max(there)]
                time = sum(there)

                previous = caseMem[str(start)]

                curTbl = Table(there, back, start, end, time, previous)

            else:

                back = None
                start = []
                end = there
                time = max(there)

                curTbl = Table(there, back, start, end, time)

            print(f"\t\t\t\t{str(there):10} {str(time):5} {str(start):10} {str(end):10}")

            if frstDec:
                optTbl = curTbl
                frstDec = False

            elif optTbl.time > curTbl.time:
                optTbl = curTbl

        print()
        print("\t\tOptimal decision:\n")

        print(f"\t\t\tThere: {optTbl.there}")
        print(f"\t\t\tTime:  {optTbl.time}")

        if optTbl.back != None:
            print()
            print(f"\t\t\t\tBack:  {optTbl.back}")
            print()
            print(f"\t\t\t\tStart: {optTbl.start}")
        else:
            print()
        print(f"\t\t\t\tEnd:   {optTbl.end}")
        print()

        # print(f"\t\t{str(optTbl.there):10} {str(optTbl.time):5} {str(optTbl.start):10} {str(optTbl.end):10}")

        caseMem[str(case)] = optTbl

        print("\n")

    caseLen += 1

print()

stpCnt = 2

time = 0
path = []

finCase = caseMem[str(strtPlc)]


print(f"\tFinal case: {strtPlc}")
print()
print("\t\t1.Step:\n")
print(f"\t\t\tThere: {finCase.there}")
print(f"\t\t\tTime:  {finCase.time}")
print()
print(f"\t\t\tBack:  {finCase.back}")
print()
print(f"\t\t\tStart: {finCase.start}")
print(f"\t\t\tEnd:   {finCase.end}")
print()

pathCase = finCase.previous

time += finCase.time
path += [finCase.there]
path += [[finCase.back]]

while pathCase != None:
    print(f"\t\t{stpCnt}.Step:\n")
    stpCnt += 1

    print(f"\t\t\tThere: {pathCase.there}")
    print(f"\t\t\tTime:  {pathCase.time}")
    print()
    print(f"\t\t\tBack:  {pathCase.back}")
    print()
    print(f"\t\t\tStart: {pathCase.start}")
    print(f"\t\t\tEnd:   {pathCase.end}")
    print()

    time += pathCase.time
    path += [pathCase.there]
    path += [[pathCase.back]]

    pathCase = pathCase.previous


# print(path)

print("\n")


for case in caseMem:
    print(f"\t{str(case):15} {str(caseMem[case].there):10} {str(caseMem[case].time):5} {str(caseMem[case].start):10} {str(caseMem[case].end):10}")


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

# optTbl = Table((1, 5), 1, [2, 10, 1], [5], 6, None)

frst = True

"""
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

    print(f"\t\tThere: {curTbl.there}")
    print(f"\t\tTime:  {curTbl.time}")
    print()
    print(f"\t\t\tBack:  {curTbl.back}")
    print()
    print(f"\t\t\tStart: {curTbl.start}")
    print(f"\t\t\tEnd:   {curTbl.end}")
    print()
    print("\n")

    if frst:
        optTbl = curTbl
        frst = False

    elif optTbl.time > curTbl.time:
        optTbl = curTbl


print("1. Optimal decision:\n")

print(f"\tThere: {optTbl.there}")
print(f"\tTime:  {optTbl.time}")
print()
print(f"\t\tBack:  {optTbl.back}")
print()
print(f"\t\tStart: {optTbl.start}")
print(f"\t\tEnd:   {optTbl.end}")
print()
print("\n")

prvTbl = optTbl
# """

"""
frst = True

coupleLst = combinations(prvTbl.start, 2)

for couple in coupleLst:

    rest = copy.deepcopy(prvTbl.start)
    rest.remove(couple[0])
    rest.remove(couple[1])

    there = couple

    end = prvTbl.end + list(couple)

    back = min(end)

    time = prvTbl.time + max(couple) + min(end)

    end.remove(back)

    start = rest + [back]

    curTbl = Table(there, back, start, end, time, prvTbl)

    print(f"\t\tThere: {curTbl.there}")
    print(f"\t\tTime:  {curTbl.time}")
    print()
    print(f"\t\t\tBack:  {curTbl.back}")
    print()
    print(f"\t\t\tStart: {curTbl.start}")
    print(f"\t\t\tEnd:   {curTbl.end}")
    print()
    print("\n")

    if frst:
        optTbl = curTbl
        frst = False

    elif optTbl.time > curTbl.time:
        optTbl = curTbl


print("2. Optimal decision:\n")

print(f"\tThere: {optTbl.there}")
print(f"\tTime:  {optTbl.time}")
print()
print(f"\t\tBack:  {optTbl.back}")
print()
print(f"\t\tStart: {optTbl.start}")
print(f"\t\tEnd:   {optTbl.end}")
print()
print("\n")
# """

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


	Case: [1, 2]

				[1, 2]     2     []         [1, 2]    

		Optimal decision:

			There: [1, 2]
			Time:  2

				End:   [1, 2]



	Case: [1, 5]

				[1, 5]     5     []         [1, 5]    

		Optimal decision:

			There: [1, 5]
			Time:  5

				End:   [1, 5]



	Case: [1, 10]

				[1, 10]    10    []         [1, 10]   

		Optimal decision:

			There: [1, 10]
			Time:  10

				End:   [1, 10]



	Case: [2, 5]

				[2, 5]     5     []         [2, 5]    

		Optimal decision:

			There: [2, 5]
			Time:  5

				End:   [2, 5]



	Case: [2, 10]

				[2, 10]    10    []         [2, 10]   

		Optimal decision:

			There: [2, 10]
			Time:  10

				End:   [2, 10]



	Case: [5, 10]

				[5, 10]    10    []         [5, 10]   

		Optimal decision:

			There: [5, 10]
			Time:  10

				End:   [5, 10]



	Case: [1, 2, 5]

				[1, 2]     3     [1, 5]     [2]       
				[1, 5]     6     [1, 2]     [5]       
				[2, 5]     7     [1, 2]     [5]       

		Optimal decision:

			There: [1, 2]
			Time:  3

				Back:  1

				Start: [1, 5]
				End:   [2]



	Case: [1, 2, 10]

				[1, 2]     3     [1, 10]    [2]       
				[1, 10]    11    [1, 2]     [10]      
				[2, 10]    12    [1, 2]     [10]      

		Optimal decision:

			There: [1, 2]
			Time:  3

				Back:  1

				Start: [1, 10]
				End:   [2]



	Case: [1, 5, 10]

				[1, 5]     6     [1, 10]    [5]       
				[1, 10]    11    [1, 5]     [10]      
				[5, 10]    15    [1, 5]     [10]      

		Optimal decision:

			There: [1, 5]
			Time:  6

				Back:  1

				Start: [1, 10]
				End:   [5]



	Case: [2, 5, 10]

				[2, 5]     7     [2, 10]    [5]       
				[2, 10]    12    [2, 5]     [10]      
				[5, 10]    15    [2, 5]     [10]      

		Optimal decision:

			There: [2, 5]
			Time:  7

				Back:  2

				Start: [2, 10]
				End:   [5]



	Case: [1, 2, 5, 10]

				[1, 2]     3     [1, 5, 10] [2]       
				[1, 5]     6     [1, 2, 10] [5]       
				[1, 10]    11    [1, 2, 5]  [10]      
				[2, 5]     7     [1, 2, 10] [5]       
				[2, 10]    12    [1, 2, 5]  [10]      
				[5, 10]    15    [1, 2, 5]  [10]      

		Optimal decision:

			There: [1, 2]
			Time:  3

				Back:  1

				Start: [1, 5, 10]
				End:   [2]




	Final case: [1, 2, 5, 10]

		1.Step:

			There: [1, 2]
			Time:  3

			Back:  1

			Start: [1, 5, 10]
			End:   [2]

		2.Step:

			There: [1, 5]
			Time:  6

			Back:  1

			Start: [1, 10]
			End:   [5]

		3.Step:

			There: [1, 10]
			Time:  10

			Back:  None

			Start: []
			End:   [1, 10]



	[1, 2]          [1, 2]     2     []         [1, 2]    
	[1, 5]          [1, 5]     5     []         [1, 5]    
	[1, 10]         [1, 10]    10    []         [1, 10]   
	[2, 5]          [2, 5]     5     []         [2, 5]    
	[2, 10]         [2, 10]    10    []         [2, 10]   
	[5, 10]         [5, 10]    10    []         [5, 10]   
	[1, 2, 5]       [1, 2]     3     [1, 5]     [2]       
	[1, 2, 10]      [1, 2]     3     [1, 10]    [2]       
	[1, 5, 10]      [1, 5]     6     [1, 10]    [5]       
	[2, 5, 10]      [2, 5]     7     [2, 10]    [5]       
	[1, 2, 5, 10]   [1, 2]     3     [1, 5, 10] [2]       

Process finished with exit code 0

"""


