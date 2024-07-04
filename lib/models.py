from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Author, Book, setup_database

class Library:
    def __init__(self):
        self.engine = setup_database()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_book(self, title, author_name, year):
        author = self.session.query(Author).filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            self.session.add(author)
            self.session.commit()

        new_book = Book(title=title, year=year, author=author)
        self.session.add(new_book)
        self.session.commit()

    def list_books(self):
        books = self.session.query(Book).all()
        if not books:
            return "No books in the library."
        else:
            return "\n".join(f"ID: {book.id} - {book.title} by {book.author.name} ({book.year}) - {'Borrowed' if book.borrowed else 'Available'}" for book in books)

    def borrow_book(self, book_id):
        book = self.session.query(Book).filter_by(id=book_id, borrowed=False).first()
        if book:
            book.borrowed = True
            self.session.commit()
            return f"{book.title} has been borrowed."
        return f"Book with ID '{book_id}' not found or already borrowed."

    def return_book(self, book_id):
        book = self.session.query(Book).filter_by(id=book_id, borrowed=True).first()
        if book:
            book.borrowed = False
            self.session.commit()
            return f"{book.title} has been returned."
        return f"Book with ID '{book_id}' not found or not borrowed."

    def delete_book(self, book_id):
        book = self.session.query(Book).filter_by(id=book_id).first()
        if book:
            self.session.delete(book)
            self.session.commit()
            return f"{book.title} has been deleted."
        return f"Book with ID '{book_id}' not found."

    def update_book(self, book_id, new_title, new_author_name, new_year):
        book = self.session.query(Book).filter_by(id=book_id).first()
        if book:
            author = self.session.query(Author).filter_by(name=new_author_name).first()
            if not author:
                author = Author(name=new_author_name)
                self.session.add(author)
                self.session.commit()
            book.title = new_title
            book.author = author
            book.year = new_year
            self.session.commit()
            return f"Book with ID '{book_id}' has been updated."
        return f"Book with ID '{book_id}' not found."
