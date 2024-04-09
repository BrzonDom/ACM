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
        print(f"{col+1:<5}", end="")
    print()

    for row in range(RowNum):
        line = InputStr_Lst.pop(0)

        for col in range(ColNum):

            Grid[row][col] = line[col].upper()

        print(f"\t\t\t{row+1}", Grid[row])
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

    # for word in Words:

    print()

"""__Output__"""
"""
Cases: 1

	1. case

		Rows: 8
		Cols: 11

				1    2    3    4    5    6    7    8    9    10   11   
			1 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'G']
			2 ['H', 'E', 'B', 'K', 'W', 'A', 'L', 'D', 'O', 'R', 'K']
			3 ['F', 'T', 'Y', 'A', 'W', 'A', 'L', 'D', 'O', 'R', 'M']
			4 ['F', 'T', 'S', 'I', 'M', 'R', 'L', 'Q', 'S', 'R', 'C']
			5 ['B', 'Y', 'O', 'A', 'R', 'B', 'E', 'D', 'E', 'Y', 'V']
			6 ['K', 'L', 'C', 'B', 'Q', 'W', 'I', 'K', 'O', 'M', 'K']
			7 ['S', 'T', 'R', 'E', 'B', 'G', 'A', 'D', 'H', 'R', 'B']
			8 ['Y', 'U', 'I', 'Q', 'L', 'X', 'C', 'N', 'B', 'J', 'F']


		Words: 4

			 WALDORF
			 BAMBI
			 BETTY
			 DAGBERT


		W : [(1, 4), (2, 4), (5, 5)]
		B : [(0, 1), (1, 2), (4, 0), (4, 5), (5, 3), (6, 4), (6, 10), (7, 8)]
		D : [(0, 3), (1, 7), (2, 7), (4, 7), (6, 7)]



Process finished with exit code 0

"""