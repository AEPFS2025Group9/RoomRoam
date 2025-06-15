class Facility:
    """
    Model Class Facility
    """

    def __init__(self, facility_id: int, facility_name: str, description: str = ""):
        if not isinstance(facility_id, int) or facility_id < 0:
            raise ValueError("ID must be a positive integer")
        if not facility_name or not isinstance(facility_name, str):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(description, str):
            raise ValueError("Description must be a string")

        self.__id = facility_id
        self.__name = facility_name
        self.__description = description

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
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self.__description = value

    def __str__(self):
        return f"{self.__name}: {self.__description}" if self.__description else self.__name
