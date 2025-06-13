import pandas as pd
from data_access.base_data_access import BaseDataAccess
from model.booking import Booking
from typing import List, Dict, Optional

class BookingDataAccess(BaseDataAccess):
    def create_booking(self, booking: Booking) -> int:
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date)
        VALUES (?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_booking_by_id(self, booking_id: int) -> Optional[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date
        FROM Booking WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        return Booking(*row) if row else None

    def read_all_bookings(self) -> List[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date
        FROM Booking
        """
        rows = self.fetchall(sql)
        return [Booking(*row) for row in rows]

    def delete_booking(self, booking_id: int) -> None:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        self.execute(sql, (booking_id,))

    def read_all_booking_overview(self) -> List[Dict]:
        sql = """
        SELECT 
            b.booking_id,
            g.first_name || ' ' || g.last_name AS guest_name,
            h.name AS hotel_name,
            r.room_number,
            b.check_in_date,
            b.check_out_date
        FROM Booking b
        JOIN Guest g ON b.guest_id = g.guest_id
        JOIN Room r ON b.room_id = r.room_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        ORDER BY b.check_in_date DESC
        """
        rows = self.fetchall(sql)
        return [
            {
                "booking_id": row[0],
                "guest_name": row[1],
                "hotel_name": row[2],
                "room_number": row[3],
                "check_in_date": row[4],
                "check_out_date": row[5],
            }
            for row in rows
        ]

    def read_all_booking_overview_as_df(self) -> pd.DataFrame:
        booking_data = self.read_all_booking_overview()
        return pd.DataFrame(booking_data)

    def get_bookings_per_room_type(self) -> List[Dict]:
        sql = """
        SELECT 
            rt.description AS room_type,
            rt.max_guests,
            COUNT(b.booking_id) AS total_bookings,
            h.name AS hotel_name,
            b.booking_id,
            g.first_name || ' ' || g.last_name AS guest_name,
            r.room_number,
            b.check_in_date,
            b.check_out_date,
            (julianday(b.check_out_date) - julianday(b.check_in_date)) AS nights_stayed
        FROM Booking b
        JOIN Guest g ON b.guest_id = g.guest_id
        JOIN Room r ON b.room_id = r.room_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        GROUP BY rt.description, h.name, b.booking_id, g.first_name, g.last_name, r.room_number, b.check_in_date, b.check_out_date
        ORDER BY rt.description, b.check_in_date DESC
        """
        rows = self.fetchall(sql)
        return [
            {
                "room_type": row[0],
                "max_guests": row[1],
                "total_bookings": row[2],
                "hotel_name": row[3],
                "booking_id": row[4],
                "guest_name": row[5],
                "room_number": row[6],
                "check_in_date": row[7],
                "check_out_date": row[8],
                "nights_stayed": int(row[9]) if row[9] else 0,
            }
            for row in rows
        ]

    def get_bookings_per_room_type_as_df(self) -> pd.DataFrame:
        data = self.get_bookings_per_room_type()
        return pd.DataFrame(data)

    def get_room_type_summary(self) -> List[Dict]:
        sql = """
        SELECT 
            rt.description AS room_type,
            rt.max_guests,
            COUNT(b.booking_id) AS total_bookings,
            COUNT(DISTINCT r.hotel_id) AS hotels_with_bookings,
            AVG(julianday(b.check_out_date) - julianday(b.check_in_date)) AS avg_nights_per_booking,
            MIN(b.check_in_date) AS first_booking_date,
            MAX(b.check_out_date) AS last_checkout_date
        FROM Room_Type rt
        LEFT JOIN Room r ON rt.type_id = r.type_id
        LEFT JOIN Booking b ON r.room_id = b.room_id
        GROUP BY rt.type_id, rt.description, rt.max_guests
        ORDER BY total_bookings DESC
        """
        rows = self.fetchall(sql)
        return [
            {
                "room_type": row[0],
                "max_guests": row[1],
                "total_bookings": row[2],
                "hotels_with_bookings": row[3],
                "avg_nights_per_booking": round(row[4], 2) if row[4] else 0,
                "first_booking_date": row[5],
                "last_checkout_date": row[6],
            }
            for row in rows
        ]

    def get_room_type_summary_as_df(self) -> pd.DataFrame:
        summary = self.get_room_type_summary()
        return pd.DataFrame(summary)
