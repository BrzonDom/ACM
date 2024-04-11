"""
11044 - Searching for Nessy
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=121&page=show_problem&problem=1985

    Given a grid of n rows and m columns representing the
    loch, 6 ≤ n, m ≤ 10000, find the minimum number s of sonar
    beams you must put in the square such that we can control
    every position in the grid, with the following conditions:

      - one sonar occupies one position in the grid; the sonar
        beam controls its own cell and the contiguous cells;
      - the border cells do not need to be controlled, because
        Nessy cannot hide there (she is too big).

    Input:
            The first line of the input contains an integer, t, indicating the number of test cases. For each test case,
        there is a line with two numbers separated by blanks, 6 ≤ n, m ≤ 10000, that is, the size of the grid (n
        rows and m columns).

    Output:
            For each test case, the output should consist of one line showing the minimum number of sonars that
        verifies the conditions above.


    Sample:
        3
        6 6
        7 7
        9 13
            =>  4
                4
                12

"""

InputOrg_Str = """
3
6 6
7 7
9 13
"""

InputOrg_Str = InputOrg_Str[1:-1]

print("Input:")
print(InputOrg_Str)