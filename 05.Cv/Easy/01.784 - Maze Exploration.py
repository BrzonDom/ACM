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


def dataExtract_Prt(InputLines):

    mazeLine = InputLines.pop(0)
    mzStrt = [0, 0]
    mzCnt = 0
    Maze = []

    dimMaze = {}

    while '_' not in mazeLine:
        Maze.append(list(mazeLine))
        print(f"\t\t\t{mazeLine}")

        dimMaze[mzCnt] = len(mazeLine)

        if '*' in mazeLine:
            mzStrt[0] = mzCnt
            mzStrt[1] = mazeLine.index('*')

        mazeLine = InputLines.pop(0)
        mzCnt += 1
    print()

    sepLine = mazeLine

    return Maze, mzStrt, dimMaze, sepLine


def fillMaze(Maze, mzStrt, dimMaze):

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

InputTst_Str = """
7
AAAAAAAAA 
A   A   A
A * A   A
A   A   A
AAAAAAAAA
_________
BBBBB   BBBBB
B   B   B   B
B * B   B   B
B   B   B   B
BBBBB   BBBBB
_________
CCCCCCCCCCCCC
C   C   C   C
C * C   C   C
C   C   C   C
CC CCCCCCC CC
C   C   C   C
C           C
C   C   C   C
CC CCCCCCC CC
C   C   C   C
C   C   C   C
C   C   C   C
CCCCCCCCCCCCC
_____________
AXXXBXXXCXXXDXXXEXXXFXXXG   
X   X   X   X   X   X   X
X *     X   X           X
X   X   X   X   X   X   X
XXXXXX XXXXXXXXXXXXXXX XX
X   X   X   X   X   X   X
X   X                   X 
X   X   X   X   X   X   X
HXXXIXXXJXXXKXXXLXXXMXXXX
_________________________
XXXXX
X  XX
X*XXX
X   X
X X X
X XX
X X
X X
XXX
__
XXX
X X
X*X
XX
____
AXXXBXXXCXXXDXXXEXXXFXXXG   
X   X   X   X   X   X   X
X *     X   X           X
X   X   X   X   X   X   X
XXXXXX XXXXXXXXXXXXXXX XX
X   X   X   X   X   X   X
X   X                   X 
X   X   X   X   X   X   X
HXXXIXXXJXXXKXXXLXXXMXXXX
_
"""

InputRaw_Str = InputRaw_Str[1:-1]
InputTst_Str = InputTst_Str[1:-1]

InputLst_Str = [InputRaw_Str, InputTst_Str]

InputStr = InputLst_Str[1]

if __name__ == '__main__':

    print("Input:")
    print(InputStr)
    print()

    InputLines, caseNum = dataProcess(InputStr)

    # InputLines = InputRaw_Str.split("\n")
    # caseNum = int(InputLines.pop(0))

    print(f"\tCases: {caseNum}")
    print()

    for case in range(caseNum):

        print(f"\t\tCase: {case+1}")
        print()

        Maze, mzStrt, inMaze, sepLine = dataExtract_Prt(InputLines)

        print(f"\t\t\tStart: {mzStrt}")
        print()

        solMaze = fillMaze(Maze, mzStrt, inMaze)

        for row in solMaze:
            print(f"\t\t\t", end="")
            for col in row:
                print(col, end="")
            print()

        print(f"\t\t\t{sepLine}")

        if (case+1) < caseNum:
            print("\n")


