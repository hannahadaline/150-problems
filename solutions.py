#* 1 (0.1)
''' Given a string s, return a greeting "Hey s". '''

def greet(s):
    return "hey " + s
   



#* 2 (0.2)
''' Given a non-empty list of numbers, return the largest number in the list '''

def max_value(nums):
    max_val = float("-inf")
  
    for num in nums:
        if num > max_val:
            max_val = num

    return max_val



#* 3 (0.3)
''' Given a sentence string, return the longest word in the sentence. 
   If there are ties, return the later word '''

def longest_word(sentence):
    words = sentence.split(" ")
    words.reverse()
    longest_length = float("-inf")
    longest_word = ""

    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word

    return longest_word




#* 4 (0.4) 
''' Given a positive integer, return whether it is prime ''' 
def longest_word(sentence):
    words = sentence.split(" ")
    words.reverse()
    longest_length = float("-inf")
    longest_word = ""

    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word

    return longest_word




#* 5 (0.5)
''' Given a positive integer n, 
    Return a list of numbers from 1 to n making the following replacements:
    - if the number is divisible by 3, make the element "fizz"
    - if the number is divisible by 5, make the element "buzz"
    - if the number is divisible by 3 and 5, make the element "fizzbuzz" '''

def fizz_buzz(n):
    result = []
   
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)

    return result




#* 6 (0.6)
''' Given a list of unique elements,
    Return a list of all unique pairs of elements in any order.
    The order within each pair does not matter. '''

def pairs(elements):
    pairs = []
   
    for i in range(0, len(elements)):
        for j in range(i + 1, len(elements)):
            pairs.append([elements[i], elements[j]])
         
    return pairs
      



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


#* 15 (2.1)
''' Given a list of numbers, compute its sum recursively '''

def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])



#* 16 (2.2)
''' Given a number, compute its factorial recursively '''

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

# This is O(n) time and O(n) space



#* 17 (2.3)
''' Given a list of strings, compute the sum of lengths of strings recursively '''

def sum_of_lengths(strings):
    if len(strings) == 0:
        return 0

    return len(strings[0]) + sum_of_lengths(strings[1:])



#* 18 (2.4) 
''' Given a string, reverse it recursively '''

def reverse_string(s):
    if len(s) == 0:
        return ""

    return s[-1] + reverse_string(s[:-1])



#* 19 (2.5)
''' Given a string, check if it is a palindrome recursively '''

def palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True 

    return s[0] == s[-1] and palindrome(s[1:-1])

# this is easy to read and intuitive, but not the most efficient:
# returning False if the outer chars are not equal prevents you from doing more searching inward

# time and space are O(n^2) for all these recursive string problems

def palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True 

    if s[0] != s[-1]:
        return False
        
    return palindrome(s[1:-1])


#* 20 (2.6)
''' Given a nonnegative integer n, compute the nth Fibonacci number recursively '''
   
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

# note: time is O(2^n), space is O(n) (height of recursion tree)




#* 21 (3.1)
''' Given the head of a linked list, 
    return a list of all the node values in the linked list '''

