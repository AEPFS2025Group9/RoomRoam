from data_access.base_data_access import BaseDataAccess
from model.facility import Facility
from typing import List, Optional

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> List[Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(id=row[0], name=row[1]) for row in rows]

    def get_facility_by_id(self, facility_id: int) -> Optional[Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities WHERE facility_id = ?"
        row = self.fetchone(sql, (facility_id,))
        if row:
            return Facility(id=row[0], name=row[1])
        return None

    def create_facility(self, facility: Facility) -> int:
        sql = "INSERT INTO Facilities (facility_name) VALUES (?)"
        params = (facility.name,)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def update_facility(self, facility: Facility) -> None:
        sql = "UPDATE Facilities SET facility_name = ? WHERE facility_id = ?"
        params = (facility.name, facility.id)
        self.execute(sql, params)

    def delete_facility(self, facility_id: int) -> None:
        sql = "DELETE FROM Facilities WHERE facility_id = ?"
        self.execute(sql, (facility_id,))
