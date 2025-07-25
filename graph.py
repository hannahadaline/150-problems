#* 51 (6.1)
''' Given a dictionary representing the adjacency list of a directed acyclic graph, 
  and two nodes src and dst within that graph, 
  return whether there exists a path between src and dst '''

# RECURSIVE DEPTH FIRST 
def has_path(graph, src, dst):
    if src == dst:
        return True 

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True 

    return False 


# ITERATIVE BREADTH FIRST 
from collections import deque 

def has_path(graph, src, dst):
    queue = deque([ src ])
    while len(queue) > 0:
        curr = queue.popleft()
        if curr == dst:
            return True 
        for node in graph[curr]:
            queue.append(node)
    return False 
