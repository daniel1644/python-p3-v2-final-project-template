
def seed_library(library):
    books = [
        {"title": "The Lean Startup", "author": "Eric Ries", "year": "2011"}, 
        {"title": "The 4-Hour Work Week", "author": "Timothy Ferriss", "year": "2007"},
        {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "year": "1936"},
        {"title": "The Hard Thing About Hard Things", "author": "Ben Horowitz", "year": "2014"},
        {"title": "Zero to One", "author": "Peter Thiel", "year": "2014"},
        {"title": "The Power of Now", "author": "Eckhart Tolle", "year": "1997"},
        {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year": "1997"}, 
        {"title": "The 7 Habits of Highly Effective People", "author": "Stephen Covey", "year": "1989"}, 
        {"title": "Essentialism: The Disciplined Pursuit of Less", "author": "Greg McKeown", "year": "2014"}, 
        {"title": "Influence: The Psychology of Persuasion", "author": "Robert Cialdini", "year": "1984"},
        {"title": "1984", "author": "George Orwell", "year": "1949"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": "1960"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": "1925"},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": "1813"},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": "1951"},
        {"title": "Moby-Dick", "author": "Herman Melville", "year": "1851"},
        {"title": "War and Peace", "author": "Leo Tolstoy", "year": "1869"},
        {"title": "The Odyssey", "author": "Homer", "year": "8th Century BC"},
        {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": "1866"},
        {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": "1880"}
    ]

    for book_data in books:
        library.add_book(book_data['title'], book_data['author'], book_data['year'])
