"""

Where’s Waldorf

        Given an m by n grid of letters and a list of words, find the location in the grid at
    which the word can be found.

    Input:
            The input begins with a single positive integer on a line by itself indicating the number
        of cases, followed by a blank line. There is also a blank line between each two consecutive
        cases.
            Each case begins with a pair of integers m followed by n on a single line, where
        1 ≤ m, n ≤ 50 in decimal notation. The next m lines contain n letters each, representing
        the grid of letters where the words must be found. The letters in the grid may be in
        upper- or lowercase. Following the grid of letters, another integer k appears on a line by
        itself (1 ≤ k ≤ 20). The next k lines of input contain the list of words to search for, one
        word per line. These words may contain upper- and lowercase letters only – no spaces,
        hyphens, or other non-alphabetic characters.

    Output:
            For each word in each test case, output a pair of integers representing its location in
        the corresponding grid. The integers must be separated by a single space. The first
        integer is the line in the grid where the first letter of the given word can be found (1
        represents the topmost line in the grid, and m represents the bottommost line). The
        second integer is the column in the grid where the first letter of the given word can
        be found (1 represents the leftmost column in the grid, and n represents the rightmost
        column in the grid). If a word can be found more than once in the grid, then output
        the location of the uppermost occurrence of the word (i.e., the occurrence which places
        the first letter of the word closest to the top of the grid). If two or more words are
        uppermost, output the leftmost of these occurrences. All words can be found at least
        once in the grid.
            The output of two consecutive cases must be separated by a blank line.


    Sample:
        1

        8 11
        abcDEFGhigg
        hEbkWalDork
        FtyAwaldORm
        FtsimrLqsrc
        byoArBeDeyv
        Klcbqwikomk
        strEBGadhrb
        yUiqlxcnBjf
        4
        Waldorf
        Bambi
        Betty
        Dagbert
            =>  2 5
                2 3
                1 2
                7 8

"""
import numpy as np

InputRaw_Str = """
1

8 11
abcDEFGhigg
hEbkWalDork
FtyAwaldORm
FtsimrLqsrc
byoArBeDeyv
Klcbqwikomk
strEBGadhrb
yUiqlxcnBjf
4
Waldorf
Bambi
Betty
Dagbert
"""

InputRaw_Str = InputRaw_Str[1:-1]

InputStr_Lst = InputRaw_Str.split("\n")

caseNum = int(InputStr_Lst.pop(0))

print(f"Cases: {caseNum}\n")

for case in range(caseNum):

    print(f"\t{case+1}. case\n")

    InputStr_Lst.pop(0)

    RowNum, ColNum = list(map(int, InputStr_Lst.pop(0).split()))

    print(f"\t\tRows: {RowNum}")
    print(f"\t\tCols: {ColNum}")
    print()

    Grid = [["" for c in range(ColNum)] for r in range(RowNum)]

    print("\t\t\t\t", end="")
    for col in range(ColNum):
        print(f"{col:<5}", end="")
    print()

    for row in range(RowNum):
        line = InputStr_Lst.pop(0)

        for col in range(ColNum):

            Grid[row][col] = line[col].upper()

        print(f"\t\t\t{row}", Grid[row])
    print("\n")

    wordNum = int(InputStr_Lst.pop(0))

    Words = []
    strtChar = set()
    strtIndx = {}

    print(f"\t\tWords: {wordNum}\n")

    for w in range(wordNum):

        Words.append(InputStr_Lst.pop(0).upper())
        strtIndx[Words[-1][0]] = []
        strtChar.add(Words[-1][0])

        print("\t\t\t", Words[-1])
    print("\n")

    for row in range(RowNum):
        for col in range(ColNum):

            for char in strtChar:

                if Grid[row][col] == char:
                    strtIndx[char].append((row, col))

    for start in strtIndx:
        print(f"\t\t{start} : {strtIndx[start]}")
    print()

    for word in Words:
        for start in strtIndx[word[0]]:
            # print(word, start)

            strRow, strCol = start

            print(f"\t\t[{strRow}, {strCol}] {word} ({len(word)})")
            print()
            # print(f"\t\t\tTop: {bordTop}")

            bordRight = (strCol + len(word) - 1) < ColNum
            bordDown = (strRow + len(word) - 1) < RowNum
            bordLeft = (strCol - (len(word) - 1)) >= 0
            bordTop = (strCol - (len(word) - 1)) >= 0

            print(f"\t\t\tRight: {bordRight}")
            print(f"\t\t\tDown: {bordDown}")
            print(f"\t\t\tLeft: {bordLeft}")
            print(f"\t\t\tTop: {bordTop}")
            print()

            print(f"\t\t\t( 1, 0) : [{strRow + len(word) - 1:3}, {strCol:3}]")
            print(f"\t\t\t( 1, 1) : [{strRow + len(word) - 1:3}, {strCol + len(word) - 1:3}]")
            print(f"\t\t\t( 0, 1) : [{strRow:3}, {strCol + len(word) - 1:3}]")
            print(f"\t\t\t(-1, 1) : [{strRow - (len(word) - 1):3}, {strCol + len(word) - 1:3}]")
            print(f"\t\t\t(-1, 0) : [{strRow - (len(word) - 1):3}, {strCol:3}]")
            print(f"\t\t\t(-1,-1) : [{strRow - (len(word) - 1):3}, {strCol - (len(word) - 1):3}]")
            print(f"\t\t\t( 0,-1) : [{strRow:3}, {strCol - (len(word) - 1):3}]")
            print(f"\t\t\t( 1,-1) : [{strRow + len(word) - 1:3}, {strCol - (len(word) - 1):3}]")
            print()


    print()

