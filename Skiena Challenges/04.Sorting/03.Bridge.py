"""

Bridge

        A group of n people wish to cross a bridge at night. At most two people may cross at
    any time, and each group must have a flashlight. Only one flashlight is available among
    the n people, so some sort of shuttle arrangement must be arranged in order to return
    the flashlight so that more people may cross.
        Each person has a different crossing speed; the speed of a group is determined by the
    speed of the slower member. Your job is to determine a strategy that gets all n people
    across the bridge in the minimum time.

    Input:
            The input begins with a single positive integer on a line by itself indicating the number
        of test cases, followed by a blank line. There is also a blank line between each two
        consecutive inputs.
            The first line of each case contains n, followed by n lines giving the crossing times
        for each of the people. There are not more than 1,000 people and nobody takes more
        than 100 seconds to cross the bridge.

    Output:
            For each test case, the first line of output must report the total number of seconds
        required for all n people to cross the bridge. Subsequent lines give a strategy for achiev-
        ing this time. Each line contains either one or two integers, indicating which person
        or people form the next group to cross. Each person is indicated by the crossing time
        specified in the input. Although many people may have the same crossing time, this
        ambiguity is of no consequence.
            Note that the crossings alternate directions, as it is necessary to return the flashlight
        so that more may cross. If more than one strategy yields the minimal time, any one
        will do.
        The output of two consecutive cases must be separated by a blank line.


    Sample:
        1

        4
        1
        2
        5
        10
            =>  17
                1 2
                1
                5 10
                2
                1 2

"""

InputRaw_Str = """
1

4
1
2
5
10
"""

InputLst_Str = InputRaw_Str.split("\n")[1:-1]

print(InputLst_Str)
print()

InputLst = []

for Input in InputLst_Str[1:]:

    if Input.isnumeric():

        InputLst.append(int(Input))

print(f"Input: {InputLst}\n")

pplNum = InputLst[0]

print(f"\tNumber of people: {pplNum}")

spdLst = InputLst[1: pplNum + 1]
print(f"\tSpeed of people:  {spdLst}")


