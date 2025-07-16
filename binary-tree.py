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
