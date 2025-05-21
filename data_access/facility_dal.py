from data_access.base_data_access import BaseDataAccess
from model.facility import Facility

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> list[Facility]:
        sql = "SELECT FacilityId, Name, Description FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(facility_id, name, description) for facility_id, name, description in rows]
