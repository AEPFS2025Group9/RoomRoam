from model.facility import Facility
from model.room_type import RoomType

class Room:
    """
    Model Class Room
    """

    def __init__(self, room_id: int, hotel_id: int, room_number: str, type_id: RoomType, price_per_night: float):
        if not isinstance(room_id, int) or room_id < 0:
            raise ValueError("Room ID must be a positive integer")
        if not isinstance(hotel_id, int) or hotel_id < 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not room_number or not isinstance(room_number, str):
            raise ValueError("Room number must be a non-empty string")
        if not isinstance(type_id, RoomType):
            raise ValueError("Invalid RoomType object")
        if not isinstance(price_per_night, (int, float)) or price_per_night < 0:
            raise ValueError("Price per night must be a positive number")
        
        self.__room_id = room_id
        self.__hotel_id = hotel_id
        self.__room_number = room_number
        self.__type_id = type_id
        self.__price_per_night = price_per_night

    @property
    def room_id(self) -> int:
        return self.__room_id

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
    def type_id(self) -> RoomType:
        return self.__type_id

    @type_id.setter
    def type_id(self, value: RoomType):
        if not isinstance(value, RoomType):
            raise ValueError("Invalid RoomType object")
        self.__type_id = value

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night