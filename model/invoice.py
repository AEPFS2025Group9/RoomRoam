from datetime import date

class Invoice:
    """
    Model Class Invoice
    """

    def __init__(self, invoice_id: int, booking_id: int, amount: float, issue_date: date, is_paid: bool = False):
        if not isinstance(invoice_id, int) or invoice_id < 0:
            raise ValueError("Invoice ID must be a positive integer")
        if not isinstance(booking_id, int) or booking_id < 0:
            raise ValueError("Booking ID must be a positive integer")
        if not isinstance(amount, float) or amount < 0:
            raise ValueError("Amount must be a non-negative float")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date must be a valid date")
        if not isinstance(is_paid, bool):
            raise ValueError("is_paid must be a boolean")

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

    def __str__(self):
        status = "Paid" if self.__is_paid else "Unpaid"
        return f"Invoice[{self.__invoice_id}] Booking {self.__booking_id}, {self.__amount:.2f} CHF, Issued {self.__issue_date}, Status: {status}"

