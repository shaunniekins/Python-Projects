def ShortestSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for amount in range(targetSum + 1):
        if table[amount] is not None:
            for num in numbers:
                if amount + num <= targetSum:
                    combination = table[amount] + [num]
                    if table[amount + num] is None or len(combination) < len(table[amount + num]):
                        table[amount + num] = combination

    return table[targetSum]


print(ShortestSum(7, [5, 3, 4, 7]))

