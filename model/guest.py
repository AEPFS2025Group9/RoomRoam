from datetime import date

class Guest:
    """
    Model Class Guest
    """

    def __init__(self, firstname: str, lastname: str, birthdate: date, nationality: str, email: str, telnr: int):
        if not firstname or not isinstance(firstname, str):
            raise ValueError("First name must be a non-empty string")
        if not lastname or not isinstance(lastname, str):
            raise ValueError("Last name must be a non-empty string")
        if not isinstance(birthdate, date):
            raise ValueError("Birthdate must be a valid date object")
        if not nationality or not isinstance(nationality, str):
            raise ValueError("Nationality must be a non-empty string")
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
        if not isinstance(telnr, int):
            raise ValueError("Telephone number must be an integer")

        self.__firstname = firstname
        self.__lastname = lastname
        self.__birthdate = birthdate
        self.__nationality = nationality
        self.__email = email
        self.__telnr = telnr

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

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

    def __str__(self):
        return f"{self.__firstname} {self.__lastname} ({self.__nationality})"
