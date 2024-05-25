def wordConstruct(target, wordBank):
    if target == '':
        return [[]]
    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = wordConstruct(suffix, wordBank)
            targetWays = [[word] + way for way in suffixWays]
            result.extend(targetWays)
    return result

print(wordConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))