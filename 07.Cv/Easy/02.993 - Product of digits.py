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

InputOrg_Raw = InputOrg_Raw[1:-1]

if __name__ == '__main__':

    print("Input:")
    print(InputOrg_Raw)
    print()

    InputLines = InputOrg_Raw.split("\n")

    caseNum = int(InputLines.pop(0))
    print(f"\tCases: {caseNum}")
    print()


    numLst = list(map(int, InputLines))

    for cs, num in enumerate(numLst):

        print(f"\t\t{cs+1}.Case")
        print(f"\t\t\tNum.: {num}")
        print()

        dgts = []

        for p in range(9, 1, -1):
            while num % p == 0:
                print(f"\t\t\t\t{num} = {p} * {num // p}")

                num = num // p
                dgts.append(p)
        print()

        print("\t\t\tDigits: ", end="")
        for dg in dgts[::-1]:
            print(dg, end="")
        print()

        if (cs+1) < caseNum:
            print("\n")


"""__Output__"""
"""
Input:
3
1
10
123456789

	Cases: 3

		1.Case
			Num.: 1


			Digits: 


		2.Case
			Num.: 10

				10 = 5 * 2
				2 = 2 * 1

			Digits: 25


		3.Case
			Num.: 123456789

				123456789 = 9 * 13717421

			Digits: 9

Process finished with exit code 0

"""