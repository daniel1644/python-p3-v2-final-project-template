# CLI Books Library Application

## Project Statement

Develop a command-line interface application that simulates a library system, allowing users to add, list, borrow, return, update, delete books, and quit the application.

## Project Description

This Command-Line Interface (CLI) application simulates a library system, allowing users to perform various operations on books such as adding, listing, borrowing, returning, updating, deleting books, and quitting the application.

## Features

- **Add a book**: Add a new book to the library with title, author, and year.
- **List all books**: List all books in the library with their status (available or borrowed).
- **Borrow a book**: Borrow a book by its ID.
- **Return a book**: Return a borrowed book by its ID.
- **Update a book**: Update book details by its ID.
- **Delete a book**: Delete a book by its ID.
- **Quit the application**: Exit the application.

## Prerequisites

- Python 3.x
<<<<<<< Updated upstream
=======
- SQLite
>>>>>>> Stashed changes

## Project Structure

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
├── models
│ ├── init.py
│ ├── book.py
│ ├── author.py
│ └── borrower.py
├── cli.py
├── database.py
<<<<<<< Updated upstream
├── debug.py
├── helpers.py
=======
├── db_setup.py
├── debug.py
├── helpers.py
├── models.py
>>>>>>> Stashed changes
└── seed.py


## Installation

1. **Clone the repository**:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
<<<<<<< Updated upstream

    If you are using Pipenv:

=======
    If you are using Pipenv:
>>>>>>> Stashed changes
    ```sh
    pipenv install
    pipenv shell
    ```

    Alternatively, if you are using pip and virtualenv:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Usage

1. **Seed the library** with initial data:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    ```sh
    python lib/seed.py
    ```

2. **Run the application**:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    ```sh
    python lib/cli.py
    ```

3. **Follow the on-screen menu** to perform library operations:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    ```
    Library Menu:
    1. Add a book
    2. List all books
    3. Borrow a book
    4. Return a book
    5. Delete a book
    6. Update a book
    7. Quit
    Enter your choice (1-7):
    ```

## Example
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
```sh
Library Menu:
1. Add a book
2. List all books
3. Borrow a book
4. Return a book
5. Delete a book
6. Update a book
7. Quit
Enter your choice (1-7): 2

List of books:
ID: 1 - 1984 by George Orwell (1949) - Available
ID: 2 - To Kill a Mockingbird by Harper Lee (1960) - Available
...

Enter your choice (1-7): 3
Enter the ID of the book to borrow: 1
1984 has been borrowed.
<<<<<<< Updated upstream


Contributing
=======
```

## Testing
Run the debug script to test the functionality:

```sh
Copy code
python lib/debug.py
```

## Contributing
>>>>>>> Stashed changes
Fork the repository.
Create your feature branch (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.
License
This project is licensed under https://github.com/daniel1644/python-p3-v2-final-project-template License.

