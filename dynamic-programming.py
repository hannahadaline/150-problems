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
