def wordConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = wordConstruct(suffix, wordBank, memo)
            targetWays = [[word] + way for way in suffixWays]
            result.extend(targetWays)
    memo[target] = result
    return result


print(wordConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))