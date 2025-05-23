from data_access.base_data_access import BaseDataAccess
from model.room import Room
from model.room_type import RoomType  # assumed needed to build Room properly

class RoomDataAccess(BaseDataAccess):
    def get_rooms_by_hotel(self, hotel_id: int) -> list[Room]:
        sql = """
        SELECT RoomId, HotelId, RoomNumber, RoomTypeId
        FROM Room WHERE HotelId = ?
        """
        rows = self.fetchall(sql, (hotel_id,))
        return [Room(*row) for row in rows]

    def get_available_rooms(self, hotel_id: int, start_date, end_date) -> list[Room]:
        sql = """
        SELECT r.RoomId, r.HotelId, r.RoomNumber, r.RoomTypeId
        FROM Room r
        WHERE r.HotelId = ?
          AND r.RoomId NOT IN (
              SELECT b.RoomId FROM Booking b
              WHERE NOT (b.CheckOutDate <= ? OR b.CheckInDate >= ?)
          )
        """
        rows = self.fetchall(sql, (hotel_id, start_date, end_date))
        return [Room(*row) for row in rows]

    def update_room_price(self, room_id: int, new_price: float) -> None:
        sql = "UPDATE Room SET Price = ? WHERE RoomId = ?"
        self.execute(sql, (new_price, room_id))

