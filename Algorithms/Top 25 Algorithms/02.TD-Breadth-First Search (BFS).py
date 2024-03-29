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

from collections import deque


# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Perform BFS on the graph starting from vertex `v`
def BFS_Iter(graph, v, discovered):
    # create a queue for doing BFS
    q = deque()

    # mark the source vertex as discovered
    discovered[v] = True

    # enqueue source vertex
    q.append(v)

    # loop till queue is empty
    while q:

        # dequeue front node and print it
        v = q.popleft()
        print(v, end=' ')

        # do for every edge (v, u)
        for u in graph.adjList[v]:
            if not discovered[u]:
                # mark it as discovered and enqueue it
                discovered[u] = True
                q.append(u)


# Perform BFS recursively on the graph
def BFS_Recu(graph, q, discovered):
    if not q:
        return

    # dequeue front node and print it
    v = q.popleft()
    print(v, end=' ')

    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            # mark it as discovered and enqueue it
            discovered[u] = True
            q.append(u)

    BFS_Recu(graph, q, discovered)


if __name__ == '__main__':

    print("02.TD-Breadth-First Search (BFS).py\n")

    # List of graph edges as per the above diagram
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]

    print("Edges:")
    for edge in edges:
        print(f"\t{edge[0]:2} {edge[1]:2}")
    print()

    # total number of nodes in the graph (labelled from 0 to 14)
    n = 13

    # build a graph from the given edges
    graph = Graph(edges, n)

    print()
    print("Iterative Implementation:", end="\n\t")

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            # start BFS traversal from vertex i
            BFS_Iter(graph, i, discovered)

    print("\n")
    print("Recursive Implementation:", end="\n\t")

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # create a queue for doing BFS
    q = deque()

    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            # mark the source vertex as discovered
            discovered[i] = True

            # enqueue source vertex
            q.append(i)

            # start BFS traversal from vertex i
            BFS_Recu(graph, q, discovered)

    print()