"""__Output__"""
"""
Input:
7
AAAAAAAAA 
A   A   A
A * A   A
A   A   A
AAAAAAAAA
_________
BBBBB   BBBBB
B   B   B   B
B * B   B   B
B   B   B   B
BBBBB   BBBBB
_________
CCCCCCCCCCCCC
C   C   C   C
C * C   C   C
C   C   C   C
CC CCCCCCC CC
C   C   C   C
C           C
C   C   C   C
CC CCCCCCC CC
C   C   C   C
C   C   C   C
C   C   C   C
CCCCCCCCCCCCC
_____________
AXXXBXXXCXXXDXXXEXXXFXXXG   
X   X   X   X   X   X   X
X *     X   X           X
X   X   X   X   X   X   X
XXXXXX XXXXXXXXXXXXXXX XX
X   X   X   X   X   X   X
X   X                   X 
X   X   X   X   X   X   X
HXXXIXXXJXXXKXXXLXXXMXXXX
_________________________
XXXXX
X  XX
X*XXX
X   X
X X X
X XX
X X
X X
XXX
__
XXX
X X
X*X
XX
____
AXXXBXXXCXXXDXXXEXXXFXXXG   
X   X   X   X   X   X   X
X *     X   X           X
X   X   X   X   X   X   X
XXXXXX XXXXXXXXXXXXXXX XX
X   X   X   X   X   X   X
X   X                   X 
X   X   X   X   X   X   X
HXXXIXXXJXXXKXXXLXXXMXXXX
_

	Cases: 7

		Case: 1

			AAAAAAAAA 
			A   A   A
			A * A   A
			A   A   A
			AAAAAAAAA

			Start: [2, 2]

			AAAAAAAAA 
			A###A   A
			A###A   A
			A###A   A
			AAAAAAAAA
			_________


		Case: 2

			BBBBB   BBBBB
			B   B   B   B
			B * B   B   B
			B   B   B   B
			BBBBB   BBBBB

			Start: [2, 2]

			BBBBB   BBBBB
			B###B   B   B
			B###B   B   B
			B###B   B   B
			BBBBB   BBBBB
			_________


		Case: 3

			CCCCCCCCCCCCC
			C   C   C   C
			C * C   C   C
			C   C   C   C
			CC CCCCCCC CC
			C   C   C   C
			C           C
			C   C   C   C
			CC CCCCCCC CC
			C   C   C   C
			C   C   C   C
			C   C   C   C
			CCCCCCCCCCCCC

			Start: [2, 2]

			CCCCCCCCCCCCC
			C###C   C###C
			C###C   C###C
			C###C   C###C
			CC#CCCCCCC#CC
			C###C###C###C
			C###########C
			C###C###C###C
			CC#CCCCCCC#CC
			C###C   C###C
			C###C   C###C
			C###C   C###C
			CCCCCCCCCCCCC
			_____________


		Case: 4

			AXXXBXXXCXXXDXXXEXXXFXXXG   
			X   X   X   X   X   X   X
			X *     X   X           X
			X   X   X   X   X   X   X
			XXXXXX XXXXXXXXXXXXXXX XX
			X   X   X   X   X   X   X
			X   X                   X 
			X   X   X   X   X   X   X
			HXXXIXXXJXXXKXXXLXXXMXXXX

			Start: [2, 2]

			AXXXBXXXCXXXDXXXEXXXFXXXG   
			X###X###X   X###X###X###X
			X#######X   X###########X
			X###X###X   X###X###X###X
			XXXXXX#XXXXXXXXXXXXXXX#XX
			X   X###X###X###X###X###X
			X   X###################X 
			X   X###X###X###X###X###X
			HXXXIXXXJXXXKXXXLXXXMXXXX
			_________________________


		Case: 5

			XXXXX
			X  XX
			X*XXX
			X   X
			X X X
			X XX
			X X
			X X
			XXX

			Start: [2, 1]

			XXXXX
			X##XX
			X#XXX
			X###X
			X#X#X
			X#XX
			X#X
			X#X
			XXX
			__


		Case: 6

			XXX
			X X
			X*X
			XX

			Start: [2, 1]

			XXX
			X#X
			X#X
			XX
			____


		Case: 7

			AXXXBXXXCXXXDXXXEXXXFXXXG   
			X   X   X   X   X   X   X
			X *     X   X           X
			X   X   X   X   X   X   X
			XXXXXX XXXXXXXXXXXXXXX XX
			X   X   X   X   X   X   X
			X   X                   X 
			X   X   X   X   X   X   X
			HXXXIXXXJXXXKXXXLXXXMXXXX

			Start: [2, 2]

			AXXXBXXXCXXXDXXXEXXXFXXXG   
			X###X###X   X###X###X###X
			X#######X   X###########X
			X###X###X   X###X###X###X
			XXXXXX#XXXXXXXXXXXXXXX#XX
			X   X###X###X###X###X###X
			X   X###################X 
			X   X###X###X###X###X###X
			HXXXIXXXJXXXKXXXLXXXMXXXX
			_

Process finished with exit code 0

"""