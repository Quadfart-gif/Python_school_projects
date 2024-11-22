#have 2 books by default
Library = {
    "To kill a mocking bird": {"author": "George Orwell", "genre": "classic"},
    "1984": {"author": "george Orwell", "genre": "classic"},

}


def add_book():
    #Adds new book
    title = input("Enter the title of book: ")
    Author = input("Enter the Author of book: ")
    genre = input("Enter the genre: ")

    #This adds a new book to the current dictionary library
    #this adds a key which is the title inputted earlier
    Library[title] = {
        "Author": Author,
        "Genre": genre
    }
    print(f"Book {title} added successfully")


def remove_book():
    #removes the book from current library
    #First we gotta know how to remove a key


