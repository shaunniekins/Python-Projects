# using python, implement hash data structure with linear probing. it should have insertion, display, search, delete, menu (for selection of what to do ) and the implementation of Load Factor and rehashing. (use only functions)

def create_table(size):
    return [None] * size, size, 0

def hash_function(key, size):
    return key % size

def insert(table, size, count, key):
    if count == size:
        table, size, count = rehash(table, size, count)
    index = hash_function(key, size)
    while table[index] is not None:
        index = (index + 1) % size
    table[index] = key
    count += 1
    return table, size, count

def search(table, size, key):
    index = hash_function(key, size)
    while table[index] is not None:
        if table[index] == key:
            return index
        index = (index + 1) % size
    return -1

def delete(table, size, count, key):
    index = search(table, size, key)
    if index != -1:
        table[index] = None
        count -= 1
    return table, size, count

def display(table, size):
    for i in range(size):
        print(i, end = " ")
        if table[i] is not None:
            print(table[i])
        else:
            print()

def load_factor(count, size):
    return count / size

def rehash(table, size, count):
    old_table = table
    size *= 2
    table = [None] * size
    count = 0
    for key in old_table:
        if key is not None:
            table, size, count = insert(table, size, count, key)
    return table, size, count

def menu():
    table, size, count = create_table(5)
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Load Factor")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            key = int(input("Enter the key to insert: "))
            table, size, count = insert(table, size, count, key)
        elif choice == 2:
            key = int(input("Enter the key to delete: "))
            table, size, count = delete(table, size, count, key)
        elif choice == 3:
            key = int(input("Enter the key to search: "))
            print("Key found at", search(table, size, key))
        elif choice == 4:
            display(table, size)
        elif choice == 5:
            print("Load factor:", load_factor(count, size))
        elif choice == 6:
            break



menu()