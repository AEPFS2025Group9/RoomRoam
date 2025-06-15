from data_access.base_data_access import BaseDataAccess
from model.facility import Facility
from typing import List, Optional

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> List[Facility]:
        sql = "SELECT facility_id, facility_name, description FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(facility_id=row[0], facility_name=row[1], description=row[2]) for row in rows]

    def get_facility_by_id(self, facility_id: int) -> Optional[Facility]:
        sql = "SELECT facility_id, facility_name, description FROM Facilities WHERE facility_id = ?"
        row = self.fetchone(sql, (facility_id,))
        if row:
            return Facility(facility_id=row[0], facility_name=row[1], description=row[2])
        return None

    def create_facility(self, facility: Facility) -> int:
        sql = "INSERT INTO Facilities (facility_name, description) VALUES (?, ?)"
        params = (facility.name, facility.description)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def update_facility(self, facility: Facility) -> None:
        sql = "UPDATE Facilities SET facility_name = ?, description = ? WHERE facility_id = ?"
        params = (facility.name, facility.description, facility.id)
        self.execute(sql, params)

    def delete_facility(self, facility_id: int) -> None:
        sql = "DELETE FROM Facilities WHERE facility_id = ?"
        self.execute(sql, (facility_id,))

    def get_facilities_by_room(self, room_id: int) -> List[Facility]:
        sql = """
            SELECT f.facility_id, f.facility_name, f.description
            FROM Facilities f
            JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
            WHERE rf.room_id = ?
        """
        rows = self.fetchall(sql, (room_id,))
        return [Facility(facility_id=row[0], facility_name=row[1], description=row[2]) for row in rows]

    def get_all_facilities(self) -> List[Facility]:
        sql = "SELECT facility_id, facility_name, description FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(facility_id=row[0], facility_name=row[1], description=row[2]) for row in rows]
