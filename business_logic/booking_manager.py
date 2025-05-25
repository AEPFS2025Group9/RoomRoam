from data_access.guest_dal import GuestDataAccess
from data_access.booking_dal import BookingDataAccess
from data_access.invoice_dal import InvoiceDataAccess
from data_access.room_dal import RoomDataAccess
from model.guest import Guest
from model.booking import Booking
from model.invoice import Invoice
from datetime import date

class BookingManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()
        self.invoice_dal = InvoiceDataAccess()
        self.guest_dal = GuestDataAccess()

    def book_room(self, guest: Guest, room_id: int, check_in: date, check_out: date, guest_count: int) -> int:
        # 1. Gast speichern oder finden
        existing_guest = self.guest_dal.get_guest_by_email(guest.email)
        if existing_guest:
            guest_id = existing_guest.guest_id
        else:
            guest_id = self.guest_dal.create_guest(guest)

        # 2. Buchung erstellen
        booking = Booking(
            booking_id=None,
            guest_id=guest_id,
            room_id=room_id,
            check_in_date=check_in,
            check_out_date=check_out,
            guest_count=guest_count
        )
        booking_id = self.booking_dal.create_booking(booking)

        # 3. Rechnung erzeugen (Preis = Tage * Zimmerpreis)
        nights = (check_out - check_in).days
        room = RoomDataAccess().get_room_by_id(room_id)
        amount = nights * room.price
        invoice = Invoice(
            invoice_id=None,
            booking_id=booking_id,
            amount=amount,
            issue_date=date.today(),
            is_paid=False
        )
        self.invoice_dal.create_invoice(invoice)

        return booking_id

    def cancel_booking(self, booking_id: int):
        # Rechnung löschen (wenn vorhanden)
        invoice = self.invoice_dal.get_invoice_by_booking_id(booking_id)
        if invoice:
            self.invoice_dal.delete_invoice(invoice.invoice_id)

        # Buchung löschen
        self.booking_dal.delete_booking(booking_id)
