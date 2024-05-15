"""
11388 - GCD LCM
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=189&page=show_problem&problem=2383

        The GCD of two positive integers is the largest integer that divides both the integers without any
    remainder. The LCM of two positive integers is the smallest positive integer that is divisible by both
    the integers. A positive integer can be the GCD of many pairs of numbers. Similarly, it can be the
    LCM of many pairs of numbers. In this problem, you will be given two positive integers. You have to
    output a pair of numbers whose GCD is the first number and LCM is the second number.

    Input:
            The first line of input will consist of a positive integer T. T denotes the number of cases. Each of the
        next T lines will contain two positive integer, G and L.

    Output:
            For each case of input, there will be one line of output. It will contain two positive integers a and
        b, a ≤ b, which has a GCD of G and LCM of L. In case there is more than one pair satisfying the
        condition, output the pair for which a is minimized. In case there is no such pair, output ‘-1’.
        Constraints
        • T ≤ 100
        • Both G and L will be less than 231.


    Sample:
        2
        1 2
        3 4
            =>  1 2
                -1

"""

InputOrg_Raw = """
2
1 2
3 4
"""

InputDbg_Raw = """
53
2 2
3 4
5 6
2 5
2 4
6 9
1 6
4 8
2 2
3 4
5 6
2 5
2 4
1 5
12 100
4 26
9 12
10 20
3 5
6 9
4 8
4 8
2 8
5 10
10 15
6 56
7 89
6 98
3 18
8 9
7 70
3 12
1 280
8 9
7 70
3 12
3 99
200 300
150 123
125 25000
13 56
13 39
8 40
3 54
1 2
3 4
6 10
2 359096
12 4
3 9
12 1260
55 5224
5424 23131231
"""

InputTst_Raw = """
14
1 10
1 23
23 31
23 46
23 4600
5 25
5 26
78 39
40 50
40 5000
56 78
45 120
9 33
9 83
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputDbg_Raw = InputDbg_Raw[1:-1]
InputTst_Raw = InputTst_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputDbg_Raw, InputTst_Raw]

InputRaw = InputRaw_Lst[2]

import math


def dataExtract_Prt(InputRaw):

    InputLines = InputRaw.split("\n")

    caseNum = int(InputLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    caseLst = []

    for cs in range(caseNum):

        inLine = InputLines.pop(0)
        nums = list(map(int, inLine.split()))

        caseLst.append(nums)

    return caseLst


if __name__ == '__main__':

    print("Input:")
    print(InputRaw)
    print()

    caseLst = dataExtract_Prt(InputRaw)

    outputLst = []

    for cs, nums in enumerate(caseLst):

        print(f"\t\t{cs+1}. Case")
        print()

        print(f"\t\t\t1.Num. (GCD): {nums[0]}")
        print(f"\t\t\t2.Num. (LCM): {nums[1]}")
        print()

        gcd = math.gcd(nums[0], nums[1])
        lcm = math.lcm(nums[0], nums[1])

        # print(f"\t\t\t\tGCD: {gcd}")
        # print(f"\t\t\t\tLCM: {lcm}")
        # print()

        if nums[1] % nums[0] == 0:
            print(f"\t\t\tRes.: {nums[0]}, {nums[1]}")
            outputLst.append(f"{nums[0]} {nums[1]}")

        else:
            print(f"\t\t\tNo result")
            outputLst.append("-1")

        if (cs+1) < len(caseLst):
            print("\n")

    print("\n")
    print("__Output__:\n")

    for out in outputLst:
        print(out)


"""__Output__"""
"""
Input:
14
1 10
1 23
23 31
23 46
23 4600
5 25
5 26
78 39
40 50
40 5000
56 78
45 120
9 33
9 83

	Cases: 14

		1. Case

			1.Num. (GCD): 1
			2.Num. (LCM): 10

			Res.: 1, 10


		2. Case

			1.Num. (GCD): 1
			2.Num. (LCM): 23

			Res.: 1, 23


		3. Case

			1.Num. (GCD): 23
			2.Num. (LCM): 31

			No result


		4. Case

			1.Num. (GCD): 23
			2.Num. (LCM): 46

			Res.: 23, 46


		5. Case

			1.Num. (GCD): 23
			2.Num. (LCM): 4600

			Res.: 23, 4600


		6. Case

			1.Num. (GCD): 5
			2.Num. (LCM): 25

			Res.: 5, 25


		7. Case

			1.Num. (GCD): 5
			2.Num. (LCM): 26

			No result


		8. Case

			1.Num. (GCD): 78
			2.Num. (LCM): 39

			No result


		9. Case

			1.Num. (GCD): 40
			2.Num. (LCM): 50

			No result


		10. Case

			1.Num. (GCD): 40
			2.Num. (LCM): 5000

			Res.: 40, 5000


		11. Case

			1.Num. (GCD): 56
			2.Num. (LCM): 78

			No result


		12. Case

			1.Num. (GCD): 45
			2.Num. (LCM): 120

			No result


		13. Case

			1.Num. (GCD): 9
			2.Num. (LCM): 33

			No result


		14. Case

			1.Num. (GCD): 9
			2.Num. (LCM): 83

			No result


__Output__:

1 10
1 23
-1
23 46
23 4600
5 25
-1
-1
-1
40 5000
-1
-1
-1
-1

Process finished with exit code 0

"""