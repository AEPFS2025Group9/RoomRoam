from data_access.base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address  # needed if you expand read logic

class HotelDataAccess(BaseDataAccess):
    def create_hotel(self, hotel: Hotel) -> int:
        sql = "INSERT INTO Hotel (Name, Stars, AddressId) VALUES (?, ?, ?)"
        params = (hotel.name, hotel.stars, hotel.address.address_id)  # assuming address_id is stored
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_all_hotels(self) -> list[Hotel]:
        sql = "SELECT HotelId, Name, Stars, AddressId FROM Hotel"
        rows = self.fetchall(sql)
        return [Hotel(hotel_id, name, stars, address_id) for hotel_id, name, stars, address_id in rows]

    def read_hotels_by_city(self, city: str) -> list[Hotel]:
        sql = """
        SELECT h.HotelId, h.Name, h.Stars, h.AddressId
        FROM Hotel h
        JOIN Address a ON h.AddressId = a.AddressId
        WHERE a.City = ?
        """
        rows = self.fetchall(sql, (city,))
        return [Hotel(hotel_id, name, stars, address_id) for hotel_id, name, stars, address_id in rows]

    def update_hotel(self, hotel: Hotel) -> None:
        sql = "UPDATE Hotel SET Name = ?, Stars = ?, AddressId = ? WHERE HotelId = ?"
        params = (hotel.name, hotel.stars, hotel.address.address_id, hotel.hotel_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        sql = "DELETE FROM Hotel WHERE HotelId = ?"
        self.execute(sql, (hotel_id,))

