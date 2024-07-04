
def get_user_choice():
    print("\nWelcome to the DANIEL Library: Please select an Option:")
    print("1. Add a book")
    print("2. List all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Delete a book")
    print("6. Update a book")
    print("7. Quit")
    return input("Enter your choice (1-7): ")

def get_book_details():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book year: ")
    return title, author, year

def get_book_id(action):
    return int(input(f"Enter the ID of the book to {action}: "))

def get_updated_book_details():
    new_title = input("Enter new book title: ")
    new_author = input("Enter new book author: ")
    new_year = input("Enter new book year: ")
    return new_title, new_author, new_year

def display_books(books):
    print("\nList of books:")
    print(books)

def display_message(message):
    print(message)
