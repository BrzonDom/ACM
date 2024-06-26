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

InputRaw_Str = """
2

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
from sys import stdin

def makeGrid(RowNum, ColNum):

    Grid = [["" for c in range(ColNum)] for r in range(RowNum)]

    # print("\t\t\t\t", end="")
    # for col in range(ColNum):
    #     print(f"{col:<5}", end="")
    # print()

    for row in range(RowNum):
        # line = InputStr_Lst.pop(0)
        line = stdin.readline()

        for col in range(ColNum):
            Grid[row][col] = line[col].upper()

    #     print(f"\t\t\t{row}", Grid[row])
    # print("\n")

    return Grid


def getStart(RowNum, ColNum, Grid, strtChar):

    strtIndx = {}

    for char in strtChar:
        strtIndx[char] = []

    for row in range(RowNum):
        for col in range(ColNum):

            for char in strtChar:

                if Grid[row][col] == char:
                    strtIndx[char].append((row, col))

    # for strt in strtIndx:
    #     print(f"\t\t{strt} : {strtIndx[strt]}")
    # print("\n")

    return strtIndx


def canFit(lenWord, RowNum, ColNum, strRow, strCol):

    bordRight = (strCol + lenWord - 1) < ColNum
    bordDown = (strRow + lenWord - 1) < RowNum
    bordLeft = (strCol - (lenWord - 1)) >= 0
    bordUp = (strRow - (lenWord - 1)) >= 0

    return bordRight, bordDown, bordLeft, bordUp


def findWord(Words, Grid, RowNum, ColNum, strtIndx):

    wordStrt = {}

    for word in Words:
        for start in strtIndx[word[0]]:

            strRow, strCol = start

            # print(f"\t\t[{strRow}, {strCol}] {word} ({len(word)})")

            right, down, left, up = canFit(len(word), RowNum, ColNum, strRow, strCol)

            if down:
                # print(f"\t\t\t( 1, 0) : [{strRow + len(word) - 1:3}, {strCol:3}]")

                for nxt, nxtChar in enumerate(word[1:]):
                    found = True

                    if nxtChar != Grid[strRow + nxt + 1][strCol]:
                        found = False
                        break

                if found:
                    # print(f"\n\tFound ( 1, 0) : [{strRow:3}, {strCol:3}] => [{strRow + len(word) - 1:3}, {strCol:3}]\n")
                    wordStrt[word] = [strRow, strCol]
                    break

                if right and not found:
                    # print(f"\t\t\t( 1, 1) : [{strRow + len(word) - 1:3}, {strCol + len(word) - 1:3}]")

                    for nxt, nxtChar in enumerate(word[1:]):
                        found = True

                        if nxtChar != Grid[strRow + nxt + 1][strCol + nxt + 1]:
                            found = False
                            break

                    if found:
                        # print(f"\n\tFound ( 1, 1) : [{strRow:3}, {strCol:3}] => [{strRow + len(word) - 1:3}, {strCol + len(word) - 1:3}]\n")
                        wordStrt[word] = [strRow, strCol]
                        break

            if right:
                # print(f"\t\t\t( 0, 1) : [{strRow:3}, {strCol + len(word) - 1:3}]")

                for nxt, nxtChar in enumerate(word[1:]):
                    found = True

                    if nxtChar != Grid[strRow][strCol + nxt + 1]:
                        found = False
                        break

                if found:
                    # print(f"\n\tFound ( 0, 1) : [{strRow:3}, {strCol:3}] => [{strRow:3}, {strCol + len(word) - 1:3}]\n")
                    wordStrt[word] = [strRow, strCol]
                    break

                if up:
                    # print(f"\t\t\t(-1, 1) : [{strRow - (len(word) - 1):3}, {strCol + len(word) - 1:3}]")

                    for nxt, nxtChar in enumerate(word[1:]):
                        found = True

                        if nxtChar != Grid[strRow - (nxt + 1)][strCol + nxt + 1]:
                            found = False
                            break

                    if found:
                        # print(f"\n\tFound (-1, 1) : [{strRow:3}, {strCol:3}] => [{strRow - (len(word) - 1):3}, {strCol + len(word) - 1:3}]\n")
                        wordStrt[word] = [strRow, strCol]
                        break

            if up:
                # print(f"\t\t\t(-1, 0) : [{strRow - (len(word) - 1):3}, {strCol:3}]")

                for nxt, nxtChar in enumerate(word[1:]):
                    found = True

                    if nxtChar != Grid[strRow - (nxt + 1)][strCol]:
                        found = False
                        break

                if found:
                    # print(f"\n\tFound (-1, 0) : [{strRow:3}, {strCol:3}] => [{strRow - (len(word) - 1):3}, {strCol:3}]\n")
                    wordStrt[word] = [strRow, strCol]
                    break

                if left:
                    # print(f"\t\t\t(-1,-1) : [{strRow - (len(word) - 1):3}, {strCol - (len(word) - 1):3}]")

                    for nxt, nxtChar in enumerate(word[1:]):
                        found = True

                        if nxtChar != Grid[strRow - (nxt + 1)][strCol - (nxt + 1)]:
                            found = False
                            break

                    if found:
                        # print(f"\n\tFound (-1,-1) : [{strRow:3}, {strCol:3}] => [{strRow - (len(word) - 1):3}, {strCol - (len(word) - 1):3}]\n")
                        wordStrt[word] = [strRow, strCol]
                        break

            if left:
                # print(f"\t\t\t( 0,-1) : [{strRow:3}, {strCol - (len(word) - 1):3}]")

                for nxt, nxtChar in enumerate(word[1:]):
                    found = True

                    if nxtChar != Grid[strRow][strCol - (nxt + 1)]:
                        found = False
                        break

                if found:
                    # print(f"\n\tFound ( 0,-1) : [{strRow:3}, {strCol:3}] => [{strRow:3}, {strCol - (len(word) - 1):3}]\n")
                    wordStrt[word] = [strRow, strCol]
                    break

                if down:
                    # print(f"\t\t\t( 1,-1) : [{strRow + len(word) - 1:3}, {strCol - (len(word) - 1):3}]")

                    for nxt, nxtChar in enumerate(word[1:]):
                        found = True

                        if nxtChar != Grid[strRow + nxt + 1][strCol - (nxt + 1)]:
                            found = False
                            break

                    if found:
                        # print(f"\n\tFound ( 1,-1) : [{strRow:3}, {strCol:3}] => [{strRow + len(word) - 1:3}, {strCol - (len(word) - 1):3}]\n")
                        wordStrt[word] = [strRow, strCol]
                        break
    #         print()
    # print()

    return wordStrt


if __name__ == "__main__":

    caseNum = int(stdin.readline())

    # print(f"Cases: {caseNum}\n")

    for case in range(caseNum):

        # print(f"\t{case+1}. case\n")

        stdin.readline()

        RowNum, ColNum = list(map(int, stdin.readline().split()))

        # print(f"\t\tRows: {RowNum}")
        # print(f"\t\tCols: {ColNum}")
        # print()

        Grid = makeGrid(RowNum, ColNum)

        wordNum = int(stdin.readline())

        InWords = []
        Words = []
        strtChar = set()

        # print(f"\t\tWords: {wordNum}\n")

        for w in range(wordNum):

            # Words.append(InputStr_Lst.pop(0).upper())
            InWords.append(stdin.readline().strip())
            Words.append(InWords[-1].upper())
            strtChar.add(Words[-1][0])

        #     print("\t\t\t", Words[-1])
        # print("\n")

        strtIndx = getStart(RowNum, ColNum, Grid, strtChar)

        wordStrt = findWord(Words, Grid, RowNum, ColNum, strtIndx)

        for word in InWords:
            # print(f"\t{word:7} : [{wordStrt[word.upper()][0] + 1}, {wordStrt[word.upper()][1] + 1}]")
            print(wordStrt[word.upper()][0] + 1, wordStrt[word.upper()][1] + 1)

        if case < caseNum-1:
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
			( 1, 0) : [  7,   4]
			( 1, 1) : [  7,  10]

	Found ( 1, 1) : [  1,   4] => [  7,  10]

		[0, 1] BAMBI (5)
			( 1, 0) : [  4,   1]
			( 1, 1) : [  4,   5]
			( 0, 1) : [  0,   5]

		[1, 2] BAMBI (5)
			( 1, 0) : [  5,   2]
			( 1, 1) : [  5,   6]

	Found ( 1, 1) : [  1,   2] => [  5,   6]

		[0, 1] BETTY (5)
			( 1, 0) : [  4,   1]

	Found ( 1, 0) : [  0,   1] => [  4,   1]

		[0, 3] DAGBERT (7)
			( 1, 0) : [  6,   3]
			( 1, 1) : [  6,   9]
			( 0, 1) : [  0,   9]

		[1, 7] DAGBERT (7)
			( 1, 0) : [  7,   7]
			( 0,-1) : [  1,   1]
			( 1,-1) : [  7,   1]

		[2, 7] DAGBERT (7)
			( 0,-1) : [  2,   1]

		[4, 7] DAGBERT (7)
			( 0,-1) : [  4,   1]

		[6, 7] DAGBERT (7)
			(-1, 0) : [  0,   7]
			(-1,-1) : [  0,   1]
			( 0,-1) : [  6,   1]

	Found ( 0,-1) : [  6,   7] => [  6,   1]


	WALDORF : [2, 5]
	BAMBI   : [2, 3]
	BETTY   : [1, 2]
	DAGBERT : [7, 8]


Process finished with exit code 0

"""