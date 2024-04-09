"""

WERTYU

    Input:
        Input consists of several lines of text. Each line may contain digits, spaces, uppercase
        letters (except “Q”, “A”, “Z”), or punctuation shown above [except back-quote (‘)].
        Keys labeled with words [Tab, BackSp, Control, etc.] are not represented in the input.

    Output:
        You are to replace each letter or punctuation symbol by the one immediately to its left
        on the QWERTY keyboard shown above. Spaces in the input should be echoed in the
        output.


    Sample:
        O S, GOMR YPFSU/
            =>  I AM FINE TODAY.

"""
import sys
from sys import stdin

InputStr = "O S, GOMR YPFSU/"

decodeDict = {'1': '`', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5',
              '7': '6', '8': '7', '9': '8', '0': '9', '-': '0', '=': '-',

              'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T', 'U': 'Y',
              'I': 'U', 'O': 'I', 'P': 'O', '[': 'P', ']': '[', '\\': ']',

              'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G', 'J': 'H',
              'K': 'J', 'L': 'K', ';': 'L', '\'': ';',

              'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B', 'M': 'N',
              ',': 'M', '.': ',', '/': '.'
              }

if __name__ == "__main__":

    InputStr = ""

    for line in sys.stdin:
        InputStr += line

    # print(f"Input: {InputStr}")
    # print()

    OutputStr = ""

    for char in InputStr:
        if char in decodeDict:
            OutputStr += decodeDict[char]
        else:
            OutputStr += char

    # print(f"\tEncoded string: {InputStr}")
    # print(f"\tDecoded string: {OutputStr}")

    print(OutputStr)
    print()

"""__Output__"""
"""
Input: O S, GOMR YPFSU/

	Encoded string: O S, GOMR YPFSU/
	Decoded string: I AM FINE TODAY.


Process finished with exit code 0
"""