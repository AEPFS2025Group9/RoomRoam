# facilities_dal.py

from data_access.base_data_access import BaseDataAccess
from model.facilities import Facility

class FacilitiesDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> list[Facility]:
        sql = "SELECT FacilityId, Name FROM Facilities"
        return [Facility(*row) for row in self.fetchall(sql)]
