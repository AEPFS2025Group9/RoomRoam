class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address):
        if hotel_id < 0:
            raise ValueError("Hotel ID must be greater than 0")
        if not name:
            raise ValueError("Name cannot be empty")
        if stars < 1 or stars > 5:
            raise ValueError("Stars must be between 1 and 5")
        if not address:
            raise ValueError("Address cannot be empty")

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
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        if value < 1 or value > 5:
            raise ValueError("Stars must be between 1 and 5")
        self.__stars = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not value:
            raise ValueError("Address cannot be empty")
        self.__address = value

    def __str__(self):
        return (
            f"Hotel[{self.__hotel_id}] {self.__name} - {self.__stars} Sterne\n"
            f"Adresse: {self.__address}"
        )


