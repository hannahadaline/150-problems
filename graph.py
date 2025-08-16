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




#* 52 (6.2)
''' Given a list of edges of an undirected graph, and two nodes, 
    return whether there exists a path between the two nodes '''

def get_graph(edges):
    graph = {}
    for node_1, node_2 in edges:
        if node_1 in graph:
            graph[node_1].append(node_2)
        else:
            graph[node_1] = [ node_2 ]
        if node_2 in graph:
            graph[node_2].append(node_1)
        else:
            graph[node_2] = [ node_1 ]

    return graph

def _undirected_path(graph, node_A, node_B, visited):
    if node_A == node_B:
        return True 

    for neighbor in graph[node_A]:
        if neighbor not in visited:
            visited.add(neighbor)
            if _undirected_path(graph, neighbor, node_B, visited):
                return True 

    return False 
    
def undirected_path(edges, node_A, node_B):
    graph = get_graph(edges)
    visited = set()
    return _undirected_path(graph, node_A, node_B, visited)



#* 53 (6.3)
''' Given the adjacency list of an undirected graph, 
    return the number of connected components within the graph '''

def connected_components_count(graph):
  count = 0 
  visited = set()

  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1 

  return count 

def explore(graph, node, visited):
    if node in visited:
        return False 

    visited.add(node)

    for neighbor in graph[node]:
        explore(graph, neighbor, visited)

    return True 




#* 54 (6.4)
''' Given the adjacency list of an undirected graph, 
    return the size of the largest connected component within the graph '''

def largest_component(graph):
    visited = set()
    max_size = 0
    for node in graph:
        size = explore(graph, node, visited, 0) 
        if size > max_size:
            max_size = size

    return max_size


def explore(graph, node, visited, size):
    if node in visited:
        return 0

    size = 1
    visited.add(node)

    for neighbor in graph[node]:
        size += explore(graph, neighbor, visited, size)

    return size 

