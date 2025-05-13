# room_dal.py

from data_access.base_data_access import BaseDataAccess
from model.room import Room

class RoomDataAccess(BaseDataAccess):
    def get_rooms_by_hotel(self, hotel_id: int) -> list[Room]:
        sql = "SELECT RoomId, HotelId, RoomTypeId, Price FROM Room WHERE HotelId = ?"
        return [Room(*row) for row in self.fetchall(sql, (hotel_id,))]

    def get_available_rooms(self, hotel_id: int, start_date, end_date) -> list[Room]:
        sql = """
        SELECT r.RoomId, r.HotelId, r.RoomTypeId, r.Price
        FROM Room r
        WHERE r.HotelId = ?
          AND r.RoomId NOT IN (
              SELECT b.RoomId FROM Booking b
              WHERE NOT (b.CheckOutDate <= ? OR b.CheckInDate >= ?)
          )
        """
        return [Room(*row) for row in self.fetchall(sql, (hotel_id, start_date, end_date))]

    def update_room_price(self, room_id: int, new_price: float):
        sql = "UPDATE Room SET Price = ? WHERE RoomId = ?"
        return self.execute(sql, (new_price, room_id))

