# Bottom-up approach: start from the smallest subproblem and work our way up to the desired solution
# Time complexity: O(n)

def fib(n):
    memo = {}
    
    for i in range(1, n+1):
        if i <= 2:
            result = 1
        else:
            result = memo[i-1] + memo[i-2]
            
        memo[i] = result
        
    return memo[n]

print(fib(50))
