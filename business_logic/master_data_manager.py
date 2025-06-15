from data_access.room_type_dal import RoomTypeDataAccess
from data_access.facility_dal import FacilityDataAccess
from data_access.room_dal import RoomDataAccess
from model.room_type import RoomType
from model.facility import Facility

class MasterDataManager:
    def __init__(self):
        self.room_type_dal = RoomTypeDataAccess()
        self.facility_dal = FacilityDataAccess()
        self.room_dal = RoomDataAccess()


    def create_room_type(self, room_type: RoomType) -> int:
        return self.room_type_dal.create_room_type(room_type)

    def update_room_type(self, room_type: RoomType):
        return self.room_type_dal.update_room_type(room_type)

    def delete_room_type(self, room_type_id: int):
        return self.room_type_dal.delete_room_type(room_type_id)


    def create_facility(self, facility: Facility) -> int:
        return self.facility_dal.create_facility(facility)

    def update_facility(self, facility: Facility):
        return self.facility_dal.update_facility(facility)

    def delete_facility(self, facility_id: int):
        return self.facility_dal.delete_facility(facility_id)


    def update_room_price(self, room_id: int, new_price: float):
        return self.room_dal.update_room_price(room_id, new_price)

