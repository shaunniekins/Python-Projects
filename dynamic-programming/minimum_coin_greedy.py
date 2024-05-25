def minimum_coins(coins, target):
    coins.sort(reverse=True)
    min_coins = 0

    for coin in coins:
        num_coins = target // coin

        target -= num_coins * coin
        min_coins += num_coins

    if target != 0:
        return -1

    return min_coins

coins = [1, 4, 5]
target_sum = 13
print(minimum_coins(coins, target_sum))
