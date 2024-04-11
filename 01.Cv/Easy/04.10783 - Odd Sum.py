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

InputRaw_Str = """
2
1
5
3
5
"""

InputRaw_Str = InputRaw_Str[1:-1]

print("Input:")

print(InputRaw_Str)
print()

InputStr_Lst = list(map(int, InputRaw_Str.split("\n")))

print(InputStr_Lst)
print()

# casesNum = int(InputStr_Lst[0])
casesNum = InputStr_Lst[0]

print(f"Num. of cases: {casesNum}")
print()

inputLst = InputStr_Lst[1:]

for case in range(casesNum):

    # rngMin = int(inputLst[case*2])
    # rngMax = int(inputLst[case*2 + 1])
    rngMin = inputLst[case*2]
    rngMax = inputLst[case*2 + 1]

    print(f"\t{case+1}. Case")
    print()

    print(f"\t\tRange min.: {rngMin}")
    print(f"\t\tRange max.: {rngMax}")
    print("\n")


"""__Output__"""
"""
Input:
2
1
5
3
5

[2, 1, 5, 3, 5]

Num. of cases: 2

	1. Case

		Range min.: 1
		Range max.: 5


	2. Case

		Range min.: 3
		Range max.: 5



Process finished with exit code 0

"""