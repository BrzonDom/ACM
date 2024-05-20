"""
10763 - Foreign Exchange
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=315&page=show_problem&problem=1704

    Your non-profit organization (iCORE - international Confederation of Revolver Enthusiasts) coor-
    dinates a very successful foreign student exchange program. Over the last few years, demand has
    sky-rocketed and now you need assistance with your task.
    The program your organization runs works as follows: All candidates are asked for their original
    location and the location they would like to go to. The program works out only if every student has a
    suitable exchange partner. In other words, if a student wants to go from A to B, there must be another
    student who wants to go from B to A. This was an easy task when there were only about 50 candidates,
    however now there are up to 500000 candidates!

    Input:
            The input file contains multiple cases. Each test case will consist of a line containing n – the number
        of candidates (1 ≤ n ≤ 500000), followed by n lines representing the exchange information for each
        candidate. Each of these lines will contain 2 integers, separated by a single space, representing the
        candidate’s original location and the candidate’s target location respectively. Locations will be repre-
        sented by nonnegative integer numbers. You may assume that no candidate will have his or her original
        location being the same as his or her target location as this would fall into the domestic exchange
        program. The input is terminated by a case where n = 0; this case should not be processed.

    Output:
            For each test case, print ‘YES’ on a single line if there is a way for the exchange program to work out,
        otherwise print ‘NO’

    Sample:
        10
        1 2
        2 1
        3 4
        4 3
        100 200
        200 100
        57 2
        2 57
        1 2
        2 1
        10
        1 2
        3 4
        5 6
        7 8
        9 10
        11 12
        13 14
        15 16
        17 18
        19 20
        0
            =>  YES
                NO

"""

InputRaw_Str = """
10
1 2
2 1
3 4
4 3
100 200
200 100
57 2
2 57
1 2
2 1
10
1 2
3 4
5 6
7 8
9 10
11 12
13 14
15 16
17 18
19 20
0
"""

InputRaw_Str = InputRaw_Str[1:-1]

print("Input:")
print(InputRaw_Str)
print()

InputLines = InputRaw_Str.split("\n")

caseNum = int(InputLines.pop(0))

while caseNum != 0:

    print(f"\tCases: {caseNum}")
    print()

    Cases = []

    DataTo = {}
    DataFr = {}

    for cs in range(caseNum):
        case = (list(map(int, InputLines.pop(0).split())))
        print(f"\t\t{case}")

        fr, to = case[0], case[1]

        Cases.append(case)

        if fr in DataFr:
            DataFr[fr] += 1
        else:
            DataFr[fr] = 1

        if to in DataTo:
            DataTo[to] += 1
        else:
            DataTo[to] = 1

    print("\n")

    caseNum = int(InputLines.pop(0))

