"""
784 - Maze Exploration
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=667&page=show_problem&problem=725

        A maze of rectangular rooms is represented on a two dimensional grid as illustrated in figure 1a.
    Each point of the grid is represented by a character. The points of room walls are marked by the
    same character which can be any printable character different than '*', '_' and space (' '). In figure 1 this
    character is 'X'. All the other points of the grid are marked by spaces.

        Initial maze:
            XXXXXXXXXXXXXXXXXXXXX
            X   X   X   X   X   X
            X           X   X   X
            X   X   X   X   X   X
            XXXXXX XXX XXXXXXXXXX
            X   X   X   X   X   X
            X   X     *         X
            X   X   X   X   X   X
            XXXXXXXXXXXXXXXXXXXXX

        Painted maze:
            XXXXXXXXXXXXXXXXXXXXX
            X###X###X###X   X   X
            X###########X   X   X
            X###X###X###X   X   X
            XXXXXX#XXX#XXXXXXXXXX
            X   X###X###X###X###X
            X   X###X###X###X###X
            X   X###X###X###X###X
            XXXXXXXXXXXXXXXXXXXXX

        All rooms of the maze are equal sized with all walls 3 points wide and 1 point thick as illustrated
    in figure 2. In addition, a wall is shared on its full length by the separated rooms. The rooms can
    communicate through doors, which are positioned in the middle of walls. There are no outdoor doors.

            door
              |
            XX XX
            X . X  measured from within the room
      door - ...-- walls are 3 points wide
            X . X__
            XXXXX |
              |___ walls are one point thick

    Your problem is to paint all rooms of a maze which can be visited starting from a given room, called
    the 'start room' which is marked by a star ('*') positioned in the middle of the room. A room can be
    visited from another room if there is a door on the wall which separates the rooms. By convention, a
    room is painted if its entire surface, including the doors, is marked by the character '#' as shown.

    Input:
            The program input is a text file structured as follows:

            1. The first line contains a positive integer which shows the number of mazes to be painted.
            2. The rest of the file contains the mazes.

        The lines of the input file can be of different length. The text which represents a maze is terminated
        by a separation line full of underscores ('_'). There are at most 30 lines and at most 80 characters in a
        line for each maze. The program reads the mazes from the standard input

    Output:
            The output text of a painted maze has the same format as that which has been read for that maze,
        including the separation lines. The program writes the painted mazes on the standard output.


    Sample:
        2
        XXXXXXXXX
        X   X   X
        X   *   X
        X   X   X
        XXXXXXXXX
        X   X
        X   X
        X   X
        XXXXX
        _____
        XXXXX
        X   X
        X * X
        X   X
        XXXXX
        _____
            =>  XXXXXXXXX
                X###X###X
                X#######X
                X###X###X
                XXXXXXXXX
                X   X
                X   X
                X   X
                XXXXX
                _____
                XXXXX
                X###X
                X###X
                X###X
                XXXXX
                _____

"""

def dataProcess(InputRaw_Str):

    InputLines = InputRaw_Str.split("\n")
    caseNum = int(InputLines.pop(0))

    return InputLines, caseNum


def dataExtract(InputLines):

    mazeLine = InputLines.pop(0)
    mzStrt = [0, 0]
    mzCnt = 0
    Maze = []

    inMaze = {}

    while '_' not in mazeLine:
        Maze.append(list(mazeLine))
        print(f"\t\t\t{mazeLine}")

        inMaze[mzCnt] = len(mazeLine)

        if '*' in mazeLine:
            mzStrt[0] = mzCnt
            mzStrt[1] = mazeLine.index('*')

        mazeLine = InputLines.pop(0)
        mzCnt += 1
    print()

    return Maze, mzStrt, inMaze


