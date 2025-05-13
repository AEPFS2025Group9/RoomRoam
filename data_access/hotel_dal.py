# hotel_dal.py

from data_access.base_data_access import BaseDataAccess
from model.hotel import Hotel

class HotelDataAccess(BaseDataAccess):
    def read_all_hotels(self) -> list[Hotel]:
        sql = "SELECT HotelId, Name, Stars, AddressId FROM Hotel"
        rows = self.fetchall(sql)
        return [Hotel(*row) for row in rows]

    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        sql = """
        SELECT h.HotelId, h.Name, h.Stars, h.AddressId
        FROM Hotel h
        JOIN Address a ON h.AddressId = a.AddressId
        WHERE a.City = ?
        """
        return [Hotel(*row) for row in self.fetchall(sql, (city,))]

    def create_hotel(self, hotel: Hotel):
        sql = "INSERT INTO Hotel (Name, Stars, AddressId) VALUES (?, ?, ?)"
        params = (hotel.name, hotel.stars, hotel.address_id)
        return self.execute(sql, params)

    def update_hotel(self, hotel: Hotel):
        sql = "UPDATE Hotel SET Name = ?, Stars = ?, AddressId = ? WHERE HotelId = ?"
        params = (hotel.name, hotel.stars, hotel.address_id, hotel.hotel_id)
        return self.execute(sql, params)

    def delete_hotel(self, hotel_id: int):
        sql = "DELETE FROM Hotel WHERE HotelId = ?"
        return self.execute(sql, (hotel_id,))
