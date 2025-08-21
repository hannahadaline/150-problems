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

