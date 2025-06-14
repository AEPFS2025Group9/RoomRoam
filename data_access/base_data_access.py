import sqlite3
import os

class BaseDataAccess:
    def __init__(self, db_path: str = None):
        if db_path:
            self.db_path = db_path 
        else:
            self.db_path = "RoomRoam/database/using_db.db"
            os.environ["ROOMROAM_DB_PATH"] = self.db_path
    
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def fetchone(self, sql: str, params: tuple = ()):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.fetchone()

    def fetchall(self, sql: str, params: tuple = ()):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.fetchall()

    def execute(self, sql: str, params: tuple = ()):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid, cursor.rowcount
