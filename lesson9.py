import sqlite3

connection = sqlite3.connect('books.sl3')

cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXIST books (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       price REAL NOT NULL DEFAULT 0.0
    );"""

with open("books.txt", "w", encoding="uts-8") as books_file:
    for book_line in books_file:
        line = book_line.strip().split("")
        name = line[0]
        price = float(line[1])

    sql = "INSERT INTO books VALUES (name, price) VALUES (?, ?);"
    cursor.execute(sql)

connection.commit()

