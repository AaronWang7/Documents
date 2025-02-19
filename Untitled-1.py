import csv
import os

# Load movie data
def load_movies(file_path="Movies list.csv"):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        return []
    
    # Open the CSV file and read the movie data
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Print column names to help the user
        print(f"Columns: {reader.fieldnames}")
        
        # Return the list of movies
        return [row for row in reader]

# Filter movies based on genre and director
def filter_movies(movies, genre=None, director=None):
    return [
        movie for movie in movies
        if (genre.lower() in movie["genre"].lower() if genre else True) and
           (director.lower() in movie["director"].lower() if director else True)
    ]

# Print the movie list
def print_movies(movies):
    if movies:
        for movie in movies:
            print(f"{movie['title']} | {movie['genre']} | {movie['director']} | {movie['length']} min")
    else:
        print("No movies to display.")

# Main function to control the program
def main():
    # Load the movies from the file
    movies = load_movies("Movies list.csv")
    
    # Continue until the user chooses to exit
    while True:
        print("\n1. Search Movies\n2. Show All Movies\n3. Exit")
        choice = input("Choose an option: ")

        # Search for movies based on genre and director
        if choice == "1":
            genre = input("Enter genre (or press Enter to skip): ")
            director = input("Enter director (or press Enter to skip): ")
            filtered_movies = filter_movies(movies, genre, director)
            print_movies(filtered_movies)

        # Show all movies
        elif choice == "2":
            print_movies(movies)

        # Exit the program
        elif choice == "3":
            break

        else:
            print("Wrong option Please try again")

# Run the program
main()


