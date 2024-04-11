"""
10783 - Odd Sum
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1724

    Given a range [a, b], you are to find the summation of all the odd integers in this range. For example,
    the summation of all the odd integers in the range [3, 9] is 3 + 5 + 7 + 9 = 24.

    Input:
            There can be at multiple test cases. The first line of input gives you the number of test cases, T
        (1 ≤ T ≤ 100). Then T test cases follow. Each test case consists of 2 integers a and b (0 ≤ a ≤ b ≤ 100)
        in two separate lines.

    Output:
            For each test case you are to print one line of output – the serial number of the test case followed by
        the summation of the odd integers in the range [a, b].

    Sample:
        2
        1
        5
        3
        5
            =>  Case 1: 9
                Case 2: 8

"""

if __name__ == '__main__':

    InputRaw_Str = """
5
1
5
3
5
4
12
2
5
0
7
"""

    InputRaw_Str = InputRaw_Str[1:-1]

    InputStr_Lst = list(map(int, InputRaw_Str.split("\n")))

    print("Input:", InputStr_Lst)
    print()

    casesNum = InputStr_Lst[0]

    print(f"Num. of cases: {casesNum}")
    print()

    inputLst = InputStr_Lst[1:]

    for case in range(casesNum):

        rngMin = inputLst[case*2]
        rngMax = inputLst[case*2 + 1]

        print(f"\t{case+1}. Case")
        print()

        print(f"\t\tRange min.: {rngMin}")
        print(f"\t\tRange max.: {rngMax}")
        print()

        if rngMin % 2 == 0:
            oddMin = rngMin + 1
        else:
            oddMin = rngMin

        oddMax = rngMax + 1

        print(f"\t\t\tParameters: [{oddMin}, {oddMax}, 2]")
        print()

        oddRange = [* range(oddMin, oddMax, 2)]

        print(f"\t\tRange: {oddRange}")
        print(f"\t\t  Sum:  {sum(oddRange)}")

        if case < casesNum - 1:
            print("\n")


"""__Output__"""
"""
Input: [5, 1, 5, 3, 5, 4, 12, 2, 5, 0, 7]

Num. of cases: 5

	1. Case

		Range min.: 1
		Range max.: 5

			Parameters: [1, 6, 2]

		Range: [1, 3, 5]
		  Sum:  9


	2. Case

		Range min.: 3
		Range max.: 5

			Parameters: [3, 6, 2]

		Range: [3, 5]
		  Sum:  8


	3. Case

		Range min.: 4
		Range max.: 12

			Parameters: [5, 13, 2]

		Range: [5, 7, 9, 11]
		  Sum:  32


	4. Case

		Range min.: 2
		Range max.: 5

			Parameters: [3, 6, 2]

		Range: [3, 5]
		  Sum:  8


	5. Case

		Range min.: 0
		Range max.: 7

			Parameters: [1, 8, 2]

		Range: [1, 3, 5, 7]
		  Sum:  16

Process finished with exit code 0

"""