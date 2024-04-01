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

# """
cases = int(stdin.readline())

for case in range(cases):

    dayNum = int(stdin.readline())

    partNum = int(stdin.readline())

    hartLst = []

    for _ in range(partNum):
        hartLst.append(int(stdin.readline()))
# """

    """
    casesTst = [[14, 3, 3, 4, 8], [100, 4, 12, 15, 25, 40]]
    
    for case in casesTst:
    
        dayNum = case[0]
    
        partNum = case[1]
    
        hartLst = case[2:]
    # """

    # print(f"\tDays: {dayNum}")
    # print(f"\tHartals: {hartLst}")
    # print()

    lostDays = 0
    hartState = copy.deepcopy(hartLst)

    for d in range(1, dayNum):
        # print(f"\t\t{d:2} {d % 7} : {days[(d % 7)]}")

        lost = False

        for h, hart in enumerate(hartLst):

            if d == hartState[h]:
                hartState[h] += hart

                if not ((d % 7) == 6 or (d % 7) == 7) and not lost:
                    # print("\t\t\t\t\tX")
                    lostDays += 1
                    lost = True

                # elif lost:
                    # print("\t\t\t\t\tX")


    # print(f"\n\tDays lost: {lostDays}")
    # print("\n")

    print(lostDays)

