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




#* 55 (6.5)
''' Given a list of edges for an undirected graph, and two nodes, 
    return the length of the shortest path between the two nodes.  
    If there is no path between the two nodes, return -1 '''

from collections import deque 

def shortest_path(edges, node_A, node_B):
    graph = get_graph(edges)
    visited = set()
    return _shortest_path(graph, node_A, node_B, visited)

def _shortest_path(graph, node_A, node_B, visited):
    queue = deque([ (node_A, 0) ])

    while len(queue) > 0:
        curr_node, curr_dist = queue.popleft()
        if curr_node not in visited:
            visited.add(curr_node)
            if curr_node == node_B:
                return curr_dist 
    
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    queue.append( (neighbor, curr_dist + 1) )

    return -1

def get_graph(edges):
    graph = {}
    for node_1, node_2 in edges:
        if node_1 not in graph:
            graph[node_1] = []
        if node_2 not in graph:
            graph[node_2] = []

        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    return graph 





#* 56 (6.6)
''' Given a grid containing Ws (water) and Ls (land), 
    return the number of islands (vertically or horizontally 
    connected region of land) on the grid '''

def island_count(grid):
    count = 0 
    visited = set()

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if explore(grid, i, j, visited) == True:
                count += 1

    return count 

def explore(grid, i, j, visited):
    if i not in range(0, len(grid)):
        return False 
    if j not in range(0, len(grid[0])):
        return False

    if (i, j) in visited:
        return False 

    if grid[i][j] == 'W':
        return False 

    visited.add( (i, j) )

    explore(grid, i + 1, j, visited)
    explore(grid, i - 1, j, visited)
    explore(grid, i, j + 1, visited)
    explore(grid, i, j - 1, visited)

    return True

    



#* 57 (6.7)
''' Given a grid containing Ws (water) and Ls (land), 
    return the size of the smallest island (vertically or horizontally 
    connected region of land) on the grid '''
    
def minimum_island(grid):
    min_island_size = float('inf')
    visited = set()
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            size = get_size(grid, i, j, visited) 
            if size > 0 and size < min_island_size:
                min_island_size = size

    return min_island_size
            
def get_size(grid, i, j, visited):
    if i not in range(0, len(grid)):
        return 0
    if j not in range(0, len(grid[0])):
        return 0

    if grid[i][j] == 'W':
        return 0

    if (i, j) in visited:
        return 0

    visited.add( (i, j) )

    size = 1 
    size += get_size(grid, i + 1, j, visited)
    size += get_size(grid, i - 1, j, visited)
    size += get_size(grid, i, j + 1, visited)
    size += get_size(grid, i, j - 1, visited)

    return size
        



#* 58 (6.8)
''' Given a grid containing Xs (walls, cannot pass through) 
    and Os (open spaces) and Cs (carrots), 
    return the distance from the starting position to the closest carrot '''

from collections import deque 

def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    return explore(grid, starting_row, starting_col, visited)


def explore(grid, starting_row, starting_col, visited):
    queue = deque([ ((starting_row, starting_col), 0) ])

    while len(queue) > 0:
        (r, c), dist = queue.popleft()
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] != 'X':
            visited.add( (r, c) )
            if grid[r][c] == 'C':
                return dist 

            neighbors = [ (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1) ]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append( (neighbor, dist + 1) )

    return -1
            




#* 59 (6.9)
''' Given a directed acyclic graph's adjacency list, 
    return the length of the longest path within the graph '''

def longest_path(graph):
    distances = {}
    for node in graph:
        if len(graph[node]) == 0:
            distances[node] = 0 

    for node in graph:
        traverse(graph, node, distances)

    return max(distances.values())

def traverse(graph, node, distances):
    if node in distances:
        return distances[node]

    max_path_len = 0 
    for neighbor in graph[node]:
        path_len = traverse(graph, neighbor, distances)
        if path_len > max_path_len:
            max_path_len = path_len 

    distances[node] = max_path_len + 1 
    return distances[node]
    




#* 60 (6.10)
''' Given a number of courses and a list of prerequisites, 
    return the minimum number of semesters required to complete all courses.  
    Courses have ids ranging from 0 to n - 1, where n is the number of courses.  
    There is no limit on how many courses you can take in a semester. '''

