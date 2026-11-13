import sqlite3

connection = sqlite3.connect('books.sl3')

cursor = connection.cursor()


sql = "select * from books b where b.price > 25"
cursor.execute(sql)
books = cursor.fetchall()
for book in books:
    id,name,price = book
    print(f"{id} | {name} | {(price + (price * 0.2)) * 60:.2f}₴ (+{price*0.2*60:.2f}₴)")


connection.commit()

connection.close()
