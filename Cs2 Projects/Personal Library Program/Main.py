#Aaron.Wang Personal Library program


"""
Create a program that allows user to manage a personal library catalog for any ONE type (books, movies, music, etc). 
The project needs to allow users to add new items, display ALL contents, search for a specific item (by title, author/artist/director),
 remove a book from the library, exit the program. 
note: We will be building off this project later on so make sure you do a good job on it! 
"""
Author = []
Titles = []
libary = []
chouice = {"Add items to the libary":1,"Serch Items to the libary":2, "remove items to libary":3

}
Tofind = []
import time 
import random
def delay():
    print("r/Loding...")
    time.sleep(1)
while True:
    def main():
        print(chouice)
        delay
        act = int(input("what whould you like to do?:"))
        if act == 1:
            add()
        elif act == 2:
            remove()
        elif act == 3:
            search()
        else:
            print("Wrong input")
    


        
    def add():
        item_add = input("What item would you like to add?:")
        Title = input("What is the title?:")
        author = input("who is the author?:")
        if item_add in libary:
            print("Sorry the item is already in the libary")
        else:
            libary.append(item_add)
            Author.append(author)
            Titles.append(Title)


    def remove():
            item_remove = input("What item would you like to remove?:")
            if item_remove not in libary:
                print("Sorry the item is not in the libary")
            else:
                libary.remove(item_remove)


    def search():
        print("You can scearch by title, author")
        searchng = input("What Item whould you like to search?:")
        when = int(input("When did you add it 0 = 1?"))
        if searchng in libary:
            print("Seems Like it is in the libary!")
            print(f"The item is{searchng}, wrote by{Author[when]} and the title is {Titles[when]} ")
    main()
            






