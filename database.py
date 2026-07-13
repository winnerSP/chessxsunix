import sqlite3


DATABASE = "chessxsunix.db"


def connect():

    return sqlite3.connect(DATABASE)



def create_tables():

    db = connect()
    cursor = db.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        rating INTEGER,
        games INTEGER

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS achievements(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        achievement TEXT

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tournaments(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT

    )
    """)



    db.commit()
    db.close()



create_tables()
