#Aaron.Wang Personal Library program


"""
Create a program that allows user to manage a personal library catalog for any ONE type (books, movies, music, etc). 
The project needs to allow users to add new items, display ALL contents, search for a specific item (by title, author/artist/director),
 remove a book from the library, exit the program. 
note: We will be building off this project later on so make sure you do a good job on it! 
"""
Author = {}
Title = {}
libary = []
chouice = {"Add items to the libary":1,"Serch Items to the libary":2, "remove items to libary":3

}
import time 
import random
def delay():
    print("r/Loding...")
    time.sleep(1)

def main():
    print(chouice)
    delay
    act = int(input("what whould you like to do?"))
    if act == 1:
        add

    
def add():
    item_add = input("What item would you like to add?:")
    Title = input("What is the title?:")
    author = input("who is the author?:")
    if item_add in libary:
        print("Sorry the item is already in the libary")
    else:
        libary.append(item_add)
        Author.add()

def remove():
        item_remove = input("What item would you like to remove?:")
        if item_remove not in libary:
            print("Sorry the item is not in the libary")
        else:
            libary.remove(item_remove)


def search():
    print("You can scearch by title, author")
    searchng = input("What Item whould you like to search?:")






