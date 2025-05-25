from data_access.base_data_access import BaseDataAccess
from model.facility import Facility

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> list[Facility]:
        sql = "SELECT FacilityId, Name, Description FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(facility_id, name, description) for facility_id, name, description in rows]

    def get_facility_by_id(self, facility_id: int) -> Facility | None:
        sql = "SELECT FacilityId, Name, Description FROM Facilities WHERE FacilityId = ?"
        row = self.fetchone(sql, (facility_id,))
        if row:
            return Facility(*row)
        return None

    def create_facility(self, facility: Facility) -> int:
        sql = "INSERT INTO Facilities (Name, Description) VALUES (?, ?)"
        params = (facility.name, facility.description)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def update_facility(self, facility: Facility) -> None:
        sql = "UPDATE Facilities SET Name = ?, Description = ? WHERE FacilityId = ?"
        params = (facility.name, facility.description, facility.facility_id)
        self.execute(sql, params)

    def delete_facility(self, facility_id: int) -> None:
        sql = "DELETE FROM Facilities WHERE FacilityId = ?"
        self.execute(sql, (facility_id,))