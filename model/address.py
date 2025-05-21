class Address:
    """
    Model Class Address
    """

    def __init__(self, street: str, streetnr: int, zip: int, city: str):
        if not street or not isinstance(street, str):
            raise ValueError("Street must be a non-empty string")
        if not isinstance(streetnr, int):
            raise ValueError("Street number must be an integer")
        if not isinstance(zip, int):
            raise ValueError("Zip must be an integer")
        if not city or not isinstance(city, str):
            raise ValueError("City must be a non-empty string")

        self.__street = street
        self.__streetnr = streetnr
        self.__zip = zip
        self.__city = city

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Street must be a non-empty string")
        self.__street = value

    @property
    def streetnr(self):
        return self.__streetnr

    @streetnr.setter
    def streetnr(self, value):
        if not isinstance(value, int):
            raise ValueError("Street number must be an integer")
        self.__streetnr = value

    @property
    def zip(self):
        return self.__zip

    @zip.setter
    def zip(self, value):
        if not isinstance(value, int):
            raise ValueError("Zip must be an integer")
        self.__zip = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("City must be a non-empty string")
        self.__city = value

    def __str__(self):
        return f"{self.__street} {self.__streetnr}, {self.__zip} {self.__city}"
