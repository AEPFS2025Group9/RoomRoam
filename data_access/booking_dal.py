# booking_dal.py

from data_access.base_data_access import BaseDataAccess
from model.booking import Booking

class BookingDataAccess(BaseDataAccess):
    def create_booking(self, booking: Booking):
        sql = "INSERT INTO Booking (GuestId, RoomId, CheckInDate, CheckOutDate) VALUES (?, ?, ?, ?)"
        params = (booking.guest_id, booking.room_id, booking.check_in_date, booking.check_out_date)
        return self.execute(sql, params)

    def cancel_booking(self, booking_id: int):
        sql = "DELETE FROM Booking WHERE BookingId = ?"
        return self.execute(sql, (booking_id,))

    def get_all_bookings(self) -> list[Booking]:
        sql = "SELECT BookingId, GuestId, RoomId, CheckInDate, CheckOutDate FROM Booking"
        return [Booking(*row) for row in self.fetchall(sql)]

