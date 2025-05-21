import sqlite3

class BaseDataAccess:
    def __init__(self, db_path: str = "database/hotel.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row  # Optional: allows name-based access
        self.cursor = self.conn.cursor()

    def fetchone(self, sql: str, params: tuple = ()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    def fetchall(self, sql: str, params: tuple = ()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def execute(self, sql: str, params: tuple = ()):
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.lastrowid, self.cursor.rowcount

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()

