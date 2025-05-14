from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_facility(self, name: str) -> model.Facility:
        sql = "INSERT INTO Facility (Name) VALUES (?)"
        last_row_id, _ = self.execute(sql, (name,))
        return model.Facility(last_row_id, name)

    def read_all_facilities(self) -> list[model.Facility]:
        sql = "SELECT FacilityId, Name FROM Facility"
        results = self.fetchall(sql)
        return [model.Facility(*row) for row in results]

    def update_facility(self, facility_id: int, name: str):
        sql = "UPDATE Facility SET Name = ? WHERE FacilityId = ?"
        self.execute(sql, (name, facility_id))

    def delete_facility(self, facility_id: int):
        sql = "DELETE FROM Facility WHERE FacilityId = ?"
        self.execute(sql, (facility_id,))
