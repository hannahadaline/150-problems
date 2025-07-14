
# 14 (1.6)
''' Given two lists a and b, each of which contains unique items,
    return a list of all items that are in only one of the two sets but not both '''

def exclusive_items(a, b):
    result = []
    set_a = set(a)
    set_b = set(b)

    for item in b:
        if item not in set_a:
            result.append(item)

    for item in a:
        if item not in set_b:
            result.append(item)

    return result

def exclusive_items(a, b):
    set_a = set(a)
    set_b = set(b)
    just_a = set_a.difference(set_b)
    just_b = set_b.difference(set_a)

    result = set(just_a)
    result.update(just_b)
    return list(result)

set_a = {4, 2, 1, 6}
set_b = {3, 6, 9, 2, 10}
print(set_a, set_b)
set_c = set(set_a) # how to copy a set
set_c.update(set_b) # how to add all elements from one set into another
print(set_c)


# 15 (1.7)
# Given a list of items, return whether all items in the list are unique

def all_unique(items):
    prev = set()
    for item in items:
        if item in prev:
            return False
        prev.add(item)

    return True

def all_unique(items):
    items_set = set(items)
    return len(items) == len(items_set)
