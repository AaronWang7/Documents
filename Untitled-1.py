# Aaron.Wang Personal Library Program

library = []

def display_menu():
    print("1. Add an item")
    print("2. Search for a item")
    print("3. Remove a item")
    print("4. Update a item")
    print("5. Display all items (simple)")
    print("6. Display all items (detail)")
    print("7. Exit the program")

def add_item():
    item_type = input("Enter the type of item book, movie, music: ").capitalize()
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = input("Enter the year of release: ")
    genre = input("Enter the genre: ")
    
    library.append({
        "type": item_type,
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    })
    print(f"Item '{title}' added!")

def search_items():
    search_items = input("Enter the title or author to search: ").strip().lower()
    results = [item for item in library if search_items in item["title"].lower() or search_items in item["author"].lower()]

    if results:
        for item in results:
            print(f"{item['title']} by {item['author']} ({item['year']})")
    else:
        print("No matching items")

def remove_item():
    title = input("Enter the title of the item to remove: ")
    for item in library:
        if item["title"].lower() == title.lower():
            library.remove(item)
            print(f"Item '{title}' removed!")
            return
    print(f"No item with the title '{title}'")

def update_item():
    title = input("enter the title of the item to update: ")
    for item in library:
        if item["title"].lower() == title.lower():
            print(f"Updating '{title}'... Leave blank to keep existing values.")
            new_author = input(f"Enter new author (Current: {item['author']}): ") or item["author"]
            new_year = input(f"Enter new year (Current: {item['year']}): ") or item["year"]
            new_genre = input(f"Enter new genre (Current: {item['genre']}): ") or item["genre"]
            
            item["author"], item["year"], item["genre"] = new_author, new_year, new_genre
            print(f"Item '{title}' updated!")
            return
    print(f"No item with the title '{title}'")

def display_all(simple=True):
    if not library:
        print("There is nothing in the libary")
        return
    
    for item in library:
        if simple:
            print(f"{item['title']} by {item['author']}")
        else:
            print(f"Type: {item['type']}\nTitle: {item['title']}\nAuthor: {item['author']}\nYear: {item['year']}\nGenre: {item['genre']}\n")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice1-7: "))
            if choice == 1:
                add_item()
            elif choice == 2:
                search_item()
            elif choice == 3:
                remove_item()
            elif choice == 4:
                update_item()
            elif choice == 5:
                display_all(simple=True)
            elif choice == 6:
                display_all(simple=False)
            elif choice == 7:
                print("Goodbye!")
                break
            else:
                print("Wrong choice, enter a number 1-7")
        except ValueError:
            print("Wrong input, enter a number")

main()




