from facility import Facility
from room_type import RoomType  # Assuming you defined this elsewhere

class Room:
    """
    Model Class Room
    """

    def __init__(self, id: int, hotel_id: int, room_number: str, room_type: RoomType):
        if not isinstance(id, int) or id < 0:
            raise ValueError("Room ID must be a positive integer")
        if not isinstance(hotel_id, int) or hotel_id < 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not room_number or not isinstance(room_number, str):
            raise ValueError("Room number must be a non-empty string")
        if not isinstance(room_type, RoomType):
            raise ValueError("Invalid RoomType object")

        self.__id = id
        self.__hotel_id = hotel_id
        self.__room_number = room_number
        self.__room_type = room_type
        self.__facilities = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def room_number(self) -> str:
        return self.__room_number

    @room_number.setter
    def room_number(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Room number must be a non-empty string")
        self.__room_number = value

    @property
    def room_type(self) -> RoomType:
        return self.__room_type

    @room_type.setter
    def room_type(self, value: RoomType):
        if not isinstance(value, RoomType):
            raise ValueError("Invalid RoomType object")
        self.__room_type = value

    @property
    def facilities(self) -> list:
        return self.__facilities

    def add_facility(self, facility: Facility):
        if facility not in self.__facilities:
            self.__facilities.append(facility)

    def remove_facility(self, facility: Facility):
        if facility in self.__facilities:
            self.__facilities.remove(facility)

    def __str__(self):
        fac_list = ', '.join([f.name for f in self.__facilities])
        return f"Room {self.__room_number} ({self.__room_type.name}) with: {fac_list if fac_list else 'No facilities'}"

