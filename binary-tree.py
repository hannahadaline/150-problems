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
    

            

