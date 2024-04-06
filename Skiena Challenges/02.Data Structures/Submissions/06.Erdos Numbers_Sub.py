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
            =>  Scenario 1
                Smith, M.N. 1
                Hsueh, Z. infinity
                Chen, X. 2

"""

Input_Str = """
2
4 3
Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors
Erdos, P., Reisig, W.: Stuttering in petri nets
Smith, M.N., Chen, X.: First order derivates in structured programming
Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
Smith, M.N.
Hsueh, Z.
Chen, X.
3 3
Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factors
Smith, M.N., Chen, X., Hsueh, Z.: First order derivates in structured programming
Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
Martin, G.
Hsueh, Z.
Jablonski, T.

"""
from sys import stdin

if __name__ == "__main__":

    """     Read line with number of scenarios  """
    ScenNum = int(stdin.readline())

    for scene in range(int(ScenNum)):

        # print(f"\n\n{scene+1}. Scene:\n")
        print(f"Scenario {scene+1}")

        """     Read line with numbers of papers and names      """
        PaperNameStr = stdin.readline()

        """     Extract number of papers and names      """
        PaperNum, NameNum = list(map(int, PaperNameStr.split()))

        # print(f"\tNum. of Papers:  {PaperNum}")
        # print(f"\tNum. of Names:   {NameNum}")
        # print()

        """     Extract list of papers      """
        Papers = [stdin.readline().rstrip() for _ in range(PaperNum)]

        Authors = set()
        Auth_Dict = {}

        # print("\tPapers:")
        for paper in Papers:
            # print(f"\t\t{paper}")

            """     Extract authors     """
            Auth_Str = paper.split(":")[0]

            """     Split authors into a list   """
            Auth_Lst = Auth_Str.split(", ")

            """     Modify list of authors      """
            for a in range(0, len(Auth_Lst), 2):

                """     Add to set of authors       """
                Authors.add(Auth_Lst[a] + ", " + Auth_Lst[a+1])
                Auth_Lst[a] = Auth_Lst[a] + ", " + Auth_Lst[a+1]

            Auth_Lst = Auth_Lst[0::2]

            for auth in Auth_Lst:

                """     Record data of authors to co-authors    """
                for coAuth in Auth_Lst:
                    if auth == coAuth:
                        continue

                    if auth not in Auth_Dict:
                        Auth_Dict[auth] = [coAuth]

                    else:
                        Auth_Dict[auth] += [coAuth]

        # print()

        Names = [stdin.readline().rstrip() for _ in range(NameNum)]

        """     Print needed names      """
        # print("\tNames:")
        # for name in Names:
        #     print(f"\t\t{name}")
        # print("\n")

        maxAthLen = len(max(Auth_Dict.keys(), key=len))

        """     Print data of authors to co-authors     """
        # print("\tAuthors data:")
        # for auth in Auth_Dict:
        #     print(f"\t\t{auth:{maxAthLen}} : {Auth_Dict[auth]}")
        # print()

        """     Data of Erdo value          """
        ErdoVal_Dict = {}

        """     Queue for Erdo value levels """
        Erdo_Queue = [["Erdos, P."], []]

        ErdoCnt = 0

        # print("\t\tErdos values process:\n")

        while Erdo_Queue[0]:

            ErdoCnt += 1

            # print(f"\t\t\t{ErdoCnt}. Erdo value")
            # print(f"\t\t\t\tQueue: {Erdo_Queue[0]}")
            # print("\t\t\t\tValues:", ErdoVal_Dict)
            # print()

            for a, auth in enumerate(Erdo_Queue[0]):

                coAuth_Lst = Auth_Dict[auth]
                # print(f"\t\t\t\t\tCo-auth. of {auth}: {coAuth_Lst}")

                for coAuth in coAuth_Lst:

                    if coAuth == "Erdos, P.":
                        continue

                    if coAuth not in ErdoVal_Dict:
                        Erdo_Queue[1].append(coAuth)
                        ErdoVal_Dict[coAuth] = ErdoCnt

            Erdo_Queue[0] = Erdo_Queue[1]
            Erdo_Queue[1] = []

        #     print()
        # print()

        for auth in Authors:
            if auth == "Erdos, P.":
                continue

            if auth not in ErdoVal_Dict:
                ErdoVal_Dict[auth] = "infinity"

        # print("\tErdos authors:")
        for auth in Names:
            # print(f"\t\t{auth:{maxAthLen}} : {ErdoVal_Dict[auth]}")

            print(f"{auth} {ErdoVal_Dict[auth]}")

        # print("\n")

    # endLine = stdin.readline()
