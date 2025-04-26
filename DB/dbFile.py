from myErrors import TableNotFound
import sqlite3

with sqlite3.connect("data.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY_KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INTEGER,
        genre TEXT
    );
    ''')

    conn.commit()

    #проверка существования таблицы
    cursor.execute('''
    SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'books'
    ''')

    result = cursor.fetchone()

    if result:
        insert = '''
        INSERT INTO books (title, author, year_published, genre)
        VALUES (?, ?, ?, ?);
        '''
        bookdata = [
            ( "The Great Gatsby", "F. Scott Fitzgerald", 1984, "Fiction" ),
            ( "1984", "George Orwell", 1949, "Dystopian" ),
            ( "To Kill a Mockingbird", "Harper Lee", 1960, "Classic" )
        ]
        cursor.executemany(insert, bookdata)
        conn.commit()
        
    else:
        raise TableNotFound("Table does not exist")

