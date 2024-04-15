"""
121 - Pipe Fitters
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=57

        A pipe is an operating system concept that permits data
    to “flow” between processes (and allows filters to be chained together easily.)
    This problem involves maximizing the number of pipes that can be fit into a storage container (but
    it’s a pipe fitting problem, not a bin packing problem).
        A company manufactures pipes of uniform diameter. All pipes are stored in rectangular storage
    containers, but the containers come in several different sizes. Pipes are stored in rows within a container
    so that there is no space between pipes in any row (there may be some space at the end of a row), i.e.,
    all pipes in a row are tangent, or touch. Within a rectangular cross-section, pipes are stored in either
    a grid pattern or a skew pattern as shown below: the two left-most cross-sections are in a grid pattern,
    the two right-most cross-sections are in a skew pattern.

    Input:
            The input is a sequence of cross-section dimensions of storage containers. Each cross-section is given
        as two real values on one line separated by white space. The dimensions are expressed in units of pipe
        diameters. All dimensions will be less than 2^7. Note that a cross section with dimensions a × b can also
        be viewed as a cross section with dimensions b × a.

    Output:
            For each cross-section in the input, your program should print the maximum number of pipes that can
        be packed into that cross section. The number of pipes is an integer — no fractional pipes can be
        packed. The maximum number is followed by the word ‘grid’ if a grid pattern results in the maximal
        number of pipes or the word ‘skew’ if a skew pattern results in the maximal number of pipes. If the
        pattern doesn’t matter, that is the same number of pipes can be packed with either a grid or skew
        pattern, then the word ‘grid’ should be printed.


    Sample:
        3 3
        2.9 10
        2.9 10.5
        11 11
            =>  9 grid
                29 skew
                30 skew
                126 skew

"""

InputRaw_Str = """
3 3
2.9 10
2.9 10.5
11 11
"""

InputRaw_Str = InputRaw_Str[1:-1]

print("Input:")
print(InputRaw_Str)
print()

InputStr_Lst = InputRaw_Str.split("\n")

for i, line in enumerate(InputStr_Lst):
    print(f"\t{i+1}. Input:")
    print(f"\t\t{line}")
    print()
