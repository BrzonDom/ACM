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


def edgeToGraph(edges):

    grph = {}

    for edge in edges:
        if edge[0] in grph:
            grph[edge[0]].append(edge[1])

            print(f"[{edge[0]:2}, {edge[1]:2}]", end="  ")

        else:
            grph[edge[0]] = [edge[1]]

            print(f"\n\t[{edge[0]:2}, {edge[1]:2}]", end="  ")

        if edge[1] in grph:
            grph[edge[1]].append(edge[0])

        else:
            grph[edge[1]] = [edge[0]]

    return grph


def BFS_Iter(grph, start = None, end = None):

    if start is None:
        start = min(list(grph.keys()))

    queue = [start]
    visited = {start}

    while len(queue) > 0:
        node = queue.pop(0)
        visited.add(node)

        print(node)

        if node == end:
            return

        for next in grph[node]:
            if next not in visited:

                visited.add(next)
                queue = queue + [next]



if __name__ == '__main__':

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

    # print("One way graph:")
    #
    # for parent in sorted(grph_one):
    #     print(f"\t{parent:2}: ", end="")
    #
    #     chldStr = ""
    #     for child in grph_one[parent]:
    #         chldStr += f"{child:2}, "
    #
    #     print(chldStr[:-2])
    #
    # print("\n")

    # print("Two way graph:")

    # for parent in sorted(grph_both):
    #     print(f"\t{parent:2}: {grph_both[parent]}")
    #
    #
    # print("\n")


    # BFS_Iter(grph_one)