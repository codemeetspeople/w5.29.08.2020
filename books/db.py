import sqlite3
import os
import pathlib

BOOKS_ROOT = pathlib.Path(__file__).parent.absolute()
DATABASE_PATH = os.path.join(BOOKS_ROOT, 'books.db')

connection = None


def get_connection():
    global connection
    if not connection:
        connection = sqlite3.connect(DATABASE_PATH)
    return connection


def create_database():
    CHECK_TABLE_EXISTS = (
        'SELECT count(name) FROM sqlite_master WHERE type=\'table\' AND name=\'book\''
    )
    CREATE_BOOK_TABLE = (
        'CREATE TABLE book ('
        '    id INTEGER PRIMARY KEY AUTOINCREMENT,'
        '    author text NOT NULL,'
        '    title text NOT NULL'
        ');'
    )

    conn = get_connection()
    cursor = conn.cursor()
    result = cursor.execute(CHECK_TABLE_EXISTS)
    is_exists = result.fetchone()[0]

    if is_exists == 0:
        cursor.execute(CREATE_BOOK_TABLE)
    conn.commit()


CREATE_BOOK_STATEMENT = 'INSERT INTO book (author, title) VALUES (?, ?)'
UPDATE_BOOK_STATEMENT = 'UPDATE book SET author = ?, title = ? WHERE id = ?'
SELECT_BOOK_STATEMENT = 'SELECT * FROM book WHERE id=?'

create_database()
