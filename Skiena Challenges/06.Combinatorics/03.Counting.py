"""

Counting

        Gustavo knows how to count, but he is just now learning how to write numbers.
    He has already learned the digits 1, 2, 3, and 4. But he does not yet realize that 4 is
    different than 1, so he thinks that 4 is just another way to write 1.
        He is having fun with a little game he created: he makes numbers with the four digits
    that he knows and sums their values. For example:
        132 = 1 + 3 + 2 = 6
        112314 = 1 + 1 + 2 + 3 + 1 + 1 = 9 (remember that Gustavo thinks that 4 = 1)

        Gustavo now wants to know how many such numbers he can create whose sum is a
    number n. For n = 2, he can make 5 numbers: 11, 14, 41, 44, and 2. (He knows how to
    count up beyond five, just not how to write it.) However, he can’t figure out this sum
    for n greater than 2, and asks for your help.

    Input:

            Input will consist of an arbitrary number of integers n such that 1 ≤ n ≤ 1, 000. You
        must read until you reach the end of file.

    Output:

            For each integer read, output an single integer on a line stating how many numbers
        Gustavo can make such that the sum of their digits is equal to n.


    Sample:

        2
        3
            =>  5
                13

"""
import copy
from itertools import combinations


InputRaw_Str = """
2
3
"""

valDict = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 1
}

numSet = {'1', '2', '3', '4'}

print(numSet)
print()
# print(type(numSet))

for n in range(10, 21):

    minDig = n // 3

    if n % 3 == 0:

        combLst = [[3] * minDig]

    else:

        if n % 3 == 1:

            combLst = [[3] * minDig + [1]]

            combLst += [[3] * (minDig - 1) + [2, 2]]

        else:

            combLst = [[3] * minDig + [2]]

        minDig += 1

    print(f"\tNum: {n:2}\n\t\tMinDig.: {minDig:2}\n")

    print(f"\t\t{minDig:2}: {combLst}")
    print()
print()

maxDigSet = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# maxDigSet = [1, 1, 1]

maxDig = len(maxDigSet)

minDig = maxDig // 3

if maxDig % 3 != 0:
    minDig += 1

digSetDict = {}

digSetDict[maxDig] = [maxDigSet]

print(f"\tNum.: {maxDig}")
print(f"\t\tMinDig: {minDig}")
# print(f"\t\tMaxDigSet: {maxDigSet}")
print()

print(f"\t\t\t{maxDig:2}: {digSetDict[maxDig]}")

for dig in range(maxDig - 1, minDig - 1, -1):

    digSetDict[dig] = []

    for digSet in digSetDict[dig+1]:
        if digSet[-1] == 1 and digSet[-2] == 1:
            newDigSet = copy.deepcopy(digSet)

            newDigSet = newDigSet[:-2] + [2]
            newDigSet.sort(reverse=True)

            if newDigSet not in digSetDict[dig]:
                digSetDict[dig] += [newDigSet]

        if 1 in digSet and 2 in digSet:
            newDigSet = copy.deepcopy(digSet)

            newDigSet.remove(1)
            newDigSet.remove(2)
            newDigSet += [3]
            newDigSet.sort(reverse=True)

            if newDigSet not in digSetDict[dig]:
                digSetDict[dig] += [newDigSet]

    print(f"\t\t\t{dig:2}: {digSetDict[dig]}")


"""__Output__"""
"""
{'4', '2', '3', '1'}

	Num: 10
		MinDig.:  4

		 4: [[3, 3, 3, 1], [3, 3, 2, 2]]

	Num: 11
		MinDig.:  4

		 4: [[3, 3, 3, 2]]

	Num: 12
		MinDig.:  4

		 4: [[3, 3, 3, 3]]

	Num: 13
		MinDig.:  5

		 5: [[3, 3, 3, 3, 1], [3, 3, 3, 2, 2]]

	Num: 14
		MinDig.:  5

		 5: [[3, 3, 3, 3, 2]]

	Num: 15
		MinDig.:  5

		 5: [[3, 3, 3, 3, 3]]

	Num: 16
		MinDig.:  6

		 6: [[3, 3, 3, 3, 3, 1], [3, 3, 3, 3, 2, 2]]

	Num: 17
		MinDig.:  6

		 6: [[3, 3, 3, 3, 3, 2]]

	Num: 18
		MinDig.:  6

		 6: [[3, 3, 3, 3, 3, 3]]

	Num: 19
		MinDig.:  7

		 7: [[3, 3, 3, 3, 3, 3, 1], [3, 3, 3, 3, 3, 2, 2]]

	Num: 20
		MinDig.:  7

		 7: [[3, 3, 3, 3, 3, 3, 2]]


	Num.: 10
		MinDig: 4

			10: [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
			 9: [[2, 1, 1, 1, 1, 1, 1, 1, 1]]
			 8: [[2, 2, 1, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1]]
			 7: [[2, 2, 2, 1, 1, 1, 1], [3, 2, 1, 1, 1, 1, 1]]
			 6: [[2, 2, 2, 2, 1, 1], [3, 2, 2, 1, 1, 1], [3, 3, 1, 1, 1, 1]]
			 5: [[2, 2, 2, 2, 2], [3, 2, 2, 2, 1], [3, 3, 2, 1, 1]]
			 4: [[3, 3, 2, 2], [3, 3, 3, 1]]

Process finished with exit code 0

"""