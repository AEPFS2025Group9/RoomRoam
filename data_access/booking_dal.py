from data_access.base_data_access import BaseDataAccess
from model.booking import Booking
from typing import List, Dict, Optional

class BookingDataAccess(BaseDataAccess):
    def create_booking(self, booking: Booking) -> int:
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_all_bookings(self) -> List[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date
        FROM Booking WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        return Booking(*row) if row else None

    def read_all_booking_overview(self) -> List[Dict]:
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
            b.check_out_date,
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
