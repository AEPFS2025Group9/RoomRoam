from data_access.base_data_access import BaseDataAccess
from typing import List

class RoomFacilityDataAccess(BaseDataAccess):
    def get_facilities_by_room(self, room_id: int) -> List[int]:
        """
        Gibt eine Liste aller Facility-IDs zurück, die einem bestimmten Zimmer zugeordnet sind.
        """
        sql = "SELECT facility_id FROM Room_Facilities WHERE room_id = ?"
        rows = self.fetchall(sql, (room_id,))
        return [row[0] for row in rows]

    def add_facility_to_room(self, room_id: int, facility_id: int) -> None:
        """
        Verknüpft eine Ausstattung mit einem Zimmer.
        """
        sql = "INSERT INTO Room_Facilities (room_id, facility_id) VALUES (?, ?)"
        self.execute(sql, (room_id, facility_id))

    def remove_facility_from_room(self, room_id: int, facility_id: int) -> None:
        """
        Entfernt die Verknüpfung einer Ausstattung von einem Zimmer.
        """
        sql = "DELETE FROM Room_Facilities WHERE room_id = ? AND facility_id = ?"
        self.execute(sql, (room_id, facility_id))
