from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room_type(self, name: str, max_guests: int, price: float, description: str) -> model.RoomType:
        sql = """
        INSERT INTO RoomType (Name, MaxGuests, Price, Description) VALUES (?, ?, ?, ?)
        """
        params = (name, max_guests, price, description)
        last_row_id, _ = self.execute(sql, params)
        return model.RoomType(last_row_id, name, max_guests, price, description)

    def read_room_type_by_id(self, room_type_id: int) -> model.RoomType | None:
        sql = "SELECT RoomTypeId, Name, MaxGuests, Price, Description FROM RoomType WHERE RoomTypeId = ?"
        result = self.fetchone(sql, (room_type_id,))
        if result:
            return model.RoomType(*result)
        return None

    def update_room_type(self, room_type_id: int, name: str, max_guests: int, price: float, description: str):
        sql = """
        UPDATE RoomType SET Name = ?, MaxGuests = ?, Price = ?, Description = ? WHERE RoomTypeId = ?
        """
        self.execute(sql, (name, max_guests, price, description, room_type_id))

    def delete_room_type(self, room_type_id: int):
        sql = "DELETE FROM RoomType WHERE RoomTypeId = ?"
        self.execute(sql, (room_type_id,))
