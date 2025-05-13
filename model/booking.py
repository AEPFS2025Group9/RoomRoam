class Booking:
    def __init__(self, booking_id: int, guest_id: int, room_id: int, check_in_date, check_out_date, guest_count: int):
        self.__booking_id = booking_id
        self.__guest_id = guest_id
        self.__room_id = room_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__guest_count = guest_count

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

    @property
    def guest_count(self):
        return self.__guest_count

    def get_booking_summary(self):
        return f"Booking ID: {self.__booking_id}, Guest ID: {self.__guest_id}, Room ID: {self.__room_id}, From: {self.__check_in_date}, To: {self.__check_out_date}, Guests: {self.__guest_count}"
