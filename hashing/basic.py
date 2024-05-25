def create_table(size):
    return [None] * size

def hash_key(table, key):
    size = len(table)
    return sum(ord(c) - ord('a') + 1 for c in key) % size

def insert(table, key):
    index = hash_key(table, key)
    table[index] = key

def search(table, key):
    index = hash_key(table, key)
    if table[index] == key:
        return index
    else:
        return None

def delete(table, key):
    index = hash_key(table, key)
    if table[index] == key:
        table[index] = None

def display(table):
    for i in range(len(table)):
        print(i, end = " ")

        if table[i]:
            print(f"--> {table[i]}")
        else:
            print()

# Initialize the table
table = create_table(7)
insert(table, "ab")
insert(table, "cd")
insert(table, "efg")

# Menu for user interaction
while True:
    print("\n1. Display\n2. Search\n3. Delete\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        display(table)
    elif choice == 2:
        key_to_search = input("Enter the key to search: ")
        index = search(table, key_to_search)
        if index is not None:
            print(f"Key '{key_to_search}' found at index {index}")
        else:
            print(f"Key '{key_to_search}' not found")
    elif choice == 3:
        key_to_delete = input("Enter the key to delete: ")
        delete(table, key_to_delete)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")