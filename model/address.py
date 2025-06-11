class Address:
    """
    Model Class Address
    """

    def __init__(self, address_id: int, street: str, zip_code: str, city: str):

        if not isinstance(address_id, int):
            raise ValueError("Address ID must be an integer")
        if not street or not isinstance(street, str):
            raise ValueError("Street must be a non-empty string")
        if not zip_code or not isinstance(zip_code, str):
            raise ValueError("Zip code must be a non-empty string")
        if not city or not isinstance(city, str):
            raise ValueError("City must be a non-empty string")

        self.__address_id = address_id
        self.__street = street
        self.__zip_code = zip_code
        self.__city = city

    @property
    def address_id(self):
        return self.__address_id

    @address_id.setter
    def address_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Address ID must be an integer")
        self.__address_id = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Street must be a non-empty string")
        self.__street = value

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Zip code must be a non-empty string")
        self.__zip_code = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("City must be a non-empty string")
        self.__city = value

    def __str__(self):
        return f"{self.__address_id}, {self.__street}, {self.__zip_code} {self.__city}"