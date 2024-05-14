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


def dataExtract(InputRaw):

    InputLines = InputRaw.split("\n")

    caseNum = int(InputLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    numLst = list(map(int, InputLines))

    return caseNum, numLst


def fndDgts(num):
    if num < 10:
        return num

    dgts = []

    for d in range(9, 1, -1):
        while num % d == 0:
            print(f"\t\t\t\t{num} = {d} * {num // d}")

            num = num // d
            dgts.append(d)
    print()

    if num > 1:
        return -1

    dgts.sort()

    return int(''.join(map(str, dgts)))


if __name__ == '__main__':

    print("Input:")
    print(InputRaw)
    print()

    caseNum, numLst = dataExtract(InputRaw)

    for cs, num in enumerate(numLst):

        print(f"\t\t{cs+1}.Case")
        print(f"\t\t\tNum.: {num}")
        print()

        # dgts = []
        #
        # if num < 10:
        #     print(f"\t\t\t\t{num} = {num} * 1")
        #
        #     dgts.append(num)
        #     num = 1
        # else:
        #     for p in range(9, 1, -1):
        #         while num % p == 0:
        #             print(f"\t\t\t\t{num} = {p} * {num // p}")
        #
        #             num = num // p
        #             dgts.append(p)
        # print()

        resDgts = fndDgts(num)

        if resDgts != -1:
            print(f"\t\t\tDigits: {resDgts}")

        else:
            print("\t\t\tNo digits found")

        # if num == 1:
        #     dgts.sort()
        #     resDgts = int(''.join(map(str, dgts)))
        #
        #     print(f"\t\t\tDigits: {resDgts}")
        #
        # else:
        #     print("\t\t\tNo digits found")

        if (cs+1) < caseNum:
            print("\n")


"""__Output__"""
"""
Input:
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

	Cases: 20

		1.Case
			Num.: 0

			Digits: 0


		2.Case
			Num.: 1

			Digits: 1


		3.Case
			Num.: 2

			Digits: 2


		4.Case
			Num.: 7

			Digits: 7


		5.Case
			Num.: 9

			Digits: 9


		6.Case
			Num.: 10

				10 = 5 * 2
				2 = 2 * 1

			Digits: 25


		7.Case
			Num.: 48

				48 = 8 * 6
				6 = 6 * 1

			Digits: 68


		8.Case
			Num.: 96

				96 = 8 * 12
				12 = 6 * 2
				2 = 2 * 1

			Digits: 268


		9.Case
			Num.: 18

				18 = 9 * 2
				2 = 2 * 1

			Digits: 29


		10.Case
			Num.: 100000000

				100000000 = 8 * 12500000
				12500000 = 8 * 1562500
				1562500 = 5 * 312500
				312500 = 5 * 62500
				62500 = 5 * 12500
				12500 = 5 * 2500
				2500 = 5 * 500
				500 = 5 * 100
				100 = 5 * 20
				20 = 5 * 4
				4 = 4 * 1

			Digits: 45555555588


		11.Case
			Num.: 7523475

				7523475 = 5 * 1504695
				1504695 = 5 * 300939
				300939 = 3 * 100313

			No digits found


		12.Case
			Num.: 643


			No digits found


		13.Case
			Num.: 156236

				156236 = 4 * 39059

			No digits found


		14.Case
			Num.: 19


			No digits found


		15.Case
			Num.: 23


			No digits found


		16.Case
			Num.: 6746

				6746 = 2 * 3373

			No digits found


		17.Case
			Num.: 59049

				59049 = 9 * 6561
				6561 = 9 * 729
				729 = 9 * 81
				81 = 9 * 9
				9 = 9 * 1

			Digits: 99999


		18.Case
			Num.: 387420489

				387420489 = 9 * 43046721
				43046721 = 9 * 4782969
				4782969 = 9 * 531441
				531441 = 9 * 59049
				59049 = 9 * 6561
				6561 = 9 * 729
				729 = 9 * 81
				81 = 9 * 9
				9 = 9 * 1

			Digits: 999999999


		19.Case
			Num.: 430467221


			No digits found


		20.Case
			Num.: 373248

				373248 = 9 * 41472
				41472 = 9 * 4608
				4608 = 9 * 512
				512 = 8 * 64
				64 = 8 * 8
				8 = 8 * 1

			Digits: 888999

Process finished with exit code 0

"""