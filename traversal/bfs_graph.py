# Using a Python dictionary to act as an adjacency list
'''The illustrated graph is represented using 
an adjacency list - an easy way to do it in Python 
is to use a dictionary data structure.
Each vertex has a list of its adjacent nodes stored.'''

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')

"""

Time Complexity

Since all of ​the nodes and vertices are visited, 
the time complexity for BFS on a graph is O(V+E); 


"""