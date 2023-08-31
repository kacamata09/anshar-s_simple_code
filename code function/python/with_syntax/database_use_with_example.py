import sqlite3


#### cara kuno
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

try:
    cursor.execute('SELECT * FROM table')
    data = cursor.fetchall()
finally:
    cursor.close()
    connection.close()


#### cara modern
with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM table')
    data = cursor.fetchall()
# Koneksi akan ditutup secara otomatis setelah blok with selesai
