"""
Breadth-First Search (BFS) – Iterative and Recursive Implementation

https://www.techiedelight.com/breadth-first-search/

    Breadth–first search (BFS) is an algorithm for traversing or searching
    tree or graph data structures. It starts at the tree root
    (or some arbitrary node of a graph, sometimes referred to as a ‘search key’)
    and explores the neighbor grph_one first before moving to the next-level neighbors.

    Breadth–first search (BFS) is a graph traversal algorithm that explores vertices
    in the order of their distance from the source vertex, where distance is
    the minimum length of a path from the source vertex to the node.

"""

if __name__ == '__main__':

    edges = [(1, 2), (1, 3), (1, 4), (2, 5),
             (2, 6), (5, 9), (5, 10), (4, 7),
             (4, 8), (7, 11), (7, 12)]

    grph_one = {}
    grph_both = {}

    print("Edges:", end="")

    for edge in edges:
        if edge[0] in grph_one:
            grph_one[edge[0]].append(edge[1])
            grph_both[edge[0]].append(edge[1])

            # print(f"[{edge[0]:2}, {edge[1]:2}]", end="  ")
        else:
            grph_one[edge[0]] = [edge[1]]
            grph_both[edge[0]] = [edge[1]]

            # print(f"\n\t[{edge[0]:2}, {edge[1]:2}]", end="  ")

        if edge[1] in grph_both:
            grph_both[edge[1]].append(edge[0])

        else:
            grph_both[edge[1]] = [edge[0]]


    print("\n")

    print("Nodes:")

    for parent in grph_one:
        print(f"\t{parent}: ", end="")

        chldStr = ""
        for child in grph_one[parent]:
            chldStr += f"{child:2}, "

        print(chldStr[:-2])

    # visited = []
    # queue = [grph_one]
    #
    # print(queue)
    # while queue:
    #
    #     if queue[0] not in visited:
    #         print(queue[0])

    # for parent in grph_one:
    #     if parent not in queue:
