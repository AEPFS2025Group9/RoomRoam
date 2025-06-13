from model.facility import Facility
from model.room_type import RoomType
from datetime import datetime

class Room:
    """
    Model Class Room
    """

    def __init__(self, room_id: int, hotel_id: int, room_number: str, type_id: int, price_per_night: float):
        if not isinstance(room_id, int) or room_id < 0:
            raise ValueError("Room ID must be a positive integer")
        if not isinstance(hotel_id, int) or hotel_id < 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not room_number or not isinstance(room_number, str):
            raise ValueError("Room number must be a non-empty string")
        if not isinstance(type_id, int) or type_id < 0:
            raise ValueError("Type ID must be a positive integer")
        if not isinstance(price_per_night, (int, float)) or price_per_night < 0:
            raise ValueError("Price per night must be a positive number")

        self.__room_id = room_id
        self.__hotel_id = hotel_id
        self.__room_number = room_number
        self.__type_id = type_id
        self.__price_per_night = price_per_night

    def get_dynamic_price(self, check_in_date: str) -> float:
        """
        Calculates dynamic price based on season:
        - High season (July, August, December): +20%
        - Low season (January, February, November): -15%
        - Others: base price
        """
        try:
            month = datetime.strptime(check_in_date, "%Y-%m-%d").month
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

        if month in [7, 8, 12]:  # Hochsaison
            return round(self.price_per_night * 1.2, 2)
        elif month in [1, 2, 11]:  # Nebensaison
            return round(self.price_per_night * 0.85, 2)
        else:
            return self.price_per_night

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
    def type_id(self) -> int:
        return self.__type_id

    @type_id.setter
    def type_id(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Type ID must be a positive integer")
        self.__type_id = value

    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price per night must be a positive number")
        self.__price_per_night = value

    def __str__(self) -> str:
        return f"Room(ID: {self.__room_id}, Hotel: {self.__hotel_id}, Number: {self.__room_number}, Type: {self.__type_id}, Price: ${self.__price_per_night})"

    def __repr__(self) -> str:
        return f"Room({self.__room_id}, {self.__hotel_id}, '{self.__room_number}', {self.__type_id}, {self.__price_per_night})"
