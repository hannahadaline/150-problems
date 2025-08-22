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
