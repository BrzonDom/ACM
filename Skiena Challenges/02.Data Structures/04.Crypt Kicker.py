"""

Crypt Kicker

    Input:
        The input consists of a line containing an integer n, followed by n lowercase words, one
        per line, in alphabetical order. These n words compose the dictionary of words which
        may appear in the decrypted text. Following the dictionary are several lines of input.
        Each line is encrypted as described above.
        There are no more than 1,000 words in the dictionary. No word exceeds 16 letters.
        The encrypted lines contain only lower case letters and spaces and do not exceed 80
        characters in length

    Output:
        Decrypt each line and print it to standard output. If there are multiple solutions, any
        one will do. If there is no solution, replace every letter of the alphabet by an asterisk.


    Sample:

        6
        and
        dick
        jane
        puff
        spot
        yertle
        bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn
        xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd

            => dick and jane and puff and spot and yertle
               **** *** **** *** **** *** **** *** ******

"""
