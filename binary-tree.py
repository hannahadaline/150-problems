#* 32 (4.1)
''' Given the root of a binary tree,
  Return a list of its values in depth search order ''' 

# RECURSIVE 
def depth_first_values(root):
    if root is None:
        return []
    return [ root.val, *depth_first_values(root.left), *depth_first_values(root.right) ]

# ITERATIVE 
def depth_first_values(root):
    values = []
    if root is None:
        return values

    stack = [ root ]
    while len(stack) > 0:
        curr = stack.pop()
        values.append(curr.val)
        
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return values 



#* 33 (4.2) 
''' Given a root of a binary tree,
  Return a list of values in breadth first order '''

from collections import deque 

def breadth_first_values(root):
    if root is None:
        return []
        
    values = []
    queue = deque([ root ])

    while len(queue) > 0:
        curr = queue.popleft()
        values.append(curr.val)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return values
    



#* 34 (4.3) 
''' Given the root of a tree, return the sum of all values in the tree '''

# RECURSIVE
def tree_sum(root):
    if root is None:
        return 0 

    return tree_sum(root.left) + root.val + tree_sum(root.right)

# BREADTH FIRST
from collections import deque 

def tree_sum(root):
    if root is None:
        return 0 

    sum = 0
    queue = deque([ root ])

    while len(queue) > 0:
        curr = queue.popleft()
        sum += curr.val 

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return sum

# DEPTH FIRST
def tree_sum(root):
    if root is None:
        return 0 

    stack = [ root ]
    sum = 0

    while len(stack) > 0:
        curr = stack.pop()
        sum += curr.val

        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)

    return sum




#*35 (4.4)
''' Given the root of a tree and a target value, 
    return whether the target value is found in the tree '''

def tree_includes(root, target):
    if root is None:
        return False
        
    if root.val == target:
        return True 

    return tree_includes(root.left, target) or tree_includes(root.right, target)




#* 36 (4.5)
''' Given the root of a tree,
    return the min value in the tree '''

def tree_min_value(root):
    left_min_value = float("inf") if root.left is None else tree_min_value(root.left)
    right_min_value = float("inf") if root.right is None else tree_min_value(root.right)

    return min(left_min_value, root.val, right_min_value)




#* 37 (4.6)
''' Given the root of a binary tree of numbers,
  return the max root to leaf path sum '''

def max_path_sum(root):
    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val 

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))




#* 38 (4.7)
''' Given the root of a binary tree and a target value,
    return a list of values indicating the path starting from the root to the value 
    return None if the value is not found '''

def path_finder(root, target):
    if _path_finder(root, target) is not None:
        return _path_finder(root, target)[::-1]
    return None
    
def _path_finder(root, target):
    if root is None:
        return None 
        
    if root.val == target:
        return [ target ]

    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path 

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path 

    return None
    

            
#* 39 (4.8)
''' Given a root of a binary tree and a target value,
    return the number of times the target value appears in the tree '''

def tree_value_count(root, target):
    if root is None:
        return 0 

    root_count = 1 if root.val == target else 0
    return tree_value_count(root.left, target) + root_count + tree_value_count(root.right, target)




##* 40 (4.9)
''' Given the root of a binary tree, return its height '''

def how_high(root):
    if root is None:
        return -1 

    return 1 + max(how_high(root.left), how_high(root.right))




#* 41 (4.10)
''' Given the root of a binary tree, return the rightmost value in the bottommost level '''

from collections import deque

def bottom_right_value(root):
    values = []
    if root is None:
        return values

    queue = deque([ root ])

    while len(queue) > 0:
        curr = queue.popleft()
        values.append(curr.val)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return values[-1]





#* 42 (4.11)
''' Given the root of a binary tree,
    return a list of all root-to-leaf paths in the tree ''' 

def all_tree_paths(root):
    all_paths = _all_tree_paths(root)
    for path in all_paths:
        path.reverse()

    return all_paths
    
def _all_tree_paths(root):
    if root is None:
        return [ ]

    if root.left is None and root.right is None:
        return [ [ root.val ] ]
        
    all_left_tree_paths = [ path + [ root.val ] for path in _all_tree_paths(root.left) ] 
    all_right_tree_paths = [ path + [ root.val ] for path in _all_tree_paths(root.right) ] 

    return [ *all_left_tree_paths, *all_right_tree_paths ]



    
    
#* 43 (4.12)
''' Given the root of a binary tree,
    return a 2-d list of lists where each sublist 
    contains the values in a given level of the tree '''

# ITERATIVE (breadth first)

from collections import deque 

def tree_levels(root):
    if root is None:
        return [ ]

    queue = deque([ (root, 0) ])
    levels = [ ]

    while len(queue) > 0:
        curr_node, curr_level = queue.popleft()

        if curr_level == len(levels):
            levels.append([ curr_node.val ])
        else:
            levels[curr_level].append(curr_node.val)

        if curr_node.left is not None:
            queue.append((curr_node.left, curr_level + 1))
        if curr_node.right is not None:
            queue.append((curr_node.right, curr_level + 1))

    return levels

# RECURSIVE

def fill_levels(root, levels, level):
    if root is None:
        return 

    if len(levels) == level:
        levels.append([ root.val ])
    else:
        levels[level].append(root.val)

    fill_levels(root.left, levels, level + 1)
    fill_levels(root.right, levels, level + 1) # have to go left to right within each level
