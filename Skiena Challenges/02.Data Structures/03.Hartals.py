"""

Hartals

    Input:
        The first line of the input consists of a single integer T giving the number of test cases
        to follow. The first line of each test case contains an integer N (7 ≤ N ≤ 3, 650), giving
        the number of days over which the simulation must be run. The next line contains
        another integer P (1 ≤ P ≤ 100) representing the number of political parties. The ith
        of the next P lines contains a positive integer hi (which will never be a multiple of 7)
        giving the hartal parameter for party i (1 ≤ i ≤ P ).

    Output:
        For each test case, output the number of working days lost on a separate line.


    Sample:

        2
        14
        3
        3
        4
        8
            => 5

        100
        4
        12
        15
        25
        40
            => 15

"""

Input = ["2 14 3 3 4 8 100 4 12 15 25 40"]