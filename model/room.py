from models.room_type import RoomType
from models.facility import Facility

class Room:
    """
    Model Class Room
    """

    def __init__(self, id: int, hotel_id: int, room_number: str, room_type: RoomType):
        self._id = id
        self._hotel_id = hotel_id
        self._room_number = room_number
        self._room_type = room_type
        self._facilities = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def hotel_id(self) -> int:
        return self._hotel_id

    @property
    def room_number(self) -> str:
        return self._room_number

    @property
    def room_type(self) -> RoomType:
        return self._room_type

    @property
    def facilities(self) -> list:
        return self._facilities

    def add_facility(self, facility: Facility):
        if facility not in self._facilities:
            self._facilities.append(facility)

    def remove_facility(self, facility: Facility):
        if facility in self._facilities:
            self._facilities.remove(facility)

    def __str__(self):
        fac_names = ', '.join([f.name for f in self._facilities])
        return f"Room {self._room_number} ({self._room_type.name}) with: {fac_names}"
