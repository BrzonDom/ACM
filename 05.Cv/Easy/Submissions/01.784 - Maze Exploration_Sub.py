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


"""
def dataExtract_Prt(MazeLines):

    mzStrt = [0, 0]
    mzCnt = 0
    Maze = []

    inMaze = {}

    for mzLine in MazeLines:
        Maze.append(list(mzLine))
        print(f"\t\t\t{mzLine}")

        inMaze[mzCnt] = len(mzLine)

        if '*' in mzLine:
            mzStrt[0] = mzCnt
            mzStrt[1] = mzLine.index('*')

        mzCnt += 1
    print()

    return Maze, mzStrt, inMaze
"""


def dataSplit(caseNum):

    MazeLst = []
    sepLst = []

    for case in range(caseNum):

        Maze = []

        InLine = input()

        while '_' not in InLine:

            Maze.append(list(InLine))

            InLine = input()

        MazeLst.append(Maze)
        sepLst.append(InLine)

    return MazeLst, sepLst


def dataExtract(Maze):

    mzStrt = [0, 0]
    mzCnt = 0

    inMaze = {}

    for mzLine in Maze:

        inMaze[mzCnt] = len(mzLine)

        if '*' in mzLine:
            mzStrt[0] = mzCnt
            mzStrt[1] = mzLine.index('*')

        mzCnt += 1

    return mzStrt, inMaze


def fillMaze(Maze, mzStrt, inMaze):

    stackFill = [mzStrt]
    filled = set()
    filled.add((mzStrt[0], mzStrt[1]))

    while len(stackFill) > 0:

        curPos = stackFill.pop(0)
        curR = curPos[0]
        curC = curPos[1]

        Maze[curR][curC] = '#'

        if (curR + 1, curC) not in filled:
            if (curR + 1) in dimMaze:
                if (curC) <= dimMaze[curR + 1]:
                    if Maze[curR + 1][curC] == ' ':
                        stackFill.append([curR + 1, curC])
                        filled.add((curR + 1, curC))

        if (curR - 1, curC) not in filled:
            if (curR - 1) in dimMaze:
                if (curC) <= dimMaze[curR - 1]:
                    if Maze[curR - 1][curC] == ' ':
                        stackFill.append([curR - 1, curC])
                        filled.add((curR - 1, curC))

        if (curR, curC + 1) not in filled:
            if (curC + 1) <= dimMaze[curR]:
                if Maze[curR][curC + 1] == ' ':
                    stackFill.append([curR, curC + 1])
                    filled.add((curR, curC + 1))

        if (curR, curC - 1) not in filled:
            if (curC - 1) <= dimMaze[curR]:
                if Maze[curR][curC - 1] == ' ':
                    stackFill.append([curR, curC - 1])
                    filled.add((curR, curC - 1))
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

    caseNum = int(input())

    MazeLst, sepLst = dataSplit(caseNum)

    for case, Maze in enumerate(MazeLst):

        mzStrt, inMaze = dataExtract(Maze)

        solMaze = fillMaze(Maze, mzStrt, inMaze)

        for row in solMaze:
            for col in row:
                print(col, end="")
            print()

        print(sepLst[case])

