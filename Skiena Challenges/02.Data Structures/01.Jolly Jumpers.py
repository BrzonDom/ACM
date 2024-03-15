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

        1 4 2 3
            => Jolly

        1 4 2 -1 6
            => Not Jolly

"""


if __name__ == '__main__':

    seqLst = [[1, 4, 2, 3],
              [1, 4, 2, -1, 6]]

    for seq in seqLst:

        print(f"\tSequence: {seq}\n")

        lenSeq = len(seq)

        jolly = set()

        # for n in range(lenSeq-1):
        #     jolly[n+1] = False

        # print(f"\t{jolly}\n")

        prev = seq[0]

        for itm in seq[1:]:
            print(f"\t\t\t|{prev} - {itm}| = {abs(prev - itm)}")

            jolly.add(abs(prev - itm))

            prev = itm

        print()
        print(f"\t\t\t{jolly}\n")

        isJolly = True

        # for key in jolly:
            # if jolly[key] == False:
            #
            #     isJolly = False
            #     break

        for n in range(1, lenSeq):
            if n not in jolly:

                isJolly = False
                break

        if isJolly:
            print(f"\t\tSequence is Jolly")

        else:
            print("\t\tSequence is Not Jolly")

        print("\n")
