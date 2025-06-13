import sqlite3

def create_address_table():
    conn = sqlite3.connect("hotel_reservation_sample.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Address (
            address_id INTEGER PRIMARY KEY AUTOINCREMENT,
            street TEXT NOT NULL,
            city TEXT NOT NULL,
            zip_code INTEGER NOT NULL
        );
    """)
    conn.commit()
    conn.close()

create_address_table()