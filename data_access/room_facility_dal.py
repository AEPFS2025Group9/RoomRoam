# room_facility_dal.py

from data_access.base_data_access import BaseDataAccess

class RoomFacilityDataAccess(BaseDataAccess):
    def get_facilities_by_room(self, room_id: int) -> list[int]:
        sql = "SELECT FacilityId FROM Room_Facility WHERE RoomId = ?"
        rows = self.fetchall(sql, (room_id,))
        return [r[0] for r in rows]

    def add_facility_to_room(self, room_id: int, facility_id: int):
        sql = "INSERT INTO Room_Facility (RoomId, FacilityId) VALUES (?, ?)"
        return self.execute(sql, (room_id, facility_id))
