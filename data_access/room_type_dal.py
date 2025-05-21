from data_access.base_data_access import BaseDataAccess
from model.room_type import RoomType

class RoomTypeDataAccess(BaseDataAccess):
    def read_all_room_types(self) -> list[RoomType]:
        sql = "SELECT RoomTypeId, Name, Description, MaxGuests, Price FROM RoomType"
        rows = self.fetchall(sql)
        return [RoomType(id, name, description, max_guests, price)
                for id, name, description, max_guests, price in rows]

