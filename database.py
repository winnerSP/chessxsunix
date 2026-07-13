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
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password_hash TEXT,

    rating INTEGER DEFAULT 800,

    xp INTEGER DEFAULT 0,

    games INTEGER DEFAULT 0

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
    cursor.execute("""
CREATE TABLE IF NOT EXISTS tournaments(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    status TEXT

)
""")



    db.commit()
    db.close()



create_tables()
