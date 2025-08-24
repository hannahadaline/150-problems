#* 64 (7.1)
''' Given a number n, return the nth Fibonacci number, 
    where the 0th number is 0 and the 1st number is 1. '''

def fib(n):
    memo = {}
    return _fib(n, memo)

def _fib(n, memo):
    if n == 0 or n == 1:
        return n 

    if n in memo:
        return memo[n]

    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]




#* 65 (7.2)
''' Given a number n, return the nth Tribonacci number, 
    where the 0th number is 0 and the 1st number is 0 
    and the 2nd number is 1. '''

def tribonacci(n):
    memo = {}
    return _tribonacci(n, memo)

def _tribonacci(n, memo):
    if n == 0 or n == 1:
        return 0 
    if n == 2:
        return 1 

    if n in memo:
        return memo[n]

    memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)

    return memo[n]




#* 66 (7.3)
''' Given a non-negative number and a list of positive numbers, 
    return whether it is possible to form the number by summing numbers 
    in the list as many times as needed. '''

def sum_possible(amount, numbers):
    memo = {}
    return _sum_possible(amount, numbers, memo)
    
def _sum_possible(amount, numbers, memo):
    if amount == 0:
        return True 

    if amount < 0:
        return False 

    if amount in memo:
        return memo[amount]

    for number in numbers:
        if _sum_possible(amount - number, numbers, memo):
            memo[amount] = True 
            return True 

    memo[amount] = False 
    return False 



#* 67 (7.4)
''' Given an amount and a list of coins, 
    return the minimum number of coins needed to sum to the amount.
    Coins may be used as many times as needed.
    If it is not possible, return -1 '''

def min_change(amount, coins):
    memo = {}
    return _min_change(amount, coins, memo)

def _min_change(amount, coins, memo):
    if amount == 0:
        return 0

    if amount < 0:
        return -1

    if amount in memo:
        return memo[amount]

    min_coins_needed = float('inf')
    for coin in coins:
        coins_needed = _min_change(amount - coin, coins, memo)
        if coins_needed > -1 and coins_needed < min_coins_needed:
            min_coins_needed = coins_needed + 1

    if min_coins_needed == float('inf'):
        memo[amount] = -1 
        return -1 
    memo[amount] = min_coins_needed 
    return min_coins_needed 





#* 68 (7.5)
''' Given a grid of Xs and Os where Xs are walls and Os are open spaces, 
    return the number of ways to get from the top left corner to the bottom right corner.  
    You can only move down or to the right and cannot move through walls. '''

def count_paths(grid):
    start_row = 0 
    start_col = 0
    memo = {}
    return _count_paths(grid, start_row, start_col, memo)

def _count_paths(grid, start_row, start_col, memo):
    if not 0 <= start_row < len(grid) or not 0 <= start_col < len(grid[0]):
        return 0

    if grid[start_row][start_col] == 'X':
        return 0

    if start_row == len(grid) - 1 and start_col == len(grid[0]) - 1:
        return 1 

    pos = (start_row, start_col)
    if pos in memo:
        return memo[pos]
        
    south_neighbor_paths = _count_paths(grid, start_row + 1, start_col, memo)
    east_neighbor_paths = _count_paths(grid, start_row, start_col + 1, memo)

    memo[pos] = south_neighbor_paths + east_neighbor_paths
    return memo[pos]





#* 69 (7.6)
''' Given a grid of non-negative integers, 
    return the max sum that can be attained by traveling 
    from the top left position to the bottom right position, 
    only moving down or right. '''

def max_path_sum(grid):
    end_row = len(grid) - 1
    end_col = len(grid[0]) - 1
    memo = {}
    return _max_path_sum(grid, end_row, end_col, memo)

def _max_path_sum(grid, end_row, end_col, memo):
    if end_row == 0 and end_col == 0:
        return grid[end_row][end_col]

    if not 0 <= end_row < len(grid) or not 0 <= end_col < len(grid[0]):
        return 0

    pos = (end_row, end_col)
    if pos in memo:
        return memo[pos]

    north_neighbor_paths = _max_path_sum(grid, end_row - 1, end_col, memo)
    west_neighbor_paths = _max_path_sum(grid, end_row, end_col - 1, memo)

    memo[pos] = max(north_neighbor_paths, west_neighbor_paths) + grid[end_row][end_col]
    return memo[pos]
    



#* 70 (7.7)
''' Given a list of numbers, 
    return the maximum sum of non-adjacent items in the list. '''

def non_adjacent_sum(nums):
    i = len(nums) - 1
    memo = {}
    return _non_adjacent_sum(nums, i, memo)

def _non_adjacent_sum(nums, i, memo):
    if i == 0:
        return nums[i]

    if i < 0:
        return 0 

    if i in memo:
        return memo[i]

    memo[i] = max(_non_adjacent_sum(nums, i - 1, memo), _non_adjacent_sum(nums, i - 2, memo) + nums[i])
    return memo[i]




#* 71 (7.8)
''' Given a number, 
    return the minimum number of (non-zero) perfect squares that sum to the number. '''

from math import floor, sqrt

def summing_squares(n):
    squares = [ i ** 2 for i in range(1, floor(sqrt(n)) + 1) ]
    memo = {}
    return _summing_squares(n, squares, memo)

