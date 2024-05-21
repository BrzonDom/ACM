"""
HOTELS - Hotels Along the Croatian Coast
https://www.spoj.com/problems/HOTELS/

        There are N hotels along the beautiful Adriatic coast. Each hotel has its value in Euros.
    Sroljo has won M Euros on the lottery. Now he wants to buy a sequence of consecutive hotels, such that the sum
    of the values of these consecutive hotels is as great as possible - but not greater than M.
    You are to calculate this greatest possible total value.

    Input:
            In the first line of the input there are integers N and M (1 ≤ N ≤ 300 000, 1 ≤ M < 2^31).
        In the next line there are N natural numbers less than 10^6, representing the hotel values in the order
        they lie along the coast.

    Output:
            Print the required number (it will be greater than 0 in all of the test data).


    Sample:
        5 12
        2 1 3 4 5
        4 9
        7 3 5 6
            =>  12
                8

"""

InputRaw_Str = """
5 12
2 1 3 4 5
4 9
7 3 5 6
"""

InputRaw_Str = InputRaw_Str[1:-1]


def infExtrc_Prt(lineInf, lineHtls):

    htlNum, mnyNum = list(map(int, lineInf.split()))
    print(f"\t\tNum. of hotels: {htlNum}")
    print(f"\t\tNum. of money:  {mnyNum}")
    print()

    Htls = list(map(int, lineHtls.split()))
    print(f"\t\tHotels: {Htls}")
    print()

    return htlNum, mnyNum, Htls


def fndMaxMny_ForPrt(Htls, mnyNum):

    maxMny = 0
    maxHtls = []

    for sH, strHtl in enumerate(Htls):

        for eH, endHtl in enumerate(Htls[sH:]):

            if sum(Htls[sH:sH + eH + 1]) > mnyNum:
                break

            elif sum(Htls[sH:sH + eH + 1]) > maxMny:
                maxMny = sum(Htls[sH:sH + eH + 1])
                maxHtls = Htls[sH:sH + eH + 1]

            print(f"\t\t\t{Htls[sH:sH + eH + 1]} ({sum(Htls[sH:sH + eH + 1])})")

        if maxMny == mnyNum:
            break
    print()

    return maxMny, maxHtls


def fndMaxMny_TwoPrt(Htls, mnyNum):

    htlNum = len(Htls)

    strHs = 0
    endHs = 1

    maxMny = 0
    maxHtls = []

    while endHs <= htlNum:

        curHtls = Htls[strHs:endHs]
        sumHtls = sum(curHtls)

        print(f"\t\t\t{strHs} | {endHs} : {Htls[strHs:endHs]} ({sumHtls})")

        if sumHtls < mnyNum:
            endHs += 1

            if sumHtls > maxMny:
                maxMny = sumHtls
                maxHtls = curHtls

        elif sumHtls > mnyNum:
            strHs += 1

        elif sumHtls == mnyNum:
            maxMny = mnyNum
            maxHtls = curHtls

            return maxHtls, maxMny

    return maxHtls, maxMny


"""__Code__"""

def infExtrc(lineInf, lineHtls):

    htlNum, mnyNum = list(map(int, lineInf.split()))

    Htls = list(map(int, lineHtls.split()))

    return htlNum, mnyNum, Htls


def fndMaxMny_Two(Htls, mnyNum):

    htlNum = len(Htls)

    strHs = 0
    endHs = 1

    maxMny = 0
    maxHtls = []

    while endHs <= htlNum:

        curHtls = Htls[strHs:endHs]
        sumHtls = sum(curHtls)

        if sumHtls < mnyNum:
            endHs += 1

            if sumHtls > maxMny:
                maxMny = sumHtls
                maxHtls = curHtls

        elif sumHtls > mnyNum:
            strHs += 1

        elif sumHtls == mnyNum:
            maxMny = mnyNum
            maxHtls = curHtls

            return maxHtls, maxMny

    return maxHtls, maxMny


if __name__ == "__main__":

    print("Input:")
    print(InputRaw_Str)
    print()

    lineInf = input()
    lineHtls = input()

    # htlNum, mnyNum, Htls = infExtrc_Prt(lineInf, lineHtls)
    htlNum, mnyNum, Htls = infExtrc(lineInf, lineHtls)

    # print(f"\t\tNum. of hotels: {htlNum}")
    # print(f"\t\tNum. of money:  {mnyNum}")
    # print()

    # print(f"\t\tHotels: {Htls}")
    # print()

    # maxHtls, maxMny = fndMaxMny_TwoPrt(Htls, mnyNum)
    maxHtls, maxMny = fndMaxMny_Two(Htls, mnyNum)

    print(maxMny)

    # print()

    # maxMny, maxHtls = fndMaxMny_ForPrt(Htls, mnyNum)

    # maxMny = 0
    # maxHtls = []
    #
    # for sH, strHtl in enumerate(Htls):
    #
    #     for eH, endHtl in enumerate(Htls[sH:]):
    #
    #         if sum(Htls[sH:sH+eH+1]) > mnyNum:
    #             break
    #
    #         elif sum(Htls[sH:sH+eH+1]) > maxMny:
    #             maxMny = sum(Htls[sH:sH+eH+1])
    #             maxHtls = Htls[sH:sH+eH+1]
    #
    #         print(f"\t\t\t{Htls[sH:sH + eH + 1]} ({sum(Htls[sH:sH + eH + 1])})")
    #
    #     if maxMny == mnyNum:
    #         break
    # print()

    # print(f"\t\tMax money: {maxMny}")
    # print(f"\t\tMax hotels: {maxHtls}")

    # print("\n")


