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
import copy

Input_Str = "2 14 3 3 4 8 100 4 12 15 25 40"

Input = list(map(int, Input_Str.split()))

print(f"Input string:   \"{Input_Str}\"")
print(f"Input:         {Input}")
print()

Input_ext = copy.deepcopy(Input)

Cases = [[] for _ in range(Input[0])]

Input_ext = Input_ext[1:]

# print(Input_ext)

for c in range(Input[0]):

    Cases[c].append(Input_ext[0])
    Cases[c].append([])
    Input_ext = Input_ext[1:]

    for p in range(1, Input_ext[0] + 1):
        Cases[c][1].append(Input_ext[p])

    Input_ext = Input_ext[Input_ext[0] + 1:]

print(f"\tCases: {Cases}")