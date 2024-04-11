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

"""29374710 	10783 	Odd Sum 	Accepted 	PYTH3 	0.020 	2024-04-11 13:34:52"""

if __name__ == '__main__':

#     InputRaw_Str = """
# 5
# 1
# 5
# 3
# 5
# 4
# 12
# 2
# 5
# 0
# 7
# """

    # InputRaw_Str = InputRaw_Str[1:-1]

    # InputStr_Lst = list(map(int, InputRaw_Str.split("\n")))

    # print("Input:", InputStr_Lst)
    # print()

    # casesNum = InputStr_Lst[0]
    casesNum = int(input())

    # print(f"Num. of cases: {casesNum}")
    # print()

    # inputLst = InputStr_Lst[1:]

    for case in range(casesNum):

        # rngMin = inputLst[case*2]
        rngMin = int(input())
        # rngMax = inputLst[case*2 + 1]
        rngMax = int(input())

        # print(f"\t{case+1}. Case")
        # print()

        # print(f"\t\tRange min.: {rngMin}")
        # print(f"\t\tRange max.: {rngMax}")
        # print()

        if rngMin % 2 == 0:
            oddMin = rngMin + 1
        else:
            oddMin = rngMin

        oddMax = rngMax + 1

        # print(f"\t\t\tParameters: [{oddMin}, {oddMax}, 2]")
        # print()

        oddRange = [* range(oddMin, oddMax, 2)]

        # print(f"\t\tRange: {oddRange}")
        # print(f"\t\t  Sum:  {sum(oddRange)}")
        print(f"Case {case+1}: {sum(oddRange)}")

        # if case < casesNum - 1:
        #     print("\n")
