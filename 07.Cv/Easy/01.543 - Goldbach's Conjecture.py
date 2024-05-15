"""
543 - Goldbach's Conjecture
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=188&page=show_problem&problem=484

        In 1742, Christian Goldbach, a German amateur mathematician, sent a letter to Leonhard Euler in
    which he made the following conjecture:
        Every number greater than 2 can be written as the sum of three prime numbers.

        Goldbach was considering 1 as a primer number, a convention that is no longer followed. Later on,
    Euler re-expressed the conjecture as:
        Every even number greater than or equal to 4 can be expressed as the sum of two prime
    numbers.

        For example:
            • 8 = 3 + 5. Both 3 and 5 are odd prime numbers.
            • 20 = 3 + 17 = 7 + 13.
            • 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23.

        Today it is still unproven whether the conjecture is right. (Oh wait, I have the proof of course, but
    it is too long to write it on the margin of this page.)
        Anyway, your task is now to verify Goldbach’s conjecture as expressed by Euler for all even numbers
    less than a million

    Input:
            The input file will contain one or more test cases.
        Each test case consists of one even integer n with 6 ≤ n < 1000000.
        Input will be terminated by a value of 0 for n.

    Output:
            For each test case, print one line of the form n = a + b, where a and b are odd primes. Numbers and
        operators should be separated by exactly one blank like in the sample output below. If there is more
        than one pair of odd primes adding up to n, choose the pair where the difference b − a is maximized.
        If there is no such pair, print a line saying "Goldbach's conjecture is wrong."


    Sample:
        8
        20
        42
        0
            =>  8 = 3 + 5
                20 = 3 + 17
                42 = 5 + 37

"""

InputOrg_Raw = """
8
20
42
0
"""

InputDbg_Raw = """
999968
6
568
43422
989838
46
10
999998
748386
8
0
"""

InputOrg_Raw = InputOrg_Raw[1:-1]
InputDbg_Raw = InputDbg_Raw[1:-1]

InputRaw_Lst = [InputOrg_Raw, InputDbg_Raw]

InputRaw = InputRaw_Lst[0]


def fndPrimeTable(num):

    PrmTable = [False, False] + [True for i in range(2, num +1)]
    prm = 2

    while (prm ** 2 <= num):
        if PrmTable[prm]:

            for indx in range(prm ** 2, num +1, prm):
                PrmTable[indx] = False

        prm += 1

    return PrmTable


if __name__ == '__main__':

    print("Input:")
    print(InputRaw)
    print()

    InLines = InputRaw.split("\n")

    maxInNum = 1_000_000
    PrmTable = fndPrimeTable(maxInNum)

    num = int(InLines.pop(0))
    case = 1

    while num:

        print(f"\t{case}.Case")
        print()
        print(f"\t\tNum.: {num}")
        print()

        PrmLst = []

        for indx, PrmBl in enumerate(PrmTable[:num+1]):
            if PrmBl:
                PrmLst.append(indx)

        print(f"\t\tPrime List:  {PrmLst}")
        print()

        # lenPrim = len(PrmLst)
        #
        # for primNum in PrmLst[:(lenPrim + 1) // 2 + 1]:
        #     restNum = num - primNum
        #
        #     if restNum in PrmLst:
        #         print(f"\t\t\t{num} = {primNum} + {restNum}")
        # print()

        GldCnjctr = 0

        if num % 2 == 0:
            prmLen = num // 2 + 1
        else:
            prmLen = num // 2 + 2

        for indx in range(2, prmLen):
            if PrmTable[indx] and PrmTable[num - indx]:

                if not GldCnjctr:
                    GldCnjctr = (indx, num - indx)

                print(f"\t\t\t{num} = {indx} + {num - indx}")
        print()

        print(f"\t\t\tResult Goldbach Conjecture:")
        print(f"\t\t\t\t{num} = {GldCnjctr[0]} + {GldCnjctr[1]}")
        print()

        num = int(InLines.pop(0))
        case += 1

        if num:
            print()


"""__Output__"""
"""
Input:
8
20
42
0

	1.Case

		Num.: 8

		Prime List:  [2, 3, 5, 7]

			8 = 3 + 5

			Result Goldbach Conjecture:
				8 = 3 + 5


	2.Case

		Num.: 20

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19]

			20 = 3 + 17
			20 = 7 + 13

			Result Goldbach Conjecture:
				20 = 3 + 17


	3.Case

		Num.: 42

		Prime List:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

			42 = 5 + 37
			42 = 11 + 31
			42 = 13 + 29
			42 = 19 + 23

			Result Goldbach Conjecture:
				42 = 5 + 37


Process finished with exit code 0

"""
