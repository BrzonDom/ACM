import copy
from sys import stdin

days = {
    0 : "Saturday",
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday"
    # 7 : "Saturday"
}

cases = int(stdin.readline())

for case in range(cases):

    dayNum = int(stdin.readline())

    partNum = int(stdin.readline())

    hartLst = []


    for _ in range(partNum):
        hartLst.append(int(stdin.readline()))

    lostDays = 0

    for d in range(1, dayNum):
        print(f"\t\t{d:2} {d % 7} : {days[(d % 7)]}")

        lost = False

        for h, hart in enumerate(hartLst):

            if d == hartLst[h]:
                hartLst[h] += hart

                if not ((d % 7) == 6 or (d % 7) == 7) and not lost:
                    print("\t\t\t\t\tX")
                    lostDays += 1
                    lost = True

                elif lost:
                    print("\t\t\t\t\tX")


    print(f"\n\tDays lost: {lostDays}")
    print("\n")