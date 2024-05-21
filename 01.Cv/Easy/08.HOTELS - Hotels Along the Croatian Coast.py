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


def infExtrc(lineInf, lineHtls):

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


if __name__ == "__main__":

    print("Input:")
    print(InputRaw_Str)
    print()

    InputStr_Lst = InputRaw_Str.split("\n")

    # print(InputStr_Lst)

    caseCnt = 1

    for lineInf, lineHtls in zip(InputStr_Lst[::2], InputStr_Lst[1::2]):

        print(f"\t{caseCnt}. Case")
        print()

        caseCnt += 1

        htlNum, mnyNum, Htls = infExtrc(lineInf, lineHtls)

        # htlNum, mnyNum = list(map(int, lineInf.split()))
        # print(f"\t\tNum. of hotels: {htlNum}")
        # print(f"\t\tNum. of money:  {mnyNum}")
        # print()
        #
        # Htls = list(map(int, lineHtls.split()))
        # print(f"\t\tHotels: {Htls}")
        # print()

        maxMny, maxHtls = fndMaxMny_TwoPrt(Htls, mnyNum)

        print()

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

        print(f"\t\tMax money: {maxMny}")
        print(f"\t\tMax hotels: {maxHtls}")

        print("\n")


"""__Output__"""
"""
Input:
5 12
2 1 3 4 5
4 9
7 3 5 6

	1. Case

		Num. of hotels: 5
		Num. of money:  12

		Hotels: [2, 1, 3, 4, 5]

			0 | 1 : [2] (2)
			0 | 2 : [2, 1] (3)
			0 | 3 : [2, 1, 3] (6)
			0 | 4 : [2, 1, 3, 4] (10)
			0 | 5 : [2, 1, 3, 4, 5] (15)
			1 | 5 : [1, 3, 4, 5] (13)
			2 | 5 : [3, 4, 5] (12)

		Max money: [3, 4, 5]
		Max hotels: 12


	2. Case

		Num. of hotels: 4
		Num. of money:  9

		Hotels: [7, 3, 5, 6]

			0 | 1 : [7] (7)
			0 | 2 : [7, 3] (10)
			1 | 2 : [3] (3)
			1 | 3 : [3, 5] (8)
			1 | 4 : [3, 5, 6] (14)
			2 | 4 : [5, 6] (11)
			3 | 4 : [6] (6)

		Max money: [3, 5]
		Max hotels: 8



Process finished with exit code 0

"""