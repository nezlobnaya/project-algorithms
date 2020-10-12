"""
Bellman Ford Algorithm in Python
The Bellman–Ford algorithm is an algorithm that computes shortest paths 
from a single source vertex to all of the other vertices in a weighted digraph. 

BF is not ideal for most SSSP(single source shortest path) problems because Dijkstra's algo is much faster
which is O((E +V) log(V))

However Dijkstra's fail when the graph has negative edge weights.
BF becomes really handy to detect negative cycles and determine where they occur.
One particular neat applications is financial arbitrage

"""

class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)

#Time complexity:
#Θ(|V||E|) where |V| is number of vertices and |E| is number of edges. 
# If the graph is complete, the value of |E| becomes Θ(|V|2).
#Space complexity:
# O(V^2) for an adjacency matrix and O(V+E) for an adjacency list.


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)