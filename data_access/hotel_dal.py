from data_access.base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address
from typing import List

class HotelDataAccess(BaseDataAccess):
    def create_hotel(self, hotel: Hotel) -> int:
        sql = "INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)"
        params = (hotel.name, hotel.stars, hotel.address.address_id)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_all_hotels(self) -> List[Hotel]:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel"
        rows = self.fetchall(sql)
        return [Hotel(hotel_id, name, stars, address_id) for hotel_id, name, stars, address_id in rows]

    def read_hotels_by_city(self, city: str) -> List[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, h.address_id
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
        """
        rows = self.fetchall(sql, (city,))
        return [Hotel(hotel_id, name, stars, address_id) for hotel_id, name, stars, address_id in rows]

    def update_hotel(self, hotel: Hotel) -> None:
        sql = "UPDATE Hotel SET name = ?, stars = ?, address_id = ? WHERE hotel_id = ?"
        params = (hotel.name, hotel.stars, hotel.address.address_id, hotel.hotel_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        self.execute(sql, (hotel_id,))

