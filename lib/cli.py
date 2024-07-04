from helpers import get_user_choice, get_book_details, get_book_id, display_books, display_message, get_updated_book_details
from seed import seed_library
from database import get_db_connection, init_db

class Library:
    def __init__(self):
        init_db()

    def add_book(self, title, author, year):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, year, borrowed) VALUES (?, ?, ?, ?)', (title, author, year, 0))
        conn.commit()
        conn.close()

    def list_books(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "No books in the library."
        else:
            books = [dict(row) for row in rows]
            return "\n".join(
                f"ID: {book['id']} - {book['title']} by {book['author']} ({book['year']}) - {'Borrowed' if book['borrowed'] else 'Available'}" 
                for book in books
            )

    def borrow_book(self, book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET borrowed = 1 WHERE id = ? AND borrowed = 0', (book_id,))
        if cursor.rowcount == 0:
            message = f"Book with ID '{book_id}' not found or already borrowed."
        else:
            message = "Book borrowed successfully."
        conn.commit()
        conn.close()
        return message

    def return_book(self, book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET borrowed = 0 WHERE id = ? AND borrowed = 1', (book_id,))
        if cursor.rowcount == 0:
            message = f"Book with ID '{book_id}' not found or not borrowed."
        else:
            message = "Book returned successfully."
        conn.commit()
        conn.close()
        return message

    def delete_book(self, book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        if cursor.rowcount == 0:
            message = f"Book with ID '{book_id}' not found."
        else:
            message = "Book deleted successfully."
        conn.commit()
        conn.close()
        return message

    def update_book(self, book_id, new_title, new_author, new_year):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?', (new_title, new_author, new_year, book_id))
        if cursor.rowcount == 0:
            message = f"Book with ID '{book_id}' not found."
        else:
            message = "Book updated successfully."
        conn.commit()
        conn.close()
        return message

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
            display_message("Quitting the application. Goodbye! ASANTE SANA!")
            break
        
        else:
            display_message("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
