def ShortestSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum in numbers: return [targetSum]
    if min(numbers) > targetSum: return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = ShortestSum(remainder, numbers, memo)

        if remainderCombination is not None:
            combination = remainderCombination + [num]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination

print(ShortestSum(7, [5, 3, 4, 7]))
