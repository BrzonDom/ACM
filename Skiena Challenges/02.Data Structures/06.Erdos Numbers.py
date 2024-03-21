"""

Erdos Numbers

    An author who has
    jointly published with Erdos had Erdos number 1. An author who had not published
    with Erdos but with somebody with Erdos number 1 obtained Erdos number 2, and so on.

    Input:
        The first line of the input contains the number of scenarios. Each scenario consists of
        a paper database and a list of names. It begins with the line P N, where P and N are
        natural numbers. Following this line is the paper database, with P lines each containing
        the description of one paper specified in the following way:
        Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors
        Note that umlauts, like “¨o,” are simply written as “o”. After the P papers follow N
        lines with names. Such a name line has the following format:
        Martin, G.

    Output:
        For every scenario you are to print a line containing a string “Scenario i” (where i is
        the number of the scenario) and the author names together with their Erdos number of
        all authors in the list of names. The authors should appear in the same order as they
        appear in the list of names. The Erdos number is based on the papers in the paper
        database of this scenario. Authors which do not have any relation to Erdos via the
        papers in the database have Erdos number “infinity.”


    Sample:
        1
        4 3
        Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors
        Erdos, P., Reisig, W.: Stuttering in petri nets
        Smith, M.N., Chen, X.: First order derivates in structured programming
        Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
        Smith, M.N.
        Hsueh, Z.
        Chen, X.

"""

Input_Str = """
1
4 3
Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors
Erdos, P., Reisig, W.: Stuttering in petri nets
Smith, M.N., Chen, X.: First order derivates in structured programming
Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
Smith, M.N.
Hsueh, Z.
Chen, X.
"""

# ScenNum, PaperNameCnt, PapersNames = Input_Str.split("\n", 3)[1:]

# Input_Lst = Input_Str.split("\n", 3)[1:]

ScenNum, Input_Str = Input_Str.split("\n", 2)[1:]
