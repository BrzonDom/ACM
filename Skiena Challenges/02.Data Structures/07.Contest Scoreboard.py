"""

Contest Scoreboard

    Contestants are ranked first by the number of problems solved, then by decreasing amounts
    of penalty time. If two or more contestants are tied in both problems solved and penalty time,
    they are displayed in order of increasing team numbers. A problem is considered solved by a
    contestant if any of the submissions for that problem was judged correct. Penalty time is
    computed as the number of minutes it took until the first correct submission for a problem
    was received, plus 20 minutes for each incorrect submission prior to the correct solution.
    Unsolved problems incur no time penalties.

    Input:
        The input begins with a single positive integer on a line by itself indicating the number
        of cases, each described as below. This line is followed by a blank line. There is also a
        blank line between two consecutive inputs.
        The input consists of a snapshot of the judging queue, containing entries from some
        or all of contestants 1 through 100 solving problems 1 through 9. Each line of input
        consists of three numbers and a letter in the format contestant problem time L, where
        L can be C, I, R, U, or E. These stand for Correct, Incorrect, clarification Request,
        Unjudged, and Erroneous submission. The last three cases do not affect scoring.
        The lines of input appear in the order in which the submissions were received.

    Output:
        The output for each test case will consist of a scoreboard, sorted by the criteria described
        above. Each line of output will contain a contestant number, the number of problems
        solved by the contestant and the total time penalty accumulated by the contestant.
        Since not all contestants are actually participating, only display those contestants who
        have made a submission.
        The output of two consecutive cases will be separated by a blank line.


    Sample:
        1

        1 2 10 I
        3 1 11 C
        1 2 19 R
        1 2 21 C
        1 1 25 C
            =>  1 2 66
                3 1 11

"""

InputRaw_Str = """
1

1 2 10 I
3 1 11 C
1 2 19 R
1 2 21 C
1 1 25 C
"""

# class Stats:
#     def __init__(self, player, problem, time, state):
#         self.player = player
#         self.problem = problem
#         self.time = time
#         self.state = state

Cases = int(InputRaw_Str[1])

print(f"Cases: {Cases}\n")

Input = list(InputRaw_Str.split("\n"))[3:-1]

print(f"\tInput: {Input}")
print()

stats = {}

for submit in Input:
    submit_lst = list(submit.split())

    player = int(submit_lst[0])
    problem = int(submit_lst[1])
    time = int(submit_lst[2])
    state = submit_lst[3]

    if player not in stats:
        stats[player] = {"Solved"  : [],
                         "Time"    : 0,
                         "Penalty" : 0}

    if state == 'C':
        stats[player]["Solved"] += [problem]
        stats[player]["Time"] += time

    elif state == 'I' and problem not in stats[player]["Solved"]:
        stats[player]["Penalty"] += 20


for player in stats:
    print(f"\tPlayer: {player}\n")
    print(f"\t\tSolved problems: {stats[player]['Solved']}")
    print(f"\t\tTime:            {stats[player]['Time']}")
    print(f"\t\tPenalty:         {stats[player]['Penalty']}")
    print(f"\t\tTotal time:      {stats[player]['Time'] + stats[player]['Penalty']}")
    print("\n")
