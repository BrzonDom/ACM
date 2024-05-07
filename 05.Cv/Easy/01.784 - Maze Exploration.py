"""
784 - Maze Exploration
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=667&page=show_problem&problem=725

    A maze of rectangular rooms is represented on a two dimensional grid as illustrated in figure 1a.
    Each point of the grid is represented by a character. The points of room walls are marked by the
    same character which can be any printable character different than `*', ` ' and space. In figure 1 this
    character is `X'. All the other points of the grid are marked by spaces.

        Initial maze
            XXXXXXXXXXXXXXXXXXXXX
            X   X   X   X   X   X
            X           X   X   X
            X   X   X   X   X   X
            XXXXXX XXX XXXXXXXXXX
            X   X   X   X   X   X
            X   X     *         X
            X   X   X   X   X   X
            XXXXXXXXXXXXXXXXXXXXX

        Painted maze
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
    the `start room' which is marked by a star (`*') positioned in the middle of the room. A room can be
    visited from another room if there is a door on the wall which separates the rooms. By convention, a
    room is painted if its entire surface, including the doors, is marked by the character `#' as shown.

    Input:
            The program input is a text file structured as follows:

            1. The first line contains a positive integer which shows the number of mazes to be painted.
            2. The rest of the file contains the mazes.

        The lines of the input file can be of different length. The text which represents a maze is terminated
        by a separation line full of underscores (` '). There are at most 30 lines and at most 80 characters in a
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

print("Input:")
print(InputRaw_Str)
print()

InputLines = InputRaw_Str.split("\n")

caseNum = int(InputLines.pop(0))

print(f"\tCases: {caseNum}")
print()