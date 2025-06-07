from data_access.base_data_access import BaseDataAccess
from model.facility import Facility
from typing import List, Dict, Optional

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> List[Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(facility_id=facility_id, facility_name=name) for facility_id, name in rows]

    def get_facility_by_id(self, facility_id: int) -> Optional[Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities WHERE facility_id = ?"
        row = self.fetchone(sql, (facility_id,))
        if row:
            return Facility(*row)
        return None

    def create_facility(self, facility: Facility) -> int:
        sql = "INSERT INTO Facilities (facility_name) VALUES (?)"
        params = (facility.facility_name,)
        result = self.execute(sql, params)
        if isinstance(result, tuple):
            return result[0]
        else:
            return result

    def update_facility(self, facility: Facility) -> None:
        sql = "UPDATE Facilities SET facility_name = ? WHERE facility_id = ?"
        params = (facility.facility_name, facility.facility_id)
        self.execute(sql, params)

    def delete_facility(self, facility_id: int) -> None:
        sql = "DELETE FROM Facilities WHERE facility_id = ?"
        self.execute(sql, (facility_id,))