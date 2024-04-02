"""

Jolly Jumpers

    A sequence of n > 0 integers is called a jolly jumper if the absolute values of the
    differences between successive elements take on all possible values 1 through n − 1.


    Inputs:
        Each line of input contains an integer n < 3, 000 followed by n integers representing the
        sequence.

    Output:
        For each line of input generate a line of output saying “Jolly” or “Not jolly”.


    Sample:

        4 1 4 2 3
            => Jolly

        5 1 4 2 -1 6
            => Not Jolly

"""
from sys import stdin

"""
def isJolly(seq, lenSeq):

    difSeq = [False] * lenSeq

    for i in range(0, lenSeq - 1):

        d = abs(seq[i] - seq[i + 1])

        if (d == 0 or d > lenSeq - 1 or difSeq[d] == True):
            return "Not Jolly"

        difSeq[d] = True

    return "Jolly"
# """

while True:

    try:
        inSeq = list(map(int, input().split()))

    except EOFError:
        break

    lenSeq, seq = inSeq[0], inSeq[1:]

    jolly = set()

    isJolly = True

    prev = seq[0]

    for nxt in seq[1:]:
        abVal = abs(prev - nxt)

        if abVal in jolly or abVal <= 0 or abVal >= lenSeq:
            isJolly = False
            break

        else:
            jolly.add(abVal)

        prev = nxt

    if isJolly:
        print("Jolly")

    else:
        print("Not jolly")

        

