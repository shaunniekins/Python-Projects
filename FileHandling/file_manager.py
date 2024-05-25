""" A simple command-line interface to perform file operations. The user is presented with a menu to choose from options like creating a file, reading a file, updating a file, deleting a file, or exiting the program. The code utilizes the `os`` module for file operations and uses file input/output functions to interact with the files.
"""

import os


def choose_Option():
    print('(1): Create a file\n(2): Read a file\n(3): Update a file\n(4): Delete a file\n(5): Exit')
    choice = input("Enter a choice (1, 2, 3, 4, or 5): ")
    choice_Function(choice)


def choice_Function(choice):
    if choice == '1':
        create_File()
    elif choice == '2':
        read_File()
    elif choice == '3':
        update_File()
    elif choice == '4':
        delete_File()
    elif choice == '5':
        exit()
    else:
        print('Invalid choice.')
        choose_Option()


def create_File():
    file_Name = input("Enter the file name to be created: ")
    file_Path = file_Name + '.txt'
    if os.path.exists(file_Path):
        print('File already exists!\n')
    else:
        with open(file_Path, 'w') as file:
            file.write('First line\n')
        print(file_Path + ' is created!\n')

    choose_Option()


def read_File():
    file_Name = input("Enter the file name to read: ")
    file_Path = file_Name + '.txt'
    if os.path.exists(file_Path):
        with open(file_Path, 'r') as file:
            print('\n<----------------------------------->')
            print(file.read())
            print('<----------------------------------->\n')

        edit = input("Do you want to edit the file? (1: yes, 2: no): ")
        if edit == '1':
            update_File(file_Name)
        elif edit == '2':
            choose_Option()
        else:
            print('Wrong input.\n')
            choose_Option()
    else:
        print('File does not exist!\n')
        choose_Option()


def update_File(file_Name=None):
    if file_Name is None:
        file_Name = input("Enter the file name to write: ")

    file_Path = file_Name + '.txt'
    if os.path.exists(file_Path):
        with open(file_Path, 'a') as file:
            text = input("Enter text: ")
            file.write('\n' + text)
        print('\nText added!\n')
        with open(file_Path, 'r') as file_Read:
            print('\n<----------------------------------->')
            print(file_Read.read())
            print('<----------------------------------->\n')
    else:
        print('File does not exist!\n')

    choose_Option()


def delete_File():
    file_Name = input('Enter the file name to be deleted: ')
    file_Path = file_Name + '.txt'
    if os.path.exists(file_Path):
        os.remove(file_Path)
        print('File deleted!\n')
    else:
        print('File does not exist!\n')

    choose_Option()


choose_Option()
