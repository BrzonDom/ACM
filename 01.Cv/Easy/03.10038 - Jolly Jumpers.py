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

InputRaw_Str = """
4 1 4 2 3
5 1 4 2 -1 6
"""

InputRaw_Str = InputRaw_Str[1:-1]

print("Input:")
print(InputRaw_Str)
print()

InputRaw_Lst = InputRaw_Str.split("\n")

for inCnt, InputStr in enumerate(InputRaw_Lst):

    Input = list(map(int, InputStr.split()))

    # print(f"\t{Input}")
    # print()

    lenSeq, seq = Input[0], Input[1:]

    print(f"\t{inCnt+1}. Sequence: {seq}")
    print(f"\t\t Lenght: {lenSeq}\n")
    print()

    jolly = set()

    isJolly = True

    prev = seq[0]

    for nxt in seq[1:]:
        abVal = abs(prev - nxt)

        print(f"\t\t\t|{prev} - {nxt}| = {abVal}")

        if abVal in jolly or abVal <= 0 or abVal >= lenSeq:
            isJolly = False
            break

        else:
            jolly.add(abVal)

        prev = nxt

    print()
    print(f"\t\t\t{jolly}\n")

    # isJolly = True
    #
    # for n in range(1, lenSeq):
    #     if n not in jolly:
    #
    #         isJolly = False
    #         break

    if isJolly:
        print(f"\t\tSequence is Jolly")

    else:
        print("\t\tSequence is Not Jolly")

    print("\n")