"""__Output__"""
"""
Cases: 1

	1. case

		Rows: 8
		Cols: 11

				0    1    2    3    4    5    6    7    8    9    10   
			0 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'G']
			1 ['H', 'E', 'B', 'K', 'W', 'A', 'L', 'D', 'O', 'R', 'K']
			2 ['F', 'T', 'Y', 'A', 'W', 'A', 'L', 'D', 'O', 'R', 'M']
			3 ['F', 'T', 'S', 'I', 'M', 'R', 'L', 'Q', 'S', 'R', 'C']
			4 ['B', 'Y', 'O', 'A', 'R', 'B', 'E', 'D', 'E', 'Y', 'V']
			5 ['K', 'L', 'C', 'B', 'Q', 'W', 'I', 'K', 'O', 'M', 'K']
			6 ['S', 'T', 'R', 'E', 'B', 'G', 'A', 'D', 'H', 'R', 'B']
			7 ['Y', 'U', 'I', 'Q', 'L', 'X', 'C', 'N', 'B', 'J', 'F']


		Words: 4

			 WALDORF
			 BAMBI
			 BETTY
			 DAGBERT


		W : [(1, 4), (2, 4), (5, 5)]
		B : [(0, 1), (1, 2), (4, 0), (4, 5), (5, 3), (6, 4), (6, 10), (7, 8)]
		D : [(0, 3), (1, 7), (2, 7), (4, 7), (6, 7)]

		[1, 4] WALDORF (7)

			Right: True
			Down: True
			Left: False
			Top: False

			( 1, 0) : [  7,   4]
			( 1, 1) : [  7,  10]
			( 0, 1) : [  1,  10]
			(-1, 1) : [ -5,  10]
			(-1, 0) : [ -5,   4]
			(-1,-1) : [ -5,  -2]
			( 0,-1) : [  1,  -2]
			( 1,-1) : [  7,  -2]

		[2, 4] WALDORF (7)

			Right: True
			Down: False
			Left: False
			Top: False

			( 1, 0) : [  8,   4]
			( 1, 1) : [  8,  10]
			( 0, 1) : [  2,  10]
			(-1, 1) : [ -4,  10]
			(-1, 0) : [ -4,   4]
			(-1,-1) : [ -4,  -2]
			( 0,-1) : [  2,  -2]
			( 1,-1) : [  8,  -2]

		[5, 5] WALDORF (7)

			Right: False
			Down: False
			Left: False
			Top: False

			( 1, 0) : [ 11,   5]
			( 1, 1) : [ 11,  11]
			( 0, 1) : [  5,  11]
			(-1, 1) : [ -1,  11]
			(-1, 0) : [ -1,   5]
			(-1,-1) : [ -1,  -1]
			( 0,-1) : [  5,  -1]
			( 1,-1) : [ 11,  -1]

		[0, 1] BAMBI (5)

			Right: True
			Down: True
			Left: False
			Top: False

			( 1, 0) : [  4,   1]
			( 1, 1) : [  4,   5]
			( 0, 1) : [  0,   5]
			(-1, 1) : [ -4,   5]
			(-1, 0) : [ -4,   1]
			(-1,-1) : [ -4,  -3]
			( 0,-1) : [  0,  -3]
			( 1,-1) : [  4,  -3]

		[1, 2] BAMBI (5)

			Right: True
			Down: True
			Left: False
			Top: False

			( 1, 0) : [  5,   2]
			( 1, 1) : [  5,   6]
			( 0, 1) : [  1,   6]
			(-1, 1) : [ -3,   6]
			(-1, 0) : [ -3,   2]
			(-1,-1) : [ -3,  -2]
			( 0,-1) : [  1,  -2]
			( 1,-1) : [  5,  -2]

		[4, 0] BAMBI (5)

			Right: True
			Down: False
			Left: False
			Top: False

			( 1, 0) : [  8,   0]
			( 1, 1) : [  8,   4]
			( 0, 1) : [  4,   4]
			(-1, 1) : [  0,   4]
			(-1, 0) : [  0,   0]
			(-1,-1) : [  0,  -4]
			( 0,-1) : [  4,  -4]
			( 1,-1) : [  8,  -4]

		[4, 5] BAMBI (5)

			Right: True
			Down: False
			Left: True
			Top: True

			( 1, 0) : [  8,   5]
			( 1, 1) : [  8,   9]
			( 0, 1) : [  4,   9]
			(-1, 1) : [  0,   9]
			(-1, 0) : [  0,   5]
			(-1,-1) : [  0,   1]
			( 0,-1) : [  4,   1]
			( 1,-1) : [  8,   1]

		[5, 3] BAMBI (5)

			Right: True
			Down: False
			Left: False
			Top: False

			( 1, 0) : [  9,   3]
			( 1, 1) : [  9,   7]
			( 0, 1) : [  5,   7]
			(-1, 1) : [  1,   7]
			(-1, 0) : [  1,   3]
			(-1,-1) : [  1,  -1]
			( 0,-1) : [  5,  -1]
			( 1,-1) : [  9,  -1]

		[6, 4] BAMBI (5)

			Right: True
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 10,   4]
			( 1, 1) : [ 10,   8]
			( 0, 1) : [  6,   8]
			(-1, 1) : [  2,   8]
			(-1, 0) : [  2,   4]
			(-1,-1) : [  2,   0]
			( 0,-1) : [  6,   0]
			( 1,-1) : [ 10,   0]

		[6, 10] BAMBI (5)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 10,  10]
			( 1, 1) : [ 10,  14]
			( 0, 1) : [  6,  14]
			(-1, 1) : [  2,  14]
			(-1, 0) : [  2,  10]
			(-1,-1) : [  2,   6]
			( 0,-1) : [  6,   6]
			( 1,-1) : [ 10,   6]

		[7, 8] BAMBI (5)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 11,   8]
			( 1, 1) : [ 11,  12]
			( 0, 1) : [  7,  12]
			(-1, 1) : [  3,  12]
			(-1, 0) : [  3,   8]
			(-1,-1) : [  3,   4]
			( 0,-1) : [  7,   4]
			( 1,-1) : [ 11,   4]

		[0, 1] BETTY (5)

			Right: True
			Down: True
			Left: False
			Top: False

			( 1, 0) : [  4,   1]
			( 1, 1) : [  4,   5]
			( 0, 1) : [  0,   5]
			(-1, 1) : [ -4,   5]
			(-1, 0) : [ -4,   1]
			(-1,-1) : [ -4,  -3]
			( 0,-1) : [  0,  -3]
			( 1,-1) : [  4,  -3]

		[1, 2] BETTY (5)

			Right: True
			Down: True
			Left: False
			Top: False

			( 1, 0) : [  5,   2]
			( 1, 1) : [  5,   6]
			( 0, 1) : [  1,   6]
			(-1, 1) : [ -3,   6]
			(-1, 0) : [ -3,   2]
			(-1,-1) : [ -3,  -2]
			( 0,-1) : [  1,  -2]
			( 1,-1) : [  5,  -2]

		[4, 0] BETTY (5)

			Right: True
			Down: False
			Left: False
			Top: False

			( 1, 0) : [  8,   0]
			( 1, 1) : [  8,   4]
			( 0, 1) : [  4,   4]
			(-1, 1) : [  0,   4]
			(-1, 0) : [  0,   0]
			(-1,-1) : [  0,  -4]
			( 0,-1) : [  4,  -4]
			( 1,-1) : [  8,  -4]

		[4, 5] BETTY (5)

			Right: True
			Down: False
			Left: True
			Top: True

			( 1, 0) : [  8,   5]
			( 1, 1) : [  8,   9]
			( 0, 1) : [  4,   9]
			(-1, 1) : [  0,   9]
			(-1, 0) : [  0,   5]
			(-1,-1) : [  0,   1]
			( 0,-1) : [  4,   1]
			( 1,-1) : [  8,   1]

		[5, 3] BETTY (5)

			Right: True
			Down: False
			Left: False
			Top: False

			( 1, 0) : [  9,   3]
			( 1, 1) : [  9,   7]
			( 0, 1) : [  5,   7]
			(-1, 1) : [  1,   7]
			(-1, 0) : [  1,   3]
			(-1,-1) : [  1,  -1]
			( 0,-1) : [  5,  -1]
			( 1,-1) : [  9,  -1]

		[6, 4] BETTY (5)

			Right: True
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 10,   4]
			( 1, 1) : [ 10,   8]
			( 0, 1) : [  6,   8]
			(-1, 1) : [  2,   8]
			(-1, 0) : [  2,   4]
			(-1,-1) : [  2,   0]
			( 0,-1) : [  6,   0]
			( 1,-1) : [ 10,   0]

		[6, 10] BETTY (5)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 10,  10]
			( 1, 1) : [ 10,  14]
			( 0, 1) : [  6,  14]
			(-1, 1) : [  2,  14]
			(-1, 0) : [  2,  10]
			(-1,-1) : [  2,   6]
			( 0,-1) : [  6,   6]
			( 1,-1) : [ 10,   6]

		[7, 8] BETTY (5)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 11,   8]
			( 1, 1) : [ 11,  12]
			( 0, 1) : [  7,  12]
			(-1, 1) : [  3,  12]
			(-1, 0) : [  3,   8]
			(-1,-1) : [  3,   4]
			( 0,-1) : [  7,   4]
			( 1,-1) : [ 11,   4]

		[0, 3] DAGBERT (7)

			Right: True
			Down: True
			Left: False
			Top: False

			( 1, 0) : [  6,   3]
			( 1, 1) : [  6,   9]
			( 0, 1) : [  0,   9]
			(-1, 1) : [ -6,   9]
			(-1, 0) : [ -6,   3]
			(-1,-1) : [ -6,  -3]
			( 0,-1) : [  0,  -3]
			( 1,-1) : [  6,  -3]

		[1, 7] DAGBERT (7)

			Right: False
			Down: True
			Left: True
			Top: True

			( 1, 0) : [  7,   7]
			( 1, 1) : [  7,  13]
			( 0, 1) : [  1,  13]
			(-1, 1) : [ -5,  13]
			(-1, 0) : [ -5,   7]
			(-1,-1) : [ -5,   1]
			( 0,-1) : [  1,   1]
			( 1,-1) : [  7,   1]

		[2, 7] DAGBERT (7)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [  8,   7]
			( 1, 1) : [  8,  13]
			( 0, 1) : [  2,  13]
			(-1, 1) : [ -4,  13]
			(-1, 0) : [ -4,   7]
			(-1,-1) : [ -4,   1]
			( 0,-1) : [  2,   1]
			( 1,-1) : [  8,   1]

		[4, 7] DAGBERT (7)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 10,   7]
			( 1, 1) : [ 10,  13]
			( 0, 1) : [  4,  13]
			(-1, 1) : [ -2,  13]
			(-1, 0) : [ -2,   7]
			(-1,-1) : [ -2,   1]
			( 0,-1) : [  4,   1]
			( 1,-1) : [ 10,   1]

		[6, 7] DAGBERT (7)

			Right: False
			Down: False
			Left: True
			Top: True

			( 1, 0) : [ 12,   7]
			( 1, 1) : [ 12,  13]
			( 0, 1) : [  6,  13]
			(-1, 1) : [  0,  13]
			(-1, 0) : [  0,   7]
			(-1,-1) : [  0,   1]
			( 0,-1) : [  6,   1]
			( 1,-1) : [ 12,   1]



Process finished with exit code 0

"""