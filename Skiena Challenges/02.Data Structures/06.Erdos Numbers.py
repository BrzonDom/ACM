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

for scene in range(int(ScenNum)):

    Work_Dict = {}
    Auth_Dict = {}

    print(f"{scene+1}. Scene:\n")

    PaperNameNum, Input_Str = Input_Str.split("\n", 1)

    PaperNum, NameNum = list(map(int, PaperNameNum.split()))

    print(f"\tNum. of Papers:  {PaperNum}")
    print(f"\tNum. of Names:   {NameNum}")
    print()

    Papers = list(Input_Str.split("\n", PaperNum)[:PaperNum])
    Input_Str = Input_Str.split("\n", PaperNum)[PaperNum]

    Authors = set()
    Works = set()

    print("\tPapers:")
    for paper in Papers:
        print(f"\t\t{paper}")

        Auth_Str, Work_Str = paper.split(":")

        Auth_Lst = Auth_Str.split(", ")

        for a in range(0, len(Auth_Lst), 2):
            Authors.add(Auth_Lst[a] + " " + Auth_Lst[a+1])
            Auth_Lst[a] = Auth_Lst[a] + " " + Auth_Lst[a+1]

        Auth_Lst = Auth_Lst[0::2]

        Work_Dict[Work_Str[1:]] = Auth_Lst

        for auth in Auth_Lst:

            # if auth != "Erdos P.":
            #     Erdo_Dict[auth] = 0

            for coAuth in Auth_Lst:
                if auth == coAuth:
                    continue

                if auth not in Auth_Dict:
                    Auth_Dict[auth] = [coAuth]

                else:
                    Auth_Dict[auth] += [coAuth]

        # for work in Auth_Lst:


        Works.add(Work_Str[1:])

    print()

    Names = list(Input_Str.split("\n", NameNum)[:NameNum])
    Input_Str = Input_Str.split("\n", NameNum)[NameNum]

    print("\tNames:")
    for name in Names:
        print(f"\t\t{name}")
    print("\n")

    print("\tAuthors:")
    for auth in Authors:
        print(f"\t\t{auth}")
    print()

    print("\tWorks:")
    for work in Works:
        print(f"\t\t{work}")
    print("\n")

    maxAthLen = len(max(Auth_Dict.keys(), key=len))

    print("\tAuthors data:")
    for auth in Auth_Dict:
        print(f"\t\t{auth:{maxAthLen}} : {Auth_Dict[auth]}")
    print()

    maxWrkLen = len(max(Work_Dict.keys(), key=len))
    # print(maxWrkLen)

    print("\tWorks data:")
    for work in Work_Dict:
        print(f"\t\t{work:{maxWrkLen}} : {Work_Dict[work]}")
    print("\n")

    Erdo_Dict = {}
    # Erdo_Queue = [[]]
    Erdo_Queue = [[], []]
    ErdoCnt = 1

    for auth in Auth_Dict["Erdos P."]:
        Erdo_Dict[auth] = ErdoCnt
        Erdo_Queue[0].append(auth)

    # while len(max(Erdo_Queue, key=len)) > 0:
    while Erdo_Queue[0]:

        ErdoCnt += 1

        # if Erdo_Queue[-1]:
        #     Erdo_Queue.append([])

        # for q, queue in enumerate(Erdo_Queue):
        for a, auth in enumerate(Erdo_Queue[0]):

            # if auth == "Erdos P.":
            #     continue

            coAuth_Lst = Auth_Dict[auth]

            for coAuth in coAuth_Lst:

                if coAuth == "Erdos P.":
                    continue

                if coAuth not in Erdo_Dict:
                    Erdo_Queue[1].append(coAuth)
                    Erdo_Dict[coAuth] = ErdoCnt

            # if len(Erdo_Queue) <= q + 1:
            #     Erdo_Queue.append([])

            # for auth in queue:
            #
            #     coAuth_Lst = Auth_Dict[auth]
            #
            #     for coAuth in coAuth_Lst:
            #
            #         if coAuth == "Erdos P.":
            #             continue
            #
            #         if coAuth not in Erdo_Dict:
            #             Erdo_Queue[q+1].append(coAuth)
            #             Erdo_Dict[coAuth] = q + 2
            #
            # Erdo_Queue[q] = []

        Erdo_Queue[0] = Erdo_Queue[1]
        Erdo_Queue[1] = []



    print("\tErdos authors:")
    for auth in Erdo_Dict:
        print(f"\t\t{auth:{maxAthLen}} : {Erdo_Dict[auth]}")


    print("\n")