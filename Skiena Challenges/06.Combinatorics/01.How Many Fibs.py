"""

How Many Fibs ?

    Inputs:
        The input contains several test cases. Each test case consists of two non-negative integer
        numbers a and b. Input is terminated by a = b = 0. Otherwise, a ≤ b ≤ 10^(100).
        The numbers a and b are given with no superfluous leading zeros.


    Output:
        For each test case output on a single line the number of Fibonacci numbers f_i with
        a ≤ f_i ≤ b


    Samples:

        10 100
            => 5

        1234567890 9876543210
            => 4

        0 0
            =>

"""

def FibNum_Recu(fibIdx):

    if fibIdx == 0:
        return 0

    elif fibIdx == 1 or fibIdx == 2:
        return 1

    else:
        return FibNum_Recu(fibIdx - 1) + FibNum_Recu(fibIdx - 2)


def FibNum_Iter(fibIdx):

    if fibIdx == 0:
        return 0

    elif fibIdx == 1 or fibIdx == 2:
        return 1

    else:

        num_1 = 1
        num_2 = 1

        for _ in range(2, fibIdx):

            num = num_1 + num_2

            num_1, num_2 = num_2, num

        return num


FibSequence = [0, 1]

def FibNum_DP(fibIdx):

    if fibIdx < len(FibSequence):
        return FibSequence[fibIdx]

    else:
        FibSequence.append(FibNum_DP(fibIdx - 1) + FibNum_DP(fibIdx - 2))
        return FibSequence[fibIdx]


if __name__ == '__main__':

    print("How Many Fibs:\n")

    print("\tFibonacci sequence drive code:\n")

    maxFibCnt = 10

    num_1 = 0
    print("\t\tf_0  = 0")

    num_2 = 1
    print("\t\tf_1  = 1")

    fibCnt = 1

    while fibCnt < maxFibCnt:
        num_1, num_2 = num_2, num_1 + num_2
        fibCnt += 1

        print(f"\t\tf_{fibCnt:<2} = {num_2}")

    print("\n")

    print("\tFibonacci number recursive:\n")

    fibIndex = 9

    fibNum = FibNum_Recu(fibIndex)

    print(f"\t\tf_{fibIndex} = {fibNum}")

    print("\n")

    print("\tFibonacci number iteratively:\n")

    fibIndex = 9

    fibNum = FibNum_Iter(fibIndex)

    print(f"\t\tf_{fibIndex} = {fibNum}")

    print("\n")

    print("\tFibonacci number dynamically:\n")

    fibNum = FibNum_DP(fibIndex)

    print(f"\t\tf_{fibIndex} = {fibNum}")
