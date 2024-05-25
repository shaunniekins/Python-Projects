def wordConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in wordBank:
            if target[i:i+len(word)] == word:
                newCombinations = [combination + [word] for combination in table[i]]
                table[i+len(word)].extend(newCombinations)

    return table[len(target)]


print(wordConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))