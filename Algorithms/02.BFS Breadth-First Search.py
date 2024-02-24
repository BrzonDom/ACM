"""
Breadth-First Search (BFS) – Iterative and Recursive Implementation

https://www.techiedelight.com/breadth-first-search/

    Breadth–first search (BFS) is an algorithm for traversing or searching
    tree or graph data structures. It starts at the tree root
    (or some arbitrary node of a graph, sometimes referred to as a ‘search key’)
    and explores the neighbor nodes first before moving to the next-level neighbors.

    Breadth–first search (BFS) is a graph traversal algorithm that explores vertices
    in the order of their distance from the source vertex, where distance is
    the minimum length of a path from the source vertex to the node.

"""

if __name__ == '__main__':

    edges = [(1, 2), (1, 3), (1, 4), (2, 5),
             (2, 6), (5, 9), (5, 10), (4, 7),
             (4, 8), (7, 11), (7, 12)]


    nodes = {}

    print("Edges:")
    for edge in edges:
        if edge[0] in nodes:
            nodes[edge[0]].append(edge[1])

            print(f"[{edge[0]:2}, {edge[1]:2}]", end="  ")
        else:
            nodes[edge[0]] = [edge[1]]

            print(f"\n\t[{edge[0]:2}, {edge[1]:2}]", end="  ")
    print("\n")

    print("Nodes:")

    for parent in nodes:
        print(f"\t{parent}: ", end="")

        chldStr = ""
        for child in nodes[parent]:
            chldStr += f"{child:2}, "

        print(chldStr[:-2])
