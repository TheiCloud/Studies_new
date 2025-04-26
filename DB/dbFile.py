from myErrors import TableNotFound
import sqlite3

with sqlite3.connect("data.db") as conn:
    cursor = conn.cursor()
    # создание таблицы
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        # insert = '''
        # INSERT INTO books (title, author, year_published, genre)
        # VALUES (?, ?, ?, ?);
        # '''
        # bookdata = [
        #     ( "The Great Gatsby", "F. Scott Fitzgerald", 1984, "Fiction" ),
        #     ( "1984", "George Orwell", 1949, "Dystopian" ),
        #     ( "To Kill a Mockingbird", "Harper Lee", 1960, "Classic" )
        #]
        #cursor.executemany(insert, bookdata)
        #conn.commit()

        print("задание 3")
        request = '''
        SELECT title 
        FROM books
        '''
        cursor.execute(request)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")


        print("задание 4")
        request = '''
        SELECT title 
        FROM books
        WHERE year_published > 1950
        '''
        cursor.execute(request)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")


        print("задание 5")
        request = '''
                SELECT title 
                FROM books
                WHERE title LIKE 'T%';
                '''
        cursor.execute(request)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")


        print("задание 6")
        request = '''
        SELECT title FROM books ORDER BY year_published ASC;
        '''
        cursor.execute(request)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")






    else:
        raise TableNotFound("Table does not exist")

