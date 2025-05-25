from data_access.base_data_access import BaseDataAccess

class RoomFacilityDataAccess(BaseDataAccess):
    def get_facilities_by_room(self, room_id: int) -> list[int]:
        """
        Gibt eine Liste aller FacilityIds zurück, die einem bestimmten Zimmer zugeordnet sind.
        """
        sql = "SELECT FacilityId FROM Room_Facility WHERE RoomId = ?"
        rows = self.fetchall(sql, (room_id,))
        return [row[0] for row in rows]

    def add_facility_to_room(self, room_id: int, facility_id: int) -> None:
        """
        Verknüpft eine Einrichtung mit einem Zimmer.
        """
        sql = "INSERT INTO Room_Facility (RoomId, FacilityId) VALUES (?, ?)"
        self.execute(sql, (room_id, facility_id))

    def remove_facility_from_room(self, room_id: int, facility_id: int) -> None:
        """
        Entfernt die Verknüpfung einer Einrichtung von einem Zimmer.
        """
        sql = "DELETE FROM Room_Facility WHERE RoomId = ? AND FacilityId = ?"
        self.execute(sql, (room_id, facility_id))
