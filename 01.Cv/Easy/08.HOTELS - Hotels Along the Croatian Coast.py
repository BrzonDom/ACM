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

        htlNum, mnyNum = list(map(int, lineInf.split()))
        print(f"\t\tNum. of hotels: {htlNum}")
        print(f"\t\tNum. of money:  {mnyNum}")
        print()

        Htls = list(map(int, lineHtls.split()))
        print(f"\t\tHotels: {Htls}")
        print()

        mnyMax = 0
        htlMax = []

        for sH, strHtl in enumerate(Htls):

            for eH, endHtl in enumerate(Htls[sH:]):

                if sum(Htls[sH:sH+eH+1]) > mnyNum:
                    break

                elif sum(Htls[sH:sH+eH+1]) > mnyMax:
                    mnyMax = sum(Htls[sH:sH+eH+1])
                    htlMax = Htls[sH:sH+eH+1]

                print(f"\t\t\t{Htls[sH:sH + eH + 1]} ({sum(Htls[sH:sH + eH + 1])})")

            if mnyMax == mnyNum:
                break
        print()

        print(f"\t\tMax money: {mnyMax}")
        print(f"\t\tMax hotels: {htlMax}")

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

			[2] (2)
			[2, 1] (3)
			[2, 1, 3] (6)
			[2, 1, 3, 4] (10)
			[1] (1)
			[1, 3] (4)
			[1, 3, 4] (8)
			[3] (3)
			[3, 4] (7)
			[3, 4, 5] (12)

		Max money: 12
		Max hotels: [3, 4, 5]


	2. Case

		Num. of hotels: 4
		Num. of money:  9

		Hotels: [7, 3, 5, 6]

			[7] (7)
			[3] (3)
			[3, 5] (8)
			[5] (5)
			[6] (6)

		Max money: 8
		Max hotels: [3, 5]



Process finished with exit code 0

"""