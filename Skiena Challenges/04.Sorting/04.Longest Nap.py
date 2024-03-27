"""

Longest Nap

        Professors lead very busy lives with full schedules of work and appointments. Professor
    P likes to nap during the day, but his schedule is so busy that he doesn’t have many
    chances to do so.
        He really wants to take one nap every day, however. Naturally, he wants to take the
    longest nap possible given his schedule. Write a program to help him with the task.

    Input:
            The input consists of an arbitrary number of test cases, where each test case represents
        one day.
            The first line of each case contains a positive integer s ≤ 100, representing the number
        of scheduled appointments for that day. The next s lines contain the appointments
        in the format time1 time2 appointment, where time1 represents the time which the
        appointment starts and time2 the time it ends. All times will be in the hh:mm format;
        the ending time will always be strictly after the starting time, and separated by a single
        space.
            All times will be greater than or equal to 10:00 and less than or equal to 18:00. Thus
        your response must be in this interval as well; i.e., no nap can start before 10:00 and
        last after 18:00.
            The appointment can be any sequence of characters, but will always be on the same
        line. You can assume that no line is be longer than 255 characters, that 10 ≤ hh ≤ 18
        and that 0 ≤ mm < 60. You cannot assume, however, that the input will be in any
        specific order, and must read the input until you reach the end of file.

    Output:
            For each test case, you must print the following line:
        Day #d: the longest nap starts at hh : mm and will last for [H hours and] M minutes.
        where d stands for the number of the test case (starting from 1) and hh : mm is the
        time when the nap can start. To display the length of the nap, follow these rules:
            1. If the total time X is less than 60 minutes, just print “X minutes.”
            2. If the total duration X is at least 60 minutes, print “H hours and M minutes,”
            where
                H = X ÷ 60 (integer division, of course) and M = X mod 60.
        You don’t have to worry about correct pluralization; i.e., you must print “1 minutes”
        or “1 hours” if that is the case.
            The duration of the nap is calculated by the difference between the ending time and
        the beginning time. That is, if an appointment ends at 14:00 and the next one starts
        at 14:47, then you have 14:47 – 14:00 = 47 minutes of possible napping.
            If there is more than one longest nap with the same duration, print the earliest one.
        You can assume the professor won’t be busy all day, so there is always time for at least
        one possible nap


    Sample:

        4
        10:00 12:00 Lectures
        12:00 13:00 Lunch, like always.
        13:00 15:00 Boring lectures...
        15:30 17:45 Reading
        4
        10:00 12:00 Lectures
        12:00 13:00 Lunch, just lunch.
        13:00 15:00 Lectures, lectures... oh, no!
        16:45 17:45 Reading (to be or not to be?)
        4
        10:00 12:00 Lectures, as everyday.
        12:00 13:00 Lunch, again!!!
        13:00 15:00 Lectures, more lectures!
        15:30 17:15 Reading (I love reading, but should I schedule it?)
        1
        12:00 13:00 I love lunch! Have you ever noticed it? :)
            =>  Day #1: the longest nap starts at 15:00 and will last for 30 minutes.
                Day #2: the longest nap starts at 15:00 and will last for 1 hours and 45 minutes.
                Day #3: the longest nap starts at 17:15 and will last for 45 minutes.
                Day #4: the longest nap starts at 13:00 and will last for 5 hours and 0 minutes.

"""

InputRaw_Str = """
4
10:00 12:00 Lectures
12:00 13:00 Lunch, like always.
13:00 15:00 Boring lectures...
15:30 17:45 Reading
4
10:00 12:00 Lectures
12:00 13:00 Lunch, just lunch.
13:00 15:00 Lectures, lectures... oh, no!
16:45 17:45 Reading (to be or not to be?)
4
10:00 12:00 Lectures, as everyday.
12:00 13:00 Lunch, again!!!
13:00 15:00 Lectures, more lectures!
15:30 17:15 Reading (I love reading, but should I schedule it?)
1
12:00 13:00 I love lunch! Have you ever noticed it? :)
"""

InputRaw_Str = InputRaw_Str[1:-1]

# print("Raw Input:\n", end="\"\"\"\n")
# print(InputRaw_Str, end="\"\"\"\n")
# print()

InputStr_Lst = InputRaw_Str.split("\n")

# print(InputStr_Lst)

lstIndx = 0
dayCnt = 1
InputLst = []

print("Inputs: \n")

while lstIndx < len(InputStr_Lst):

    if InputStr_Lst[lstIndx].isnumeric():
        apptmNum = int(InputStr_Lst[lstIndx])

        InputLst.append(InputStr_Lst[lstIndx + 1: lstIndx + 1 + apptmNum])

        print(f"\t{dayCnt}.Day:")

        for Input in InputLst[dayCnt-1]:
            print(f"\t\t{Input}")
        print("\n")

        dayCnt += 1
        lstIndx += apptmNum

    else:
        lstIndx += 1
