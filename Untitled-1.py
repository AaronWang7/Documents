#Aaron.Wang Personal Library Program


# Pseudocode:
# - Use a list to store items as dictionaries with title author and type
# - Create functions for each different jobs


#library list
library = []

def display():
    # Display the chouice
    print("1 = Add an item")
    print("2 = Search for an item")
    print("3 = Remove an item")
    print("4 = Display all items")
    print("5 = Exit the program")

def add_item():
    #Add a new item to the library
    item_type = input("Enter the type of item (book, movie, music): ")
    title = input("Enter the title: ")
    author = input("Enter the author/artist/director: ")
    # Add the item as a dictionary
    library.append({"type": item_type, "title": title, "author": author})
    print(f"Item '{title}' added to library.")

def search_item():
    """Search for an item by title or author."""
    itemname = input("Enter the title or author to search: ")
    results = []
    #library loop
    for item in library:
        # Check if the item is the title or author
        if itemname in item["title"] or itemname in item["author"]:
            results.append(item)  # add item to results list
            print(f"Item found!{results}")
    

def remove_item():
    #Remove item
    title = input("Enter the title of item to remove: ")
    for item in library:
        if item["title"] == title:
            library.remove(item)
            print(f"Item {title} removed from library")
            return
    print(f"No item with the title {title}")

def display_all():
    # Display all item in the library
    print(library)

def main():
    # Main function to run the library program
    while True:
        display()
        try:
            choice = int(input("Enter your choice 1-5: "))
            if choice == 1:
                add_item()
            elif choice == 2:
                search_item()
            elif choice == 3:
                remove_item()
            elif choice == 4:
                display_all()
            elif choice == 5:
                print("Exiting the program. Goodbye!!!!!!!!!!!!!!!")
                break
            else:
                print("Wrong choice, Please enter a number between 1- 5!")
        except ValueError:
            print("Wrong input. Please enter a right number!")

# Run the program
main()
