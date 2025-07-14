#* 7 (1.1)
''' Given two strings, return whether the two strings are anagrams
(containing the same characters but in a different order '''

def anagrams(s1, s2):
   counts_1 = {}
   for char in s1:
      if char in counts_1:
         counts_1[char] += 1
      else:
         counts_1[char] = 1

   counts_2 = {}
   for char in s2:
      if char in counts_2:
         counts_2[char] += 1
      else:
         counts_2[char] = 1

   return counts_1 == counts_2
         
def anagrams(s1, s2):
   counts = {}
   for char in s1:
      if char in counts:
         counts[char] += 1
      else:
         counts[char] = 1

   for char in s2:
      if char in counts:
         counts[char] -= 1
      else:
         return False

   for char in counts:
      if counts[char] != 0:
         return False
   return True



#* 8 (1.2)
''' Given a string, return most frequent char in the string
    If there are ties, return first char to occur '''

# using >= (the equals part) and then reversing the string 
# gives the first occurrence in one pass 

def most_frequent_char(s):
    freqs = {}
    max_freq = 0
    max_char = ""
   
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        freqs[char] = freqs.get(char, 0) + 1

        if freqs[char] >= max_freq:
            max_freq = freqs[char]
            max_char = char

    return max_char


#* 9 (1.3)
''' Given a list of integers and a target sum, 
    return a tuple (in any order) of the two indices whose values sum to the target
    There is guaranteed to be one solution '''

def pair_sum(numbers, target_sum):
    prev = {}
    for i, num in enumerate(numbers):
        complement = target_sum - num
        if complement in prev:
            return (prev[complement], i)
        else:
            prev[num] = i


#* 10 (1.4)
''' Given a list of integers and a target product, 
    return a tuple (in any order) of the two indices whose values multiply to the target
    There is guaranteed to be one solution '''

def pair_product(numbers, target_product):
    prev_nums = {}
    for i, num in enumerate(numbers):
        complement = target_product / num
        if complement in prev_nums:
            return (prev_nums[complement], i)

        prev_nums[num] = i


#* 11 (1.5) 
''' Given two input lists, each without duplicates,
    return a list containing elements in both lists '''

def intersection(a, b):
    a_set = set(a)
    result = [ element for element in b if element in a_set ]
    
    # for element in b:
    #     if element in a_set:
    #         result.append(element)

    return result



#* 12 (1.6)
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



#* 13 (1.7)
''' Given a list of items, return whether all items in the list are unique '''

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


#* 14 (1.8)
''' Given two lists of items, 
    return list of elements common to both lists, 
    as many times as they occur in both lists '''

from collections import Counter 

def intersection_with_dupes(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)

    common_dict = {}
    for char in a_dict:
        if char in b_dict:
            common_dict[char] = min(a_dict[char], b_dict[char])

    result = []
    for char in common_dict:
        result.extend([ char for i in range(common_dict[char]) ])

    return result

# a.extend(b) adds the list b to list a

# this gets rid of the extra space needed to create a new dictionary
def intersection_with_dupes(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)

    result = []

    for char in a_dict:
        num_common_occurrences = min(a_dict[char], b_dict[char])
        result.extend([ char for i in range(num_common_occurrences) ])

    return result
