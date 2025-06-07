from model.address import Address

class Hotel:
    """
    Model Class Hotel
    """

    def __init__(self, hotel_id: int, name: str, stars: int, address: Address):
        if not isinstance(hotel_id, int) or hotel_id < 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        if not isinstance(address, Address):
            raise ValueError("Invalid address object")

        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address

    @property
    def hotel_id(self):
        return self.__hotel_id  # read-only

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self.__name = value

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Stars must be between 1 and 5")
        self.__stars = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise ValueError("Invalid address object")
        self.__address = value

    def __str__(self):
        return f"Hotel[{self.__hotel_id}] {self.__name} - {self.__stars} Stars\nAddress: {self.__address}"


