# room_type_dal.py

from data_access.base_data_access import BaseDataAccess
from model.room_type import RoomType

class RoomTypeDataAccess(BaseDataAccess):
    def read_all_room_types(self) -> list[RoomType]:
        sql = "SELECT RoomTypeId, Name, MaxGuests, Description FROM RoomType"
        return [RoomType(*row) for row in self.fetchall(sql)]
