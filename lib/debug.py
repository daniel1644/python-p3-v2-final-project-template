from models import Library, Book, Author
from sqlalchemy.orm import sessionmaker

def run_tests():
    library = Library()

    # Clear the library database for a clean test environment
    Session = sessionmaker(bind=library.engine)
    session = Session()
    session.query(Book).delete()
    session.query(Author).delete()
    session.commit()

    # Test adding books
    print("Adding books...")
    library.add_book("The Lean Startup", "Eric Ries", 2011)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    library.add_book("1984", "George Orwell", 1949)
    print("Books added.")

    # Test listing books
    print("\nListing all books:")
    print(library.list_books())

    # Test borrowing a book
    print("\nBorrowing a book with ID 1...")
    print(library.borrow_book(1))
    print("Listing all books:")
    print(library.list_books())

    # Test returning a book
    print("\nReturning a book with ID 1...")
    print(library.return_book(1))
    print("Listing all books:")
    print(library.list_books())

    # Test updating a book
    print("\nUpdating a book with ID 1...")
    print(library.update_book(1, "The Lean Startup Updated", "Eric Ries", 2012))
    print("Listing all books:")
    print(library.list_books())

    # Test deleting a book
    print("\nDeleting a book with ID 1...")
    print(library.delete_book(1))
    print("Listing all books:")
    print(library.list_books())

if __name__ == "__main__":
    run_tests()
