"""
Depth-First Search (DFS) – Iterative and Recursive Implementation

https://www.techiedelight.com/depth-first-search/

    Depth–first search (DFS) is an algorithm for traversing or searching
    tree or graph data structures. One starts at the root
    (selecting some arbitrary node as the root for a graph) and
    explore as far as possible along each branch before backtracking.

"""

def makeGraph(edges):

    grph = {}

    for edge in edges:
        if edge[0] in grph:
            grph[edge[0]].append(edge[1])

            # print(f"[{edge[0]:2}, {edge[1]:2}]", end="  ")

        else:
            grph[edge[0]] = [edge[1]]

            # print(f"\n\t[{edge[0]:2}, {edge[1]:2}]", end="  ")

        if edge[1] in grph:
            grph[edge[1]].append(edge[0])

        else:
            grph[edge[1]] = [edge[0]]

    return grph


if __name__ == '__main__':

    print("03.DFS Depth-First Search.py\n")

    edges = [(1, 2), (1, 3), (1, 4), (2, 5),
             (2, 6), (5, 9), (5, 10), (4, 7),
             (4, 8), (7, 11), (7, 12)]

    edge_set = set()

    print("Edges:", end="")

    for edge in edges:
        if edge[0] in edge_set:

            print(f"[{edge[0]:2}, {edge[1]:2}]", end="  ")
        else:
            edge_set.add(edge[0])

            print(f"\n\t[{edge[0]:2}, {edge[1]:2}]", end="  ")

    print("\n")

    grph = makeGraph(edges)

    print("Two way graph:\n")

    for parent in sorted(grph):
        print(f"\t{parent:2}: {grph[parent]}")

    print("\n")