from datetime import date

class Booking:
    """
    Model Class Booking
    """

    def __init__(self, booking_id: int, guest_id: int, room_id: int, check_in_date: date, check_out_date: date):
        if not isinstance(booking_id, int) or booking_id < 0:
            raise ValueError("Booking ID must be a positive integer")
        if not isinstance(guest_id, int) or guest_id < 0:
            raise ValueError("Guest ID must be a positive integer")
        if not isinstance(room_id, int) or room_id < 0:
            raise ValueError("Room ID must be a positive integer")
        if not isinstance(check_in_date, date) or not isinstance(check_out_date, date):
            raise ValueError("Check-in and Check-out must be valid dates")
        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date")
        if not isinstance(guest_count, int) or guest_count <= 0:
            raise ValueError("Guest count must be a positive integer")

        self.__booking_id = booking_id
        self.__guest_id = guest_id
        self.__room_id = room_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def guest_id(self):
        return self.__guest_id

    @property
    def room_id(self):
        return self.__room_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    def __str__(self):
        return f"Booking[{self.__booking_id}] Guest {self.__guest_id}, Room {self.__room_id}, {self.__check_in_date} → {self.__check_out_date}"

