import model

class BookingDataAccess(BaseDataAccess):
    def create_booking(self, booking: model.Booking) -> int:
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

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        sql = "SELECT * FROM Booking WHERE booking_id = ?"
        result = self.fetchone(sql, (booking_id,))
        if result:
            return model.Booking(*result)
        return None

    def read_all_bookings(self) -> list[model.Booking]:
        sql = "SELECT * FROM Booking"
        results = self.fetchall(sql)
        return [model.Booking(*row) for row in results]

    def delete_booking(self, booking_id: int) -> None:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        self.execute(sql, (booking_id,))

