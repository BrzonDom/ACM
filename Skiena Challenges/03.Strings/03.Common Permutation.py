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

# InputRaw_Str = """
# pretty
# women
# walking
# down
# the
# street
# """

InputRaw_Str = """
pretty
women
walking
down
the
street
banana
bandana
apple
pineapple
hello
hollow
"""


def getLetters(word):

    dataWord = {}

    for char in word:
        if char not in dataWord:
            dataWord[char] = 1

        else:
            dataWord[char] += 1

    return dataWord


def prntLetters(dataWord):

    for wrd in dataWord:
        for data in dataWord[wrd]:
            print(f"\t\t\t{data} : {dataWord[wrd][data]}")

        print()
    print()


def findCommonChar(dataWord):

    commonChar = []

    if len(dataWord[0]) <= len(dataWord[1]):

        for char in dataWord[0]:
            if char in dataWord[1]:
                commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
                # commonStr += min(dataWord[0][char], dataWord[1][char]) * char

    else:
        for char in dataWord[1]:
            if char in dataWord[0]:
                commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
                # commonStr += min(dataWord[0][char], dataWord[1][char]) * char

    commonChar.sort()
    return commonChar


def getCommonStr(commonChar):

    commonStr = ""

    for char in commonChar:
        commonStr += char

    return commonStr


def findCommonStr(dataWord):

    commonStr = ""

    if len(dataWord[0]) <= len(dataWord[1]):

        for char in dataWord[0]:
            if char in dataWord[1]:
                # commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
                commonStr += min(dataWord[0][char], dataWord[1][char]) * char

    else:
        for char in dataWord[1]:
            if char in dataWord[0]:
                # commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
                commonStr += min(dataWord[0][char], dataWord[1][char]) * char

    return ''.join(sorted(commonStr))


InputRaw_Str = InputRaw_Str[1:-1]

# print("Input:")
# print(InputRaw_Str)
# print()

if __name__ == "__main__":

    InputStr_Lst = list(InputRaw_Str.split("\n"))

    print("Input:")
    print("\t\t\"")

    for inLine in InputStr_Lst:
        print("\t\t", inLine)
    print("\t\t\"\n")

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
            dataWord[w] = getLetters(word)

        # for w, word in enumerate(words):
        #     for char in word:
        #         if char not in dataWord[w]:
        #             dataWord[w][char] = 1
        #
        #         else:
        #             dataWord[w][char] += 1

        # prntLetters(dataWord)

        # for wrd in dataWord:
        #     for data in dataWord[wrd]:
        #         print(f"\t\t\t{data} : {dataWord[wrd][data]}")
        #
        #     print()
        # print()

        commonChar = findCommonChar(dataWord)

        # if len(dataWord[0]) <= len(dataWord[1]):
        #
        #     for char in dataWord[0]:
        #         if char in dataWord[1]:
        #             commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
        #             # commonStr += min(dataWord[0][char], dataWord[1][char]) * char
        #
        # else:
        #     for char in dataWord[1]:
        #         if char in dataWord[0]:
        #             commonChar += min(dataWord[0][char], dataWord[1][char]) * [char]
        #             # commonStr += min(dataWord[0][char], dataWord[1][char]) * char
        #
        # commonChar.sort()

        # print("\t\tCommon unsorted characters: ", commonChar)
        # print("\t\tCommon sorted characters:   ", sorted(commonChar))

        print("\t\tCommon characters:", commonChar)

        commonStr = getCommonStr(commonChar)

        # commonStr = ""
        # for char in commonChar:
        #     commonStr += char

        print("\t\tCommon substring:", commonStr)
        print()

        commonStr = findCommonStr(dataWord)
        print("\t\tCommon substring:", commonStr)
        print("\n")


"""__Output__"""
"""
Input:
		"
		 pretty
		 women
		 walking
		 down
		 the
		 street
		 banana
		 bandana
		 apple
		 pineapple
		 hello
		 hollow
		"

['pretty', 'women', 'walking', 'down', 'the', 'street', 'banana', 'bandana', 'apple', 'pineapple', 'hello', 'hollow']

	1. Word: pretty
	2. Word: women

		Common characters: ['e']
		Common substring: e

		Common substring: e


	1. Word: walking
	2. Word: down

		Common characters: ['n', 'w']
		Common substring: nw

		Common substring: nw


	1. Word: the
	2. Word: street

		Common characters: ['e', 't']
		Common substring: et

		Common substring: et


	1. Word: banana
	2. Word: bandana

		Common characters: ['a', 'a', 'a', 'b', 'n', 'n']
		Common substring: aaabnn

		Common substring: aaabnn


	1. Word: apple
	2. Word: pineapple

		Common characters: ['a', 'e', 'l', 'p', 'p']
		Common substring: aelpp

		Common substring: aelpp


	1. Word: hello
	2. Word: hollow

		Common characters: ['h', 'l', 'l', 'o']
		Common substring: hllo

		Common substring: hllo



Process finished with exit code 0

"""