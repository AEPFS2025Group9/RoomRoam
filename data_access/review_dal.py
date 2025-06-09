from data_access.base_data_access import BaseDataAccess
from datetime import datetime

class ReviewDAL(BaseDataAccess):
    def create_table(self):
        create_sql = """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_id INTEGER NOT NULL,
            hotel_id INTEGER NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            comment TEXT,
            review_date TEXT,
            FOREIGN KEY (guest_id) REFERENCES guests(id),
            FOREIGN KEY (hotel_id) REFERENCES hotels(id)
        )
        """
        self.execute(create_sql)

    def insert_review(self, guest_id: int, hotel_id: int, rating: int, comment: str):
        sql = """
        INSERT INTO reviews (guest_id, hotel_id, rating, comment, review_date)
        VALUES (?, ?, ?, ?, ?)
        """
        review_date = datetime.now().strftime("%Y-%m-%d")
        return self.execute(sql, (guest_id, hotel_id, rating, comment, review_date))

    def get_reviews_by_hotel(self, hotel_id: int):
        sql = """
        SELECT id, guest_id, rating, comment, review_date
        FROM reviews
        WHERE hotel_id = ?
        ORDER BY review_date DESC
        """
        return self.fetchall(sql, (hotel_id,))

def get_last_inserted_id(self):
    sql = "SELECT last_insert_rowid()"
    result = self.fetchone(sql)
    return result[0] if result else -1
