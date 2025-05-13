import sqlite3

class BaseDataAccess:
    def __init__(self, db_path: str = "database/hotel.db"):
        """
        Stellt eine Verbindung zur SQLite-Datenbank her.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def fetchone(self, sql: str, params: tuple = ()):
        """
        Führt ein SELECT aus und gibt einen einzelnen Datensatz zurück.
        """
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    def fetchall(self, sql: str, params: tuple = ()):
        """
        Führt ein SELECT aus und gibt alle Datensätze zurück.
        """
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def execute(self, sql: str, params: tuple = ()):
        """
        Führt INSERT, UPDATE oder DELETE aus und committed automatisch.
        Gibt die ID und die Anzahl der betroffenen Zeilen zurück.
        """
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.lastrowid, self.cursor.rowcount

    def close(self):
        """
        Schliesst die Datenbankverbindung.
        """
        self.conn.close()
