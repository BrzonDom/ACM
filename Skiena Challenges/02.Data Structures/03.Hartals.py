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

days = {
    0: "Saturday",
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday"
    # 7 : "Saturday"
}

# days = {
#     0 : "Sunday",
#     1 : "Monday",
#     2 : "Tuesday",
#     3 : "Wednesday",
#     4 : "Thursday",
#     5 : "Friday",
#     6 : "Saturday"
# }


Input_Str = "2 14 3 3 4 8 100 4 12 15 25 40"

Input = list(map(int, Input_Str.split()))

print(f"Input string:   \"{Input_Str}\"")
print(f"Input:         {Input}")
print("\n")

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

    print(f"\tDays: {Cases[c][0]}")
    print(f"\tCases: {Cases[c][1]}")
    print()

    lostDays = 0

    Hartals = copy.deepcopy(Cases[c][1])

    for d in range(1, Cases[c][0]):
        print(f"\t\t{d:2} {d % 7} : {days[(d % 7)]}")

        lost = False

        for cs, case in enumerate(Cases[c][1]):

            if d == Hartals[cs]:
                Hartals[cs] += case

                if not ((d % 7) == 6 or (d % 7) == 7) and not lost:
                    print("\t\t\t\t\tX")
                    lostDays += 1
                    lost = True

                elif lost:
                    print("\t\t\t\t\tX")


    print(f"\n\tDays lost: {lostDays}")
    print("\n")