import sqlite3

conn = sqlite3.connect('wufazhuce_com.db')
c = conn.cursor()
print('DATABASE OPEN OK')

# CREATE TABLE
c.execute('''CREATE TABLE OneArticulo(
                ID INT PRIMARY KEY NOT NULL,
                TITLE VARCHAR(255) NULL,
                AUTOR VARCHAR(20) NULL,
                COMILLA VARCHAR(255) NULL,
                ARTICULO TEXT NULL
              )''')
conn.commit()
print(' OK')
conn.close()
