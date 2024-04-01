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

"""__Solution 1__"""
# """
import copy
from sys import stdin

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

cases = int(stdin.readline())

for case in range(cases):

    dayNum = int(stdin.readline())

    partNum = int(stdin.readline())

    hartLst = []

    for _ in range(partNum):
        hartLst.append(int(stdin.readline()))

    # print(f"\tDays: {dayNum}")
    # print(f"\tHartals: {hartLst}")
    # print()

    lostDays = 0
    hartVal = copy.deepcopy(hartLst)

    for day in range(1, dayNum + 1):
        # print(f"\t\t{day:2} {day % 7} : {dayPrnt[(day % 7)]}")

        lost = False

        for h, hart in enumerate(hartVal):

            if day == hartLst[h]:
                hartLst[h] += hart

                if not ((day % 7) == 0 or (day % 7) == 6) and not lost:
                    # print("\t\t\t\t\tX")
                    lostDays += 1
                    lost = True

    print(lostDays)
# """


"""__Solution 2__"""
"""
from sys import stdin

def readCase():

    dayNum = int(stdin.readline())

    partNum = int(stdin.readline())

    return dayNum, [int(stdin.readline()) for _ in range(partNum)]


def lostDays(dayNum, hartLst):

    calendar = [0 for _ in range(dayNum)]

    for hart in hartLst:

        curHart = hart

        while curHart <= dayNum:

            if not ((curHart-1) % 7 == 6 or (curHart-1) % 7 == 5):
                calendar[curHart-1] = 1

            curHart += hart

    return sum(calendar)

cases = int(stdin.readline())

for c in range(cases):

    dayNum, hartLst = readCase()

    print(lostDays(dayNum, hartLst))
    
"""