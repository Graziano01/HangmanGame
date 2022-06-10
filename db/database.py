import sqlite3
from PROGETTO.menu import USERNAME, PASSWORD

def Database():
    global conn, curs
    # Connect database
    conn = sqlite3.conn("database.db")
    curs = conn.cursor()
    # Execute query
    curs.execute("CREATE TABLE IF NOT EXISTS `user` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, score INTEGER)")
    
def scoreUpdate():
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute("UPDATE user SET score=1 WHERE id=(?)", (id.get())) # Change score
    conn.commit()
    conn.close()

def Register():
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        print("Complete the required field!") # Change with label config
    else:
        curs.execute("SELECT * FROM `user` WHERE `username` = ?", (USERNAME.get()))
        if curs.fetchone() is not None:
            print("Username alredy taken!") # Change with label config
        else:
            curs.execute("INSERT INTO `user` (username, password, score) VALUES (?, ?, 0)", (str(USERNAME.get()), str(PASSWORD.get())))
            conn.commit()
            # TODO: add success message
        curs.close()
        conn.close()

def Login():
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        print("Complete the required field!") # Change with label config
    else:
        curs.execute("SELECT * FROM `user` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if curs.fetchone() is not None:
            print("Successfully login!") # Change with label config
        else:
            print("Invalid username or password!")