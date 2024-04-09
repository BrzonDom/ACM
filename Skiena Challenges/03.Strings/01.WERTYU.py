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

InputRaw_Str = "O S, GOMR YPFSU/"

decodeDict = {'1':'`', '2':'1', '3':'2', '4':'3', '5':'4', '6':'5',
              '7':'6', '8':'7', '9':'8', '0':'9', '-':'0', '=':'-',

              'W':'Q', 'E':'W', 'R':'E', 'T':'R', 'Y':'T', 'U':'Y',
              'I':'U', 'O':'I', 'P':'O', '[':'P', ']':'[', '\\':']'
              }


print(f"Input: {InputRaw_Str}")
print()

row1 = "`1234567890-="
row2 = "QWERTYUIOP[]\\"
row3 = "ASDFGHJKL;'"
row4 = "ZXCVBNM,./"

rows = [row1, row2, row3, row4]

for row in rows:
    for c, char in enumerate(row[1:]):
        print(f"\'{char}\' : \'{row[c]}\'", end=", ")
    print()