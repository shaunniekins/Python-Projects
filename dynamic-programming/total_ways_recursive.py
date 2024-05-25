def count_ways(coins, m):
    if m == 0:
        return 1
    if m < 0 or len(coins) == 0:
        return 0
    
    return count_ways(coins[:-1], m) + count_ways(coins, m - coins[-1])
