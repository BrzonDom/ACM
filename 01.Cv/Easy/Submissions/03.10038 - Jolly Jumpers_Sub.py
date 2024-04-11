"""
10038 - Jolly Jumpers
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=30&page=show_problem&problem=979

    A sequence of n > 0 integers is called a jolly jumper if the absolute values of the
    differences between successive elements take on all possible values 1 through n − 1.


    Inputs:
        Each line of input contains an integer n < 3, 000 followed by n integers representing the
        sequence.

    Output:
        For each line of input generate a line of output saying “Jolly” or “Not jolly”.


    Sample:

        4 1 4 2 3
        5 1 4 2 -1 6
            =>  Not Jolly
                Jolly

"""

"""29374594 	10038 	Jolly Jumpers 	Accepted 	PYTH3 	0.030 	2024-04-11 13:08:18"""

if __name__ == '__main__':

#     InputRaw_Str = """
# 4 1 4 2 3
# 5 1 4 2 -1 6
# """
#
#     InputRaw_Str = InputRaw_Str[1:-1]
#
#     print("Input:")
#     print(InputRaw_Str)
#     print()
#
#     InputStr_Lst = InputRaw_Str.split("\n")

    # for inCnt, InputStr in enumerate(InputStr_Lst):
    #
    #     Input = list(map(int, InputStr.split()))

    # inCnt = 0

    while True:

        try:
            inSeq = list(map(int, input().split()))

        except EOFError:
            break

        # inCnt += 1

        lenSeq, seq = inSeq[0], inSeq[1:]

        # print(f"\t{inCnt}. Sequence: {seq}")
        # print(f"\t\t Lenght: {lenSeq}\n")

        jolly = set()

        isJolly = True

        prev = seq[0]

        for nxt in seq[1:]:
            abVal = abs(prev - nxt)

            # print(f"\t\t\t|{prev} - {nxt}| = {abVal}")

            if abVal in jolly or abVal <= 0 or abVal >= lenSeq:
                isJolly = False
                break

            else:
                jolly.add(abVal)

            prev = nxt

        # print()
        # print(f"\t\t\t{jolly}\n")

        if isJolly:
            # print(f"\t\tSequence is Jolly")
            print("Jolly")

        else:
            # print("\t\tSequence is Not Jolly")
            print("Not jolly")

            # print("\n")

            # if inCnt < len(InputStr_Lst) - 1:
            #     print("\n")
