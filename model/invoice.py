class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, amount: float, issue_date, is_paid: bool = False):
        self.__invoice_id = invoice_id
        self.__booking_id = booking_id
        self.__amount = amount
        self.__issue_date = issue_date
        self.__is_paid = is_paid

    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def amount(self):
        return self.__amount

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def is_paid(self):
        return self.__is_paid

    def get_invoice_summary(self):
        return f"Invoice ID: {self.__invoice_id}, Booking ID: {self.__booking_id}, Amount: {self.__amount} CHF, Issued: {self.__issue_date}, Paid: {self.__is_paid}"
