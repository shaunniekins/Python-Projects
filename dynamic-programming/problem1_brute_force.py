def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            return remainderResult + [num]
    return None



print(howSum(7, [5, 3, 4, 7]))
print(howSum(7, [5,2]))