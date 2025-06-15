from datetime import date, datetime

class Guest:
    """
    Model Class Guest
    """

    def __init__(self, first_name: str, last_name: str, birthdate, nationality: str, email: str, telnr: str,
                 address_id: int = 1, guest_id: int = None):
        self.__guest_id = guest_id
        if not first_name or not isinstance(first_name, str):
            raise ValueError("First name must be a non-empty string")
        if not last_name or not isinstance(last_name, str):
            raise ValueError("Last name must be a non-empty string")
        self.__birthdate = self._validate_birthdate(birthdate)
        if not nationality or not isinstance(nationality, str):
            raise ValueError("Nationality must be a non-empty string")
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
        if not telnr or not isinstance(telnr, str) or not telnr.isdigit():
            raise ValueError("Telephone number must be a numeric string")

        self.__first_name = first_name
        self.__last_name = last_name
        self.__nationality = nationality
        self.__email = email
        self.__telnr = telnr
        self.__address_id = address_id

    def _validate_birthdate(self, birthdate):
        if isinstance(birthdate, date):
            return birthdate
        if isinstance(birthdate, str):
            try:
                return datetime.strptime(birthdate, "%d.%m.%Y").date()
            except ValueError:
                raise ValueError("Birthdate string must be in format DD.MM.YYYY")
        raise ValueError("Birthdate must be a valid date object or a properly formatted string")

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

    @property
    def guest_id(self):
        return self.__guest_id

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} ({self.__nationality})"
