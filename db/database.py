import sqlite3

def Database():
    global conn, curs
    # Connect database
    conn = sqlite3.conn("database.db")
    curs = conn.cursor()
    # Execute query
    curs.execute("CREATE TABLE IF NOT EXISTS `user` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, score INTEGER)")
    