from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room(self, room_number: str, room_type: model.RoomType, hotel_id: int) -> model.Room:
        sql = """
        INSERT INTO Room (RoomNumber, RoomTypeId, HotelId) VALUES (?, ?, ?)
        """
        params = (room_number, room_type.room_type_id, hotel_id)
        last_row_id, _ = self.execute(sql, params)
        return model.Room(last_row_id, room_number, room_type, hotel_id)

    def read_room_by_id(self, room_id: int) -> model.Room | None:
        sql = """
        SELECT RoomId, RoomNumber, RoomTypeId, HotelId FROM Room WHERE RoomId = ?
        """
        result = self.fetchone(sql, (room_id,))
        if result:
            room_id, room_number, room_type_id, hotel_id = result
            room_type = model.RoomType(room_type_id)  # erweitern bei Bedarf
            return model.Room(room_id, room_number, room_type, hotel_id)
        else:
            return None

    def update_room(self, room_id: int, new_number: str, room_type_id: int, hotel_id: int):
        sql = """
        UPDATE Room SET RoomNumber = ?, RoomTypeId = ?, HotelId = ? WHERE RoomId = ?
        """
        self.execute(sql, (new_number, room_type_id, hotel_id, room_id))

    def delete_room(self, room_id: int):
        sql = "DELETE FROM Room WHERE RoomId = ?"
        self.execute(sql, (room_id,))
