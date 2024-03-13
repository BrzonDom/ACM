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


# Function to perform DFS traversal on the graph on a graph
def DFS_Recu(graph, v, discovered):
    discovered[v] = True  # mark the current node as discovered
    print(v, end=' ')  # print the current node

    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:  # if `u` is not yet discovered
            DFS_Recu(graph, u, discovered)


# Perform iterative DFS on graph starting from vertex `v`
def DFS_Iter(graph, v, discovered):
    # create a stack used to do iterative DFS
    stack = deque()

    # push the source node into the stack
    stack.append(v)

    # loop till stack is empty
    while stack:

        # Pop a vertex from the stack
        v = stack.pop()

        # if the vertex is already discovered yet, ignore it
        if discovered[v]:
            continue

        # we will reach here if the popped vertex `v` is not discovered yet;
        # print `v` and process its undiscovered adjacent nodes into the stack
        discovered[v] = True
        print(v, end=' ')

        # do for every edge (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)


if __name__ == '__main__':

    print("03.TD-Depth-First Search (DFS).py\n")

    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]

    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13

    # build a graph from the given edges
    graph = Graph(edges, n)

    print("Recursive Implementation:", end="\n\t")

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFS_Recu(graph, i, discovered)

    print("\n")
    print("Iterative Implementation:", end="\n\t")

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # Do iterative DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFS_Iter(graph, i, discovered)