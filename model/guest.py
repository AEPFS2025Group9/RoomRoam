from datetime import date

class Guest:
    """
    Model Class Guest
    """

    def __init__(self, first_name: str, last_name: str, birthdate: date, nationality: str, email: str, telnr: int, address_id: int = 1):
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name must be a non-empty string")
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name must be a non-empty string")
        if not isinstance(birthdate, date):
            raise ValueError("Birthdate must be a valid date object")
        if not nationality or not isinstance(nationality, str):
            raise ValueError("Nationality must be a non-empty string")
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
        if not isinstance(telnr, int):
            raise ValueError("Telephone number must be an integer")

        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthdate = birthdate
        self.__nationality = nationality
        self.__email = email
        self.__telnr = telnr
        self.__address_id = address_id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def nationality(self):
        return self.__nationality

    @property
    def email(self):
        return self.__email

    @property
    def telnr(self):
        return self.__telnr

    @property
    def address_id(self):
        return self.__address_id

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} ({self.__nationality})"
