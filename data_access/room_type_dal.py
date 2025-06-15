from data_access.base_data_access import BaseDataAccess
from model.room_type import RoomType
from model.room import Room

from typing import Optional, List

class RoomTypeDataAccess(BaseDataAccess):
    def read_all_room_types(self) -> List[RoomType]:
        sql = "SELECT type_id, description, max_guests FROM Room_Type"
        rows = self.fetchall(sql)
        room_types = []
        for type_id, description, max_guests in rows:
            room_type = RoomType(
                type_id=type_id,
                description=f"{description} room",
                max_guests=max_guests
            )
            room_types.append(room_type)
        return room_types

    def get_room_type_by_id(self, room_type_id: int) -> Optional[RoomType]:
        sql = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        row = self.fetchone(sql, (room_type_id,))
        if row:
            # Handle None or empty description
            description = row[1] if row[1] else "Standard"
            return RoomType(
                type_id=row[0],
                description=f"{description} room",
                max_guests=row[2]
            )
        return None

    def create_room_type(self, room_type: RoomType) -> int:
        sql = """
        INSERT INTO Room_Type (description, max_guests)
        VALUES (?, ?)
        """
        params = (room_type.description, room_type.max_guests)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def update_room_type(self, room_type: RoomType) -> None:
        sql = """
        UPDATE Room_Type
        SET description = ?, max_guests = ?
        WHERE type_id = ?
        """
        params = (room_type.description, room_type.max_guests, room_type.type_id)
        self.execute(sql, params)

    def delete_room_type(self, room_type_id: int) -> None:
        sql = "DELETE FROM Room_Type WHERE type_id = ?"
        self.execute(sql, (room_type_id,))

    def get_all_room_types(self) -> List[RoomType]:
        sql = "SELECT type_id, description, max_guests FROM Room_Type"
        rows = self.fetchall(sql)
        return [RoomType(type_id=row[0], description=row[1], max_guests=row[2]) for row in rows]