def fillMaze(Maze, mzStrt, inMaze):
    stackFill = [mzStrt]

    while len(stackFill) > 0:

        curPos = stackFill.pop(0)
        curR = curPos[0]
        curC = curPos[1]

        Maze[curR][curC] = '#'

        if (curR + 1) in inMaze:
            if (curC) <= inMaze[curR + 1]:
                if Maze[curR + 1][curC] == ' ':
                    stackFill.append([curR + 1, curC])

        if (curR - 1) in inMaze:
            if (curC) <= inMaze[curR - 1]:
                if Maze[curR - 1][curC] == ' ':
                    stackFill.append([curR - 1, curC])

        if (curC + 1) <= inMaze[curR]:
            if Maze[curR][curC + 1] == ' ':
                stackFill.append([curR, curC + 1])

        if (curC - 1) <= inMaze[curR]:
            if Maze[curR][curC - 1] == ' ':
                stackFill.append([curR, curC - 1])

    return Maze


InputRaw_Str = """
2
XXXXXXXXX
X   X   X
X   *   X
X   X   X
XXXXXXXXX
X   X
X   X
X   X
XXXXX
_____
XXXXX
X   X
X * X
X   X
XXXXX
_____
"""

InputRaw_Str = InputRaw_Str[1:-1]

if __name__ == '__main__':

    print("Input:")
    print(InputRaw_Str)
    print()

    InputLines, caseNum = dataProcess(InputRaw_Str)

    # InputLines = InputRaw_Str.split("\n")
    # caseNum = int(InputLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    for case in range(caseNum):

        print(f"\t\tCase: {case+1}")
        print()

        Maze, mzStrt, inMaze = dataExtract(InputLines)

        # mazeLine = InputLines.pop(0)
        # mzStrt = [0, 0]
        # mzCnt = 0
        # Maze = []
        #
        # inMaze = {}
        #
        # while '_' not in mazeLine:
        #     Maze.append(list(mazeLine))
        #     print(f"\t\t\t{mazeLine}")
        #
        #     inMaze[mzCnt] = len(mazeLine)
        #
        #     if '*' in mazeLine:
        #         mzStrt[0] = mzCnt
        #         mzStrt[1] = mazeLine.index('*')
        #
        #     mazeLine = InputLines.pop(0)
        #     mzCnt += 1
        # print()

        print(f"\t\t\tStart: {mzStrt}")
        print()

        # for r, row in enumerate(Maze):
        #     print(f"\t\t\t\t[{r:<2} {inMaze[r]:2}] : {row}")
        # print()

        Maze = fillMaze(Maze, mzStrt, inMaze)

        # stackFill = [mzStrt]
        #
        # while len(stackFill) > 0:
        #
        #     curPos = stackFill.pop(0)
        #     curR = curPos[0]
        #     curC = curPos[1]
        #
        #     Maze[curR][curC] = '#'
        #
        #     if (curR+1) in inMaze:
        #         if (curC) <= inMaze[curR+1]:
        #             if Maze[curR+1][curC] == ' ':
        #                 stackFill.append([curR+1, curC])
        #
        #     if (curR-1) in inMaze:
        #         if (curC) <= inMaze[curR-1]:
        #             if Maze[curR-1][curC] == ' ':
        #                 stackFill.append([curR-1, curC])
        #
        #     if (curC+1) <= inMaze[curR]:
        #         if Maze[curR][curC+1] == ' ':
        #             stackFill.append([curR, curC+1])
        #
        #     if (curC-1) <= inMaze[curR]:
        #         if Maze[curR][curC-1] == ' ':
        #             stackFill.append([curR, curC-1])

        for r, row in enumerate(Maze):
            print(f"\t\t\t", end="")
            for col in row:
                print(col, end="")
            print()

        if (case+1) < caseNum:
            print("\n")


"""__Output__"""
"""
Input:
2
XXXXXXXXX
X   X   X
X   *   X
X   X   X
XXXXXXXXX
X   X
X   X
X   X
XXXXX
_____
XXXXX
X   X
X * X
X   X
XXXXX
_____

	Cases: 2

		Case: 1

			XXXXXXXXX
			X   X   X
			X   *   X
			X   X   X
			XXXXXXXXX
			X   X
			X   X
			X   X
			XXXXX

			Start: [2, 4]

			XXXXXXXXX
			X###X###X
			X#######X
			X###X###X
			XXXXXXXXX
			X   X
			X   X
			X   X
			XXXXX


		Case: 2

			XXXXX
			X   X
			X * X
			X   X
			XXXXX

			Start: [2, 2]

			XXXXX
			X###X
			X###X
			X###X
			XXXXX

Process finished with exit code 0

"""