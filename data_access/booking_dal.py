from data_access.base_data_access import BaseDataAccess
from model.booking import Booking

class BookingDataAccess(BaseDataAccess):
    def create_booking(self, booking: Booking) -> int:
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, guest_count)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            booking.guest_count
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, guest_count
        FROM Booking WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        return Booking(*row) if row else None

    def read_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, guest_count
        FROM Booking
        """
        rows = self.fetchall(sql)
        return [Booking(*row) for row in rows]

    def delete_booking(self, booking_id: int) -> None:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        self.execute(sql, (booking_id,))


