from data_access.base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address
from typing import List

class HotelDataAccess(BaseDataAccess):
    def create_hotel(self, hotel: Hotel) -> int:
        sql = "INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)"
        # Hotel hat ein Address-Objekt mit address_id Property
        address_id = hotel.address.address_id
        params = (hotel.name, hotel.stars, address_id)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_all_hotels(self) -> List[Hotel]:
        sql = "SELECT hotel_id, name, stars, address_id FROM Hotel"
        rows = self.fetchall(sql)
        # Hier erstellen wir Hotels mit einer temporären address_id
        # Die vollständige Address wird später vom AdminManager geladen
        hotels = []
        for hotel_id, name, stars, address_id in rows:
            # Temporäres Hotel-Objekt mit Dummy-Address (mit korrekten Parametern)
            temp_address = Address(0, "temp", "1111", "temp")
            hotel = Hotel(hotel_id, name, stars, temp_address)
            # address_id als Attribut speichern für späteren Zugriff
            hotel.address_id = address_id
            hotels.append(hotel)
        return hotels

    def read_hotels_by_city(self, city: str) -> List[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, h.address_id
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE a.city = ?
        """
        rows = self.fetchall(sql, (city,))
        hotels = []
        for hotel_id, name, stars, address_id in rows:
            # Temporäres Hotel-Objekt mit Dummy-Address (mit korrekten Parametern)
            temp_address = Address(0, "temp", 1111, "temp")
            hotel = Hotel(hotel_id, name, stars, temp_address)
            # address_id als Attribut speichern für späteren Zugriff
            hotel.address_id = address_id
            hotels.append(hotel)
        return hotels

    def update_hotel(self, hotel: Hotel) -> None:
        sql = "UPDATE Hotel SET name = ?, stars = ?, address_id = ? WHERE hotel_id = ?"
        address_id = hotel.address.address_id
        params = (hotel.name, hotel.stars, address_id, hotel.hotel_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        sql = "DELETE FROM Hotel WHERE hotel_id = ?"
        self.execute(sql, (hotel_id,))