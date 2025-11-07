import sqlite3

def connect_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            isbn TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def insert_book(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", 
                   (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_books(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR year LIKE ? OR isbn LIKE ?", 
                   ('%'+title+'%', '%'+author+'%', '%'+year+'%', '%'+isbn+'%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_book(id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_book(id, title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", 
                   (title, author, year, isbn, id))
    conn.commit()
    conn.close()
