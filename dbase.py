import sqlite3

class Dbase:
    def __init__(self, dbase):
        self.dbase = dbase
        self.conn = sqlite3.connect(self.dbase)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS stats (name TEXT, score INTEGER)")
        self.conn.commit()

    def insert(self, name, score):
        self.cur.execute("INSERT INTO stats VALUES (?, ?)", (name, score))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM stats")
        rows = self.cur.fetchall()
        return rows

    def search(self, name="", score=""):
        self.cur.execute("SELECT * FROM stats WHERE name=? OR score=?", (name, score))
        rows = self.cur.fetchall()
        return rows

    def update(self, name, score):
        self.cur.execute("UPDATE stats SET score=? WHERE name=?", (score, name))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
