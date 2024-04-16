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

print("Input:")
print(InputRaw_Str)
print()

InputStr_Lst = InputRaw_Str.split("\n")

# print(InputStr_Lst)

caseCnt = 1

for lineInf, lineHtls in zip(InputStr_Lst[::2], InputStr_Lst[1::2]):

    print(f"\t{caseCnt}. Case")
    print()

    htlNum, mnyNum = list(map(int, lineInf.split()))
    print(f"\t\tNum. of hotels: {htlNum}")
    print(f"\t\tNum. of money:  {mnyNum}")
    print()

    Htls = list(map(int, lineHtls.split()))
    print(f"\t\tHotels: {Htls}")
    print()

    for sH, strHtl in enumerate(Htls):

        for eH, endHtl in enumerate(Htls[sH:]):

            print(f"\t\t\t{Htls[sH:sH+eH+1]}")

    print("\n")