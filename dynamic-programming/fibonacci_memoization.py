# Memoization: storing the results of expensive function calls and returning the cached result when the same inputs occur again
# Dynamic programming = Recursion + Memoization
# Time Complexity: O(n)

memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
        
    memo[n] = result
    return result

print(fib(50))