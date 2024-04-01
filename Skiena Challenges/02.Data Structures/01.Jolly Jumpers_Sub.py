from sys import stdin

def isJolly(seq, lenSeq):

    difSeq = [False] * lenSeq

    for i in range(0, lenSeq - 1):

        d = abs(seq[i] - seq[i + 1])

        if (d == 0 or d > lenSeq - 1 or difSeq[d] == True):
            return "Not Jolly"

        difSeq[d] = True

    return "Jolly"


while True:

    try:
        seq = list(map(int, input().split()))

    except EOFError:
        break

# for strSeq in stdin:

    lenSeq = seq[0]

    seq = seq[1:]

    print(isJolly(seq, lenSeq))

    """
    jolly = set()

    prev = seq[0]

    for itm in seq[1:]:

        jolly.add(abs(prev - itm))

        prev = itm

    isJolly = True

    for n in range(1, lenSeq):
        if n not in jolly:
            isJolly = False
            break

    if isJolly:
        print("Jolly")

    else:
        print("Not Jolly")
    # """
        