print()

dayCnt = 0

print("Input times:\n")

for InputDay in InputLst:

    dayCnt += 1

    timeLst_Str = []
    timeLst = []

    print(f"\t{dayCnt}.Day:")

    for Apptm in InputDay:

        print(f"\t\t{Apptm[0:5]} {Apptm[6:11]}")
        # print(Apptm[0:2], ":", Apptm[3:5], "  ", Apptm[6:8], ":", Apptm[9:11])

        timeLst_Str.append([Apptm[0:5], Apptm[6:11]])
        timeLst.append([[int(Apptm[0:2]), int(Apptm[3:5])], [int(Apptm[6:8]), int(Apptm[9:11])]])

        print(f"\t\t{timeLst[-1]}")
        print()

    print(f"\t\t{timeLst}")
    print("\n")

    print("\t\tMinutes:\n")

    minutLst = []

    for time in timeLst:

        minutLst.append([time[0][0] * 60 + time[0][1] - 10 * 60, time[1][0] * 60 + time[1][1] - 10 * 60])

        print(f"\t\t\t{time[0][0]:02}:{time[0][1]:02} = {time[0][0] * 60 + time[0][1]:4}  => {minutLst[-1][0]}")
        print(f"\t\t\t{time[1][0]:02}:{time[1][1]:02} = {time[1][0] * 60 + time[1][1]:4}  => {minutLst[-1][1]}")
        print()

        # time[0] = time[0][0] * 60 + time[0][1] - 10 * 60
        # time[1] = time[1][0] * 60 + time[1][1] - 10 * 60

        # print("\t\t", time[0], time[1])
    print()


"""__Output__"""
"""
Inputs: 

	1.Day:
		10:00 12:00 Lectures
		12:00 13:00 Lunch, like always.
		13:00 15:00 Boring lectures...
		15:30 17:45 Reading


	2.Day:
		10:00 12:00 Lectures
		12:00 13:00 Lunch, just lunch.
		13:00 15:00 Lectures, lectures... oh, no!
		16:45 17:45 Reading (to be or not to be?)


	3.Day:
		10:00 12:00 Lectures, as everyday.
		12:00 13:00 Lunch, again!!!
		13:00 15:00 Lectures, more lectures!
		15:30 17:15 Reading (I love reading, but should I schedule it?)


	4.Day:
		12:00 13:00 I love lunch! Have you ever noticed it? :)



Input times:

	1.Day:
		10:00 12:00
		[[10, 0], [12, 0]]

		12:00 13:00
		[[12, 0], [13, 0]]

		13:00 15:00
		[[13, 0], [15, 0]]

		15:30 17:45
		[[15, 30], [17, 45]]

		[[[10, 0], [12, 0]], [[12, 0], [13, 0]], [[13, 0], [15, 0]], [[15, 30], [17, 45]]]


		Minutes:

			10:00 =  600  => 0
			12:00 =  720  => 120

			12:00 =  720  => 120
			13:00 =  780  => 180

			13:00 =  780  => 180
			15:00 =  900  => 300

			15:30 =  930  => 330
			17:45 = 1065  => 465


	2.Day:
		10:00 12:00
		[[10, 0], [12, 0]]

		12:00 13:00
		[[12, 0], [13, 0]]

		13:00 15:00
		[[13, 0], [15, 0]]

		16:45 17:45
		[[16, 45], [17, 45]]

		[[[10, 0], [12, 0]], [[12, 0], [13, 0]], [[13, 0], [15, 0]], [[16, 45], [17, 45]]]


		Minutes:

			10:00 =  600  => 0
			12:00 =  720  => 120

			12:00 =  720  => 120
			13:00 =  780  => 180

			13:00 =  780  => 180
			15:00 =  900  => 300

			16:45 = 1005  => 405
			17:45 = 1065  => 465


	3.Day:
		10:00 12:00
		[[10, 0], [12, 0]]

		12:00 13:00
		[[12, 0], [13, 0]]

		13:00 15:00
		[[13, 0], [15, 0]]

		15:30 17:15
		[[15, 30], [17, 15]]

		[[[10, 0], [12, 0]], [[12, 0], [13, 0]], [[13, 0], [15, 0]], [[15, 30], [17, 15]]]


		Minutes:

			10:00 =  600  => 0
			12:00 =  720  => 120

			12:00 =  720  => 120
			13:00 =  780  => 180

			13:00 =  780  => 180
			15:00 =  900  => 300

			15:30 =  930  => 330
			17:15 = 1035  => 435


	4.Day:
		12:00 13:00
		[[12, 0], [13, 0]]

		[[[12, 0], [13, 0]]]


		Minutes:

			12:00 =  720  => 120
			13:00 =  780  => 180



Process finished with exit code 0

"""