# ITERATIVE
def linked_list_values(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next 

    return values

# RECURSIVE
def linked_list_values(head):
    values = []
    fill_values(head, values)
    return values

def fill_values(head, values):
    if head is None:
        return

    values.append(head.val)
    fill_values(head.next, values)


#* 22 (3.2)
''' Given the head of a linked list of numbers,
    Return the sum of all the numbers in the linked list '''

# ITERATIVE 
def sum_list(head):
    sum = 0
    curr = head

    while curr is not None:
        sum += curr.val 
        curr = curr.next 

    return sum


# RECURSIVE
def sum_list(head):
    sum = [0]
    _sum_list(head, sum)
    return sum [0]

def _sum_list(head, sum):
    if head is None:
        return sum[0]

    sum[0] += head.val 
    _sum_list(head.next, sum)

# The reason we need to use [0] instead of 0 is because an int is not mutable but a list is

# RECURSIVE, ELEGANT
def sum_list(head):
    if head is None:
        return 0 

    return head.val + sum_list(head.next)




#* 23 
''' Given the head of a linked list and a target,
    Return whether the linked list contains the target '''

# ITERATIVE
def linked_list_find(head, target):
    curr = head
    while curr is not None:
        if curr.val == target:
            return True 
        curr = curr.next

    return False 

# RECURSIVE 
def linked_list_find(head, target):
    if head is None:
        return False 

    if head.val == target:
        return True 

    return linked_list_find(head.next, target)




#* 24 (3.4)
''' Given a head of a linked list and an index,
    Return the value of the node at the index
    If there is no node at the index, return None '''

# ITERATIVE
def get_node_value(head, index):
    curr_index = 0
    curr_node = head 

    while curr_node is not None:
        if curr_index == index:
            return curr_node.val 

        curr_index += 1
        curr_node = curr_node.next

    return None

# RECURSIVE
def get_node_value(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val 

    return get_node_value(head.next, index - 1)



#* 25 (3.5)
''' Given the head of a linked list, reverse the linked list and return the new head '''

# ITERATIVE 
def reverse_list(head):
    if head is None:
        return None 
    if head.next is None:
        return head 
        
    curr = head 
    prev = None 
    while curr is not None:
        next = curr.next # make sure to set this before
        curr.next = prev 
        prev = curr 
        curr = next 

    return prev 

# None <- a   b -> c -> d -> e -> f
#       prev curr   


# RECURSIVE

def reverse_list(head):
    prev = None 
    return _reverse_list(head, prev)

def _reverse_list(head, prev):
    if head is None:
        return prev # we get this from the last step of the iterative 
        
    next = head.next 
    head.next = prev 

    return _reverse_list(next, head)




#*26 (3.6)
''' Given the heads of two linked lists,
    Zipper the nodes in alternating order (starting with the first head) 
    and return the head of the resulting linked list
    If one list is longer than the other, end with its extra nodes '''

# RECURSIVE
def zipper_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None 

    elif head_1 is None:
        return head_2

    elif head_2 is None:
        return head_1

    next_1 = head_1.next 
    next_2 = head_2.next 

    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)

    return head_1

# ITERATIVE
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
    placeholder_head = Node("None")
    tail = placeholder_head 
    curr_1 = head_1 
    curr_2 = head_2 

    while curr_1 is not None and curr_2 is not None:
        next_1 = curr_1.next 
        next_2 = curr_2.next 
        
        tail.next = curr_1 
        curr_1.next = curr_2 
        tail = curr_2 
        
        curr_1 = next_1 
        curr_2 = next_2 

    if curr_1 is None:
        tail.next = curr_2 

    if curr_2 is None:
        tail.next = curr_1 

    return placeholder_head.next 



#* 27 (3.7)
''' Given two heads of two sorted linked lists in increasing order,
    Merge the lists into a single sorted list and return its head '''

# ITERATIVE
def merge_lists(head_1, head_2):
    placeholder_head = Node("None")
    tail = placeholder_head 
    curr_1 = head_1 
    curr_2 = head_2 

    while curr_1 is not None and curr_2 is not None:
        if curr_1.val < curr_2.val:
            tail.next = curr_1 
            curr_1 = curr_1.next 
        else:
            tail.next = curr_2 
            curr_2 = curr_2.next 
        tail = tail.next

    if curr_1 is None:
        tail.next = curr_2 
    if curr_2 is None:
        tail.next = curr_1 
        
    return placeholder_head.next 

# RECURSIVE
def merge_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None 

    if head_1 is None:
        return head_2

    if head_2 is None:
        return head_1 

    next_1 = head_1.next 
    next_2 = head_2.next

    if head_1.val > head_2.val:
        head_2.next = merge_lists(head_1, next_2)
        return head_2

    else: 
        head_1.next = merge_lists(next_1, head_2)
        return head_1 



#* 28 (3.8)
''' Given the head of a linked list, 
    return whether the linked list contains only one unique value '''

# ITERATIVE
def is_univalue_list(head):
    val = head.val 
    curr = head 
    
    while curr is not None:
        if curr.val != val:
            return False 
        curr = curr.next
        
    return True 


# RECURSIVE
def is_univalue_list(head):
    if head.next is None:
        return True 

    return head.val == head.next.val and is_univalue_list(head.next)

# This is more efficient
def is_univalue_list(head):
    if head.next is None:
        return True 

    if head.val != head.next.val:
        return False 

    return is_univalue_list(head.next)




#* 29 (3.9)
''' Given the head of a linked list, 
    return length of longest consecutive streak of the same value in the list '''

def longest_streak(head):
    prev = None 
    curr = head 
    len_longest_streak = 0
    len_current_streak = 0

    while curr is not None:
        if prev is not None and prev.val == curr.val:
            len_current_streak += 1
        else:
            len_current_streak = 1

        if len_current_streak > len_longest_streak:
            len_longest_streak = len_current_streak

        prev = curr 
        curr = curr.next 

    return len_longest_streak




#* 30 (3.10)
''' Given a head of a linked list and an index,
    Remove the node at that index and return the head of the resulting linked list '''

# ITERATIVE
def remove_node(head, target_val):
    prev = None
    curr = head

    if head.val == target_val:
        return head.next 

    while curr is not None:
        if curr.val == target_val:
            next = curr.next 
            prev.next = next 
            curr.next = None 
            return head 
        prev = curr 
        curr = curr.next 

# RECURSIVE
def remove_node(head, target_val):
    if head is None:
        return None 

    if head.val == target_val:
        return head.next 

    head.next = remove_node(head.next, target_val)
    return head




#* 31 (3.11)
''' Given the head of a linked list and an index 
    (no bigger than the length of the linked list),
    Insert the node at the index and return the head of the resulting linked list ''' 

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# ITERATIVE 
def insert_node(head, value, index):
    new_node = Node(value)

    if index == 0:
        new_node.next = head 
        return new_node 

    curr_index = 0
    curr_node = head 
    prev_node = None

    while curr_node is not None:
        if curr_index == index:
            prev_node.next = new_node 
            new_node.next = curr_node 
            return head 
            
        prev_node = curr_node 
        curr_node = curr_node.next 
        curr_index += 1

    prev_node.next = new_node 
    return head 


# RECURSIVE

def insert_node(head, value, index):
    if index == 0:
        new_node = Node(value)
        new_node.next = head 
        return new_node 

    head.next = insert_node(head.next, value, index - 1)
    return head 
            
