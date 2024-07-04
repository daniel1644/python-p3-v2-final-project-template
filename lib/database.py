import sqlite3
import os

DB_FILE = 'library.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year TEXT NOT NULL,
        borrowed INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

def reset_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    init_db()
