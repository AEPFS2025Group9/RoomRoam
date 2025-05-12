class RoomFacility:
    """
    Model Class RoomFacility
    """
    def __init__(self, room_id: int, facility_id: int):
        self._room_id = room_id
        self._facility_id = facility_id

    @property
    def room_id(self) -> int:
        return self._room_id

    @property
    def facility_id(self) -> int:
        return self._facility_id
