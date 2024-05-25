from random import randint

def verify_hash(key, lengthTable):
    isFound = False
    count = 0
        
    while (count != lengthTable):
        randomNum = randint(0, lengthTable)
        count = count + 1
        print(randomNum)
        if (randomNum == key):
            # print(randomNum)
            isFound = True

    return isFound


def hash_function(set):
    length = len(set)
    hash_value = 0
    for s in set:
        hash_value = hash_value + s

    return hash_value % length
    # return hash_value

# set = [5, 12, 19, 7, 13, 27]
set = []
max = 0
lengthTable = 5
while(max != 5):
    randomNum = randint(0, lengthTable) 
    set.append(randomNum)
    max = max + 1

# print(set)

key = hash_function(set)

verification = verify_hash(key, lengthTable)
print('key', key)
print(verification)