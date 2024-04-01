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

dayPrnt = {
    0 : "Saturday",
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday"
    # 7 : "Saturday"
}


Input_Str = "2 14 3 3 4 8 100 4 12 15 25 40"

Input = list(map(int, Input_Str.split()))

print(f"Input string:   \"{Input_Str}\"")
print(f"Input:         {Input}")
print("\n")

Input_read = copy.deepcopy(Input)

caseNum = Input_read.pop(0)

for case in range(caseNum):

    dayNum = Input_read.pop(0)

    partNum = Input_read.pop(0)

    hartLst = []

    for h in range(partNum):
            hartLst.append(Input_read.pop(0))

    print(f"\tDays: {dayNum}")
    print(f"\tParties: {partNum}")
    print()
    print(f"\tHartals: {hartLst}")
    print()

    hartVal = copy.deepcopy(hartLst)

    lostDays = 0

    for day in range(1, dayNum + 1):
        print(f"\t\t{day:2} {day % 7} : {dayPrnt[(day % 7)]}")

        lost = False

        for h, hart in enumerate(hartVal):

            if day == hartLst[h]:
                hartLst[h] += hart

                if not ((day % 7) == 0 or (day % 7) == 6) and not lost:
                    print(f"\t\t\t\t\tX {hart}")
                    lostDays += 1
                    lost = True

                elif lost:
                    print(f"\t\t\t\t\tX {hart}")

        if (day % 7) == 6:
            print("\t\t\t\t\tO")

        if (day % 7) == 0:
            print("\t\t\t\t\tO")


    print(f"\n\tDays lost: {lostDays}")
    print("\n")


# """
Input_ext = copy.deepcopy(Input)

Cases = [[] for _ in range(Input[0])]

Input_ext = Input_ext[1:]

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

    for d in range(1, Cases[c][0] + 1):
        print(f"\t\t{d:2} {d % 7} : {dayPrnt[(d % 7)]}")

        lost = False

        for cs, case in enumerate(Cases[c][1]):

            if d == Hartals[cs]:
                Hartals[cs] += case

                if not ((d % 7) == 0 or (d % 7) == 6) and not lost:
                    print(f"\t\t\t\t\tX")
                    lostDays += 1
                    lost = True

                elif lost:
                    print("\t\t\t\t\tX")

        if (d % 7) == 6:
            print("\t\t\t\t\tFo")

        if (d % 7) == 0:
            print("\t\t\t\t\tSo")


    print(f"\n\tDays lost: {lostDays}")
    print("\n")
# """


"""__Output__"""
"""
Input string:   "2 14 3 3 4 8 100 4 12 15 25 40"
Input:         [2, 14, 3, 3, 4, 8, 100, 4, 12, 15, 25, 40]


	Days: 14
	Cases: [3, 4, 8]

		 1 1 : Sunday
		 2 2 : Monday
		 3 3 : Tuesday
					X
		 4 4 : Wednesday
					X
		 5 5 : Thursday
		 6 6 : Friday
					Fo
		 7 0 : Saturday
					So
		 8 1 : Sunday
					X
					X
		 9 2 : Monday
					X
		10 3 : Tuesday
		11 4 : Wednesday
		12 5 : Thursday
					X
					X
		13 6 : Friday
					Fo
		14 0 : Saturday
					So

	Days lost: 5


	Days: 100
	Cases: [12, 15, 25, 40]

		 1 1 : Sunday
		 2 2 : Monday
		 3 3 : Tuesday
		 4 4 : Wednesday
		 5 5 : Thursday
		 6 6 : Friday
					Fo
		 7 0 : Saturday
					So
		 8 1 : Sunday
		 9 2 : Monday
		10 3 : Tuesday
		11 4 : Wednesday
		12 5 : Thursday
					X
		13 6 : Friday
					Fo
		14 0 : Saturday
					So
		15 1 : Sunday
					X
		16 2 : Monday
		17 3 : Tuesday
		18 4 : Wednesday
		19 5 : Thursday
		20 6 : Friday
					Fo
		21 0 : Saturday
					So
		22 1 : Sunday
		23 2 : Monday
		24 3 : Tuesday
					X
		25 4 : Wednesday
					X
		26 5 : Thursday
		27 6 : Friday
					Fo
		28 0 : Saturday
					So
		29 1 : Sunday
		30 2 : Monday
					X
		31 3 : Tuesday
		32 4 : Wednesday
		33 5 : Thursday
		34 6 : Friday
					Fo
		35 0 : Saturday
					So
		36 1 : Sunday
					X
		37 2 : Monday
		38 3 : Tuesday
		39 4 : Wednesday
		40 5 : Thursday
					X
		41 6 : Friday
					Fo
		42 0 : Saturday
					So
		43 1 : Sunday
		44 2 : Monday
		45 3 : Tuesday
					X
		46 4 : Wednesday
		47 5 : Thursday
		48 6 : Friday
					Fo
		49 0 : Saturday
					So
		50 1 : Sunday
					X
		51 2 : Monday
		52 3 : Tuesday
		53 4 : Wednesday
		54 5 : Thursday
		55 6 : Friday
					Fo
		56 0 : Saturday
					So
		57 1 : Sunday
		58 2 : Monday
		59 3 : Tuesday
		60 4 : Wednesday
					X
					X
		61 5 : Thursday
		62 6 : Friday
					Fo
		63 0 : Saturday
					So
		64 1 : Sunday
		65 2 : Monday
		66 3 : Tuesday
		67 4 : Wednesday
		68 5 : Thursday
		69 6 : Friday
					Fo
		70 0 : Saturday
					So
		71 1 : Sunday
		72 2 : Monday
					X
		73 3 : Tuesday
		74 4 : Wednesday
		75 5 : Thursday
					X
					X
		76 6 : Friday
					Fo
		77 0 : Saturday
					So
		78 1 : Sunday
		79 2 : Monday
		80 3 : Tuesday
					X
		81 4 : Wednesday
		82 5 : Thursday
		83 6 : Friday
					Fo
		84 0 : Saturday
					So
		85 1 : Sunday
		86 2 : Monday
		87 3 : Tuesday
		88 4 : Wednesday
		89 5 : Thursday
		90 6 : Friday
					Fo
		91 0 : Saturday
					So
		92 1 : Sunday
		93 2 : Monday
		94 3 : Tuesday
		95 4 : Wednesday
		96 5 : Thursday
					X
		97 6 : Friday
					Fo
		98 0 : Saturday
					So
		99 1 : Sunday
		100 2 : Monday
					X

	Days lost: 15



Process finished with exit code 0

"""