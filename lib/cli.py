from models import Library
from helpers import (
    get_user_choice, get_book_details, get_book_id,
    display_books, display_message, get_updated_book_details
)
from seed import seed_library

def main():
    library = Library()
    seed_library(library)  
    
    while True:
        choice = get_user_choice()
        
        if choice == "1":
            title, author, year = get_book_details()
            library.add_book(title, author, year)
            display_message("Book added successfully!")
        
        elif choice == "2":
            books_list = library.list_books()
            display_books(books_list)
        
        elif choice == "3":
            book_id = get_book_id("borrow")
            message = library.borrow_book(book_id)
            display_message(message)
        
        elif choice == "4":
            book_id = get_book_id("return")
            message = library.return_book(book_id)
            display_message(message)
        
        elif choice == "5":
            book_id = get_book_id("delete")
            message = library.delete_book(book_id)
            display_message(message)
        
        elif choice == "6":
            book_id = get_book_id("update")
            new_title, new_author, new_year = get_updated_book_details()
            message = library.update_book(book_id, new_title, new_author, new_year)
            display_message(message)
        
        elif choice == "7":
            display_message("Goodbye!")
            break
        
        else:
            display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
