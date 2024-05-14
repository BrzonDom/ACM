"""
993 - Product of digits
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=934

        For a given non-negative integer number N, find the minimal natural Q such that the product of all
    digits of Q is equal N.

    Input:
            The first line of input contains one positive integer number, which is the number of data sets. Each
        subsequent line contains one data set which consists of one non-negative integer number N (0 ≤ N ≤ 10^9).

    Output:
            For each data set, write one line containing the corresponding natural number Q or '-1' if Q does not
        exist.


    Sample:
        3
        1
        10
        123456789
            =>  1
                25
                -1

"""

"""29474193 	993 	Product of digits 	Accepted 	PYTH3 	0.010 	2024-05-14 20:53:04"""

InputOrg_Raw = """
3
1
10
123456789
"""

InputDbg_Raw = """
20
0
1
2
7
9
10
48
96
18
100000000
7523475
643
156236
19
23
6746
59049
387420489
430467221
373248
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputDbg_Raw = InputDbg_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputDbg_Raw]

InputRaw = InputRaw_Lst[1]

"""
def dataExtract_Prt():

    caseNum = int(input())

    print(f"\tCases: {caseNum}")
    print()

    numLst = []

    for _ in range(caseNum):
        numLst.append(int(input()))

    return caseNum, numLst


def fndDgts_Prt(num):
    if num < 10:
        return num

    dgts = []

    for d in range(9, 1, -1):
        while num % d == 0:
            print(f"\t\t\t\t{num} = {d} * {num // d}")

            num = num // d
            dgts.append(d)
    if dgts:
        print()

    if num > 1:
        return -1

    dgts.sort()

    return int(''.join(map(str, dgts)))
"""

"""__Code__"""

def dataExtract():

    caseNum = int(input())

    numLst = []

    for _ in range(caseNum):
        numLst.append(int(input()))

    return numLst


def fndDgts(num):
    if num < 10:
        return num

    dgts = []

    for d in range(9, 1, -1):
        while num % d == 0:

            num = num // d
            dgts.append(d)

    if num > 1:
        return -1

    dgts.sort()

    return int(''.join(map(str, dgts)))


if __name__ == '__main__':

    numLst = dataExtract()

    for cs, num in enumerate(numLst):

        # print(f"\t{cs+1}.Case")
        # print(f"\t\tNum.: {num}")
        # print()

        resDgts = fndDgts(num)
        print(resDgts)

        # if resDgts != -1:
        #     print(f"\t\tDigits: {resDgts}")
        #
        # else:
        #     print("\t\tNo digits found")
        #
        # if (cs+1) < len(numLst):
        #     print("\n")

