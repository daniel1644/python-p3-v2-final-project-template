
from models import Book

def debug_book():
    book = Book("1984", "George Orwell", 1949)
    print(book)
    book.borrow()
    print(book)
    book.return_book()
    print(book)

if __name__ == "__main__":
    debug_book()



