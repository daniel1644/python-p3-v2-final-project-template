from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    borrowed = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', back_populates='books')

def setup_database():
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
    return engine

if __name__ == "__main__":
    setup_database()