def _summing_squares(n, squares, memo):
    if n == 0:
        return 0

    if n < 0:
        return float('inf')

    if n in memo:
        return memo[n]

    min_squares_needed = float('inf')
    for square in squares:
        squares_needed = _summing_squares(n - square, squares, memo)
        if squares_needed < min_squares_needed:
            min_squares_needed = squares_needed + 1

    memo[n] = min_squares_needed
    return memo[n]
    




#* 72 (7.9)
''' Given an amount and a list of coin values, 
    return the number of ways to sum to the amount using the coins.
    You can use each coin as much as you need. '''

# both the amount and i changes 
# you have to remove duplicates so count how many of each coin 

def counting_change(amount, coins):
    i = 0
    memo = {}
    return _counting_change(amount, coins, i, memo)

def _counting_change(amount, coins, i, memo):  
    if amount == 0:
        return 1

    if amount < 0:
        return 0 

    if i == len(coins):
        return 0

    key = (amount, i)
    if key in memo:
        return memo[key]

    total_ways = 0 
    coin = coins[i]
    for j in range(0, amount // coin + 1):
        num_ways = _counting_change(amount - coin * j, coins, i + 1, memo)
        total_ways += num_ways 

    memo[key] = total_ways
    return memo[key]




#* 73 (7.10)
''' Given a list of numbers, 
    return whether it is possible to reach the last position of the list.  
    You start at the first position and at any position 
    you can take a max number of steps to the right, given by the number at the position. '''

def array_stepper(numbers):
    i = 0 
    memo = {}
    return _array_stepper(numbers, i, memo)

def _array_stepper(numbers, i, memo):
    if i >= len(numbers):
        return False 

    if i == len(numbers) - 1:
        return True 

    if i in memo:
        return memo[i]

    max_steps = numbers[i]
    for j in range(1, max_steps + 1):
        if _array_stepper(numbers, i + j, memo):
            memo[i] = True
            return True 

    memo[i] = False 
    return False 




#* 74 (7.11)
''' Given a string, return the length of the longest subsequence 
    of the string that is also a palindrome. '''

def max_palin_subsequence(string):
    i = 0 
    j = len(string) - 1
    memo = {}
    return _max_palin_subsequence(string, i, j, memo)

def _max_palin_subsequence(string, i, j, memo):
    if i == j:
        return 1
        
    if i > j:
        return 0

    key = (i, j)
    if key in memo:
        return memo[key]

    if string[i] == string[j]:
        memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
        return memo[key]

    memo[key] = max(_max_palin_subsequence(string, i + 1, j, memo), _max_palin_subsequence(string, i, j - 1, memo))
    return memo[key]




#* 75 (7.12)
''' Given two strings, return the length of the longest overlapping subsequence.  
    A subsequence is created by deleting any characters while 
    maintaining the relative order of characters. '''

def overlap_subsequence(string_1, string_2):
    i_1 = 0
    i_2 = 0 
    memo = {}
    return _overlap_subsequence(string_1, string_2, i_1, i_2, memo)
    
def _overlap_subsequence(string_1, string_2, i_1, i_2, memo):
    if i_1 == len(string_1) or i_2 == len(string_2):
        return 0

    key = (i_1, i_2) 
    if key in memo:
        return memo[key]
        
    if string_1[i_1] == string_2[i_2]:
        memo[key] = 1 + _overlap_subsequence(string_1, string_2, i_1 + 1, i_2 + 1, memo)
        return memo[key]

    memo[key] = max(
        _overlap_subsequence(string_1, string_2, i_1 + 1, i_2, memo),
        _overlap_subsequence(string_1, string_2, i_1, i_2 + 1, memo)
    )
    return memo[key]





#* 76 (7.13)
''' Given a string and a list of words, 
    return whether it is possible to concatenate words in the list 
    together to form the string.  
    You can use each word as many times as needed. '''

def can_concat(s, words):
    i = 0 
    memo = {}
    return _can_concat(s, words, i, memo)
    
    
def _can_concat(s, words, i, memo):
    if i == len(s):
        return True 

    if i in memo:
        return memo[i]
        
    for word in words:
        if s.startswith(word, i):
            if _can_concat(s, words, i + len(word), memo) == True:
                memo[i] = True
                return True

    memo[i] = False 
    return False 






#* 77 (7.14)
''' Given a string and a list of words, 
    return the minimum number of words needed to 
    concatenate words in the list together to form the string.  
    You can use each word as many times as needed. 
    If it is not possible, return -1. '''

def quickest_concat(s, words):
    i = 0 
    memo = {}
    return _quickest_concat(s, words, i, memo)

def _quickest_concat(s, words, i, memo):
    if i == len(s):
        return 0 

    if i in memo:
        return memo[i]

    min_words = float('inf')
    for word in words:
        if s.startswith(word, i):
            num_words = _quickest_concat(s, words, i + len(word), memo) 
            if num_words != -1 and num_words < min_words:
                min_words = num_words 

    if min_words == float('inf'):
        memo[i] = -1 
        return memo[i] 
    memo[i] = min_words + 1
    return memo[i]
