from collections import defaultdict
import heapq
"""

The problem is that they want to efficiently transfer a piece of information 
to anyone and everyone who may be listening. This is important in gaming so that 
all the players know the very latest position of every other player. 
This is important for Internet radio so that all the listeners that are tuned in 
are getting all the data they need to reconstruct the song they are listening to. 
from collections import defaultdict
import heapq

"""

def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

print(dict(create_spanning_tree(example_graph, 'A')))

# {'A': set(['B']),
#  'B': set(['C', 'D']),
#  'D': set(['E']),
#  'E': set(['F']),
#  'F': set(['G'])}
