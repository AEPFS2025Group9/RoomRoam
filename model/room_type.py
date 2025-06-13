class RoomType:
    """
    Model Class RoomType
    """

    def __init__(self, type_id: int, description: str, max_guests: int):
        if not isinstance(type_id, int) or type_id < 0:
            raise ValueError("ID must be a positive integer")
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string")
        if not isinstance(max_guests, int) or max_guests <= 0:
            raise ValueError("Max guests must be a positive integer")

        self.__type_id = type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def type_id(self) -> int:
        return self.__type_id

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

    def __str__(self):
        return f"{self.__description} ({self.__max_guests} guests)"
