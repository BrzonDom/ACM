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