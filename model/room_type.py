class RoomType:
    """
    Model Class RoomType
    """

    def __init__(self, id: int, name: str, description: str, max_guests: int, price: float):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID must be a positive integer")
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string")
        if not isinstance(max_guests, int) or max_guests <= 0:
            raise ValueError("Max guests must be a positive integer")
        if not isinstance(price, float) or price < 0:
            raise ValueError("Price must be a non-negative float")

        self.__id = id
        self.__name = name
        self.__description = description
        self.__max_guests = max_guests
        self.__price = price

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string")
        self.__name = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Description must be a non-empty string")
        self.__description = value

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Max guests must be a positive integer")
        self.__max_guests = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, float) or value < 0:
            raise ValueError("Price must be a non-negative float")
        self.__price = value

    def __str__(self):
        return f"{self.__name} ({self.__max_guests} guests) – CHF {self.__price:.2f}"