def semesters_required(num_courses, prereqs):
    graph = make_graph(num_courses, prereqs)

    distances = {}
    for node in graph:
        if len(graph[node]) == 0:
            distances[node] = 0 

    for node in graph:
        traverse(graph, node, distances)

    return max(distances.values()) + 1

def traverse(graph, node, distances):
    if node in distances:
        return distances[node]

    max_path_len = 0 
    for neighbor in graph[node]:
        path_len = traverse(graph, neighbor, distances)
        if path_len > max_path_len:
            max_path_len = path_len 

    distances[node] = max_path_len + 1 
    return distances[node]

def make_graph(num_courses, prereqs):
    graph = {}
    for i in range(num_courses):
        graph[i] = []

    for course_1, course_2 in prereqs:
        graph[course_1].append(course_2)

    return graph 
    



#* 61 (6.11)
''' Given a grid containing Ws (water) and Ls (land), 
    where there are two islands (vertically or horizontally 
    connected region of land) on the grid,
    return the minimum length bridge needed to connect the two islands '''

# the trick here is to bfs from the set of positions in the first island as a group
# if you bfs from each position individually and then find the minimum from there,
# you're not taking into account that joining the positions together minimizes your bridge

from collections import deque 

def best_bridge(grid):
    first_island = get_first_island(grid)

    queue = deque([])
    for (r, c) in first_island:
        queue.append(((r, c), 0))

    visited = first_island.copy()
    
    while len(queue) > 0:
        (r, c), dist = queue.popleft()

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
    
            if grid[r][c] == 'L' and (r, c) not in visited:
                return dist - 1
    
            neighbors = [ (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1) ]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append( (neighbor, dist + 1) )


def get_first_island(grid):
    island_1_i = None 
    island_1_j = None 
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 'L':
                island_1_i = i 
                island_1_j = j
                break

    visited = set()
    explore(grid, island_1_i, island_1_j, visited)
    return visited



def explore(grid, i, j, visited):
    if i not in range(0, len(grid)):
        return 
    if j not in range(0, len(grid[0])):
        return 

    if (i, j) in visited:
        return 

    if grid[i][j] == 'W':
        return

    visited.add( (i, j) )

    explore(grid, i + 1, j, visited)
    explore(grid, i - 1, j, visited)
    explore(grid, i, j + 1, visited)
    explore(grid, i, j - 1, visited)

    return 
    



#* 62 (6.12)
''' Given an adjacency list for a directed graph, 
    return whether there are any cycles in the graph '''

# note that if any neighbor finds a cycle then 
# you have to return True right away, because you found a cycle too
def has_cycle(graph):
    visited = set()
    visiting = set()
    for node in graph:
        if explore(graph, node, visited, visiting) == True:
            return True 

    return False 

def explore(graph, node, visited, visiting):
    if node in visiting:
        return True

    if node in visited:
        return False 

    visiting.add(node)

    for neighbor in graph[node]:
        if explore(graph, neighbor, visited, visiting) == True:
            return True 

    visiting.remove(node)
    visited.add(node)

    return False 



#* 63 (6.13)
''' Given a number of courses and a list of prerequisites, 
    return whether it is possible to complete all courses.  
    Courses have ids ranging from 0 to n - 1, where n is the number of courses.  
    There is no limit on how many courses you can take in a semester. '''

def prereqs_possible(num_courses, prereqs):
    graph = make_graph(num_courses, prereqs)
    return not has_cycle(graph)

def has_cycle(graph):
    visiting = set()
    visited = set()
    for node in graph:
        if find_cycle(graph, node, visited, visiting):
            return True 
    return False

def find_cycle(graph, node, visited, visiting):
    if node in visited:
        return False 
    if node in visiting:
        return True 

    visiting.add(node)
    for neighbor in graph[node]:
        if find_cycle(graph, neighbor, visited, visiting) == True:
            return True 

    visiting.remove(node)
    visited.add(node)

    return False 
    
def make_graph(num_courses, prereqs):
    graph = {}
    for course in range(num_courses):
        graph[course] = []

    for course_1, course_2 in prereqs:
        graph[course_1].append(course_2)

    return graph 
    
