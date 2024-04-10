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


def getLetters(word):

    dataWord = {}

    for char in word:
        if char not in dataWord:
            dataWord[char] = 1

        else:
            dataWord[char] += 1

    return dataWord


# InputRaw_Str = InputRaw_Str[1:-1]
#
# print("Input:")
#
# print(InputRaw_Str)
# print()

from sys import stdin

if __name__ == "__main__":

    # InputStr_Lst = list(InputRaw_Str.split("\n"))
    #
    # print(InputStr_Lst)
    # print()

    InputLst = []

    Input = input()

    while Input != '\n' and Input != '':

        InputLst.append(Input)
        Input = input()

    # while True:
    #
    #     try:
    #         InputLst.append(input())
    #
    #     except EOFError:
    #         break

    words = ["", ""]

    for words[0], words[1] in zip(InputLst[:-1:2], InputLst[1::2]):

        print("\t1. Word:", words[0])
        print("\t2. Word:", words[1])
        print()

        dataWord = {0: {}, 1: {}}
        # print(dataWord)

        for w, word in enumerate(words):
            dataWord[w] = getLetters(word)

        # for w, word in enumerate(words):
        #     for char in word:
        #         if char not in dataWord[w]:
        #             dataWord[w][char] = 1
        #
        #         else:
        #             dataWord[w][char] += 1

        for wrd in dataWord:
            for data in dataWord[wrd]:
                print(f"\t\t\t{data} : {dataWord[wrd][data]}")

            print()
        print()

        commonChar = []
        commonStr = ""

        if len(dataWord[0]) <= len(dataWord[1]):

            for char in dataWord[0]:
                if char in dataWord[1]:
                    commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
                    commonStr += min(dataWord[0][char], dataWord[1][char]) * char

        else:
            for char in dataWord[1]:
                if char in dataWord[0]:
                    commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
                    commonStr += min(dataWord[0][char], dataWord[1][char]) * char

        # print(f"\t\tCommon characters: {commonChar} = {commonStr}")

        print(f"\t\tCommon characters: {commonChar}")
        print(f"\t\tCommon subseq.: {commonStr}")
        print()



        print("\n")

        # print(commonStr)
