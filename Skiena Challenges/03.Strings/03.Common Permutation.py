"""

Common Permutation

        Given two strings a and b, print the longest string x of letters such that there is a
    permutation of x that is a subsequence of a and there is a permutation of x that is a
    subsequence of b.

    Input:
            The input file contains several cases, each case consisting of two consecutive lines. This
        means that lines 1 and 2 are a test case, lines 3 and 4 are another test case, and so on.
        Each line contains one string of lowercase characters, with first line of a pair denoting
        a and the second denoting b. Each string consists of at most 1,000 characters

    Output:
            For each set of input, output a line containing x. If several x satisfy the criteria above,
        choose the first one in alphabetical order


    Sample:
        pretty
        women
        walking
        down
        the
        street
            =>  e
                nw
                et

"""

InputRaw_Str = """
pretty
women
walking
down
the
street
"""

InputRaw_Str = InputRaw_Str[1:-1]

print("Input:")

print(InputRaw_Str)

InputStr_Lst = list(InputRaw_Str.split("\n"))

print(InputStr_Lst)
print()

words = ["", ""]

for words[0], words[1] in zip(InputStr_Lst[:-1:2], InputStr_Lst[1::2]):
    print("\t1. Word:", words[0])
    print("\t2. Word:", words[1])
    print()

    dataWord = {0: {}, 1: {}}
    # print(dataWord)

    for w, word in enumerate(words):
        for char in word:
            if char not in dataWord[w]:
                dataWord[w][char] = 1

            else:
                dataWord[w][char] += 1

    print(dataWord)
