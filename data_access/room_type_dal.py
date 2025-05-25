from data_access.base_data_access import BaseDataAccess
from model.room_type import RoomType

class RoomTypeDataAccess(BaseDataAccess):
    def read_all_room_types(self) -> list[RoomType]:
        sql = "SELECT RoomTypeId, Name, Description, MaxGuests, Price FROM RoomType"
        rows = self.fetchall(sql)
        return [RoomType(id, name, description, max_guests, price)
                for id, name, description, max_guests, price in rows]

    def get_room_type_by_id(self, room_type_id: int) -> RoomType | None:
        sql = "SELECT RoomTypeId, Name, Description, MaxGuests, Price FROM RoomType WHERE RoomTypeId = ?"
        row = self.fetchone(sql, (room_type_id,))
        if row:
            return RoomType(*row)
        return None

    def create_room_type(self, room_type: RoomType) -> int:
        sql = """
        INSERT INTO RoomType (Name, Description, MaxGuests, Price)
        VALUES (?, ?, ?, ?)
        """
        params = (room_type.name, room_type.description, room_type.max_guests, room_type.price)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def update_room_type(self, room_type: RoomType) -> None:
        sql = """
        UPDATE RoomType
        SET Name = ?, Description = ?, MaxGuests = ?, Price = ?
        WHERE RoomTypeId = ?
        """
        params = (room_type.name, room_type.description, room_type.max_guests, room_type.price, room_type.room_type_id)
        self.execute(sql, params)

    def delete_room_type(self, room_type_id: int) -> None:
        sql = "DELETE FROM RoomType WHERE RoomTypeId = ?"
        self.execute(sql, (room_type_id,))
