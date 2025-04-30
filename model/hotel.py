class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address

    @property
    def hotel_id(self):
        return self.__hotel_id
        if hotel_id < 0:
            raise ValueError("Hotel ID must be greater than 0")
        return self.__hotel_id

    @property
    def name(self):
        return self.__name
        if self.__name == "":
            raise ValueError("Name cannot be empty")
        return self.__name

    @property
    def stars(self):
        return self.__stars
        if self.__stars 1 =< self.__stars <= 5:
            raise ValueError("Stars must be between 1 and 5")
        return self.__stars

    @property
    def address(self):
        return self.__address
        if self.__address == "":
            raise ValueError("Address cannot be empty")
        return self.__address

    def __str__(self):
        return (
            f"Hotel[{self.__hotel_id}] {self.__name} - {self.__stars} Sterne\n"
            f"Adresse: {self.__address}"
        )

