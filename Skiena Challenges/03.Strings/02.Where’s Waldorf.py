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

# print("Input:")
# print(InputRaw_Str)

InputStr_Lst = InputRaw_Str.split("\n")
print(InputStr_Lst)

caseNum = int(InputStr_Lst.pop(0))

print(f"Cases: {caseNum}\n")

for case in range(caseNum):

    print(f"\t{case+1}. case\n")

    InputStr_Lst.pop(0)

