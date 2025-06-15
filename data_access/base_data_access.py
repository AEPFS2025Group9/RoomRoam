import sqlite3
import os

class BaseDataAccess:
    def __init__(self, db_path: str = None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        default_path = os.path.join(base_dir, "database", "hotel_reservation_sample.db")
        self.db_path = db_path or os.environ.get("ROOMROAM_DB_PATH", default_path)

        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found: {self.db_path}")

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
