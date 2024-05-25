def switch(numbers):
    count = 0
    state = 0
    
    for number in numbers:
        if number == state:
            count += 1 
            state = 1 - state
    return count

print(switch([0, 1, 0, 1, 1, 0, 1, 1]))