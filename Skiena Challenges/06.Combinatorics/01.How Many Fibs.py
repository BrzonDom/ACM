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


if __name__ == '__main__':

    print("How Many Fibs:\n")

    print("\tFibonacci numbers:\n")

    maxFibCnt = 10

    num_1 = 0
    print("\t\tf_0  = 0")

    num_2 = 1
    print("\t\tf_1  = 1")

    fibCnt = 2

    while fibCnt < maxFibCnt:
        num_1, num_2 = num_2, num_1 + num_2
        fibCnt += 1

        print(f"\t\tf_{fibCnt:<2} = {num_2}")
