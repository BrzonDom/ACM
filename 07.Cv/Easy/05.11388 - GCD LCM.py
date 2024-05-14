"""
11388 - GCD LCM
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=189&page=show_problem&problem=2383

        The GCD of two positive integers is the largest integer that divides both the integers without any
    remainder. The LCM of two positive integers is the smallest positive integer that is divisible by both
    the integers. A positive integer can be the GCD of many pairs of numbers. Similarly, it can be the
    LCM of many pairs of numbers. In this problem, you will be given two positive integers. You have to
    output a pair of numbers whose GCD is the first number and LCM is the second number.

    Input:
            The first line of input will consist of a positive integer T . T denotes the number of cases. Each of the
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

InputOrg_Raw = InputOrg_Raw[1:-1]

print("Input:")
print(InputOrg_Raw)
print()

InputLines = InputOrg_Raw.split("\n")

caseNum = int(InputLines.pop(0))

print(f"\tCases: {caseNum}")
print()

for cs in range(caseNum):

    inLine = InputLines.pop(0)
    nums = list(map(int, inLine.split()))

    print(f"\t\t{cs+1}. Case")
    print()
    # print(f"\t\t\t{inLine}")
    print(f"\t\t\t1.Num: {nums[0]}")
    print(f"\t\t\t2.Num: {nums[1]}")
    print()