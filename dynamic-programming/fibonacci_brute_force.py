# Brute force: Recursion
# Time complexity: O(2^n)

def fib(n):
    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

print(fib(3))