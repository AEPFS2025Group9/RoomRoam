from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class RoomFacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def add_facility_to_room(self, room_id: int, facility_id: int):
        sql = "INSERT INTO RoomFacility (RoomId, FacilityId) VALUES (?, ?)"
        self.execute(sql, (room_id, facility_id))

    def read_facilities_by_room(self, room_id: int) -> list[model.Facility]:
        sql = """
        SELECT f.FacilityId, f.Name
        FROM Facility f
        JOIN RoomFacility rf ON f.FacilityId = rf.FacilityId
        WHERE rf.RoomId = ?
        """
        results = self.fetchall(sql, (room_id,))
        return [model.Facility(*row) for row in results]

    def remove_facility_from_room(self, room_id: int, facility_id: int):
        sql = "DELETE FROM RoomFacility WHERE RoomId = ? AND FacilityId = ?"
        self.execute(sql, (room_id, facility_id))
