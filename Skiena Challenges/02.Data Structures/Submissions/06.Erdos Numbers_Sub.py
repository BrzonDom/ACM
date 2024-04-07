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


def readInput():

    PaperNum, NameNum = list(map(int, stdin.readline().split()))

    Papers = [stdin.readline() for _ in range(PaperNum)]
    Names = [stdin.readline().rstrip() for _ in range(NameNum)]

    return Papers, Names


def extractAuth(Papers):

    authData = {}

    for paper in Papers:

        """     Extract string of authors     """
        authStr = paper.split(":")[0]

        """     Split string of authors into a list   """
        authLst = authStr.split(", ")

        """     Modify list of authors      """
        for a in range(0, len(authLst), 2):
            authLst[a] = authLst[a] + ", " + authLst[a+1]

        authLst = authLst[::2]

        for auth in authLst:

            """     Record data of authors to co-authors    """
            for coAuth in authLst:

                if auth == coAuth:
                    continue

                if auth not in authData:
                    authData[auth] = [coAuth]

                else:
                    authData[auth] += [coAuth]

    return authData


def valueAuth(authData):

    valueData = {}

    curQueue = ["Erdos, P."]
    nxtQueue = []
    value = 0

    while curQueue:

        value += 1

        for auth in curQueue:

            coAuthLst = authData[auth]

            for coAuth in coAuthLst:

                if coAuth == "Erdos, P.":
                    continue

                if coAuth not in valueData:

                    valueData[coAuth] = value
                    nxtQueue.append(coAuth)

        curQueue, nxtQueue = nxtQueue, []

    return valueData


if __name__ == "__main__":

    """     Read line with number of scenarios  """
    ScenNum = int(stdin.readline())

    for scene in range(int(ScenNum)):

        # print(f"\n\n{scene+1}. Scene:\n")
        print(f"Scenario {scene+1}")

        Papers, Names = readInput()

        authData = extractAuth(Papers)

        valueData = valueAuth(authData)

        for name in Names:

            if name not in valueData:
                print(f"{name} infinity")

            else:
                print(f"{name} {valueData[name]}")

