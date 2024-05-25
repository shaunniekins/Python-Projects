def howSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum and table[i + num] is None:
                    table[i + num] = table[i] + [num]

    return table[targetSum]

print(howSum(7, [5, 3, 4, 7]))