from data_access.guest_dal import GuestDataAccess
from data_access.booking_dal import BookingDataAccess
from data_access.room_dal import RoomDataAccess
from business_logic.invoice_manager import InvoiceManager
from model.guest import Guest
from model.booking import Booking
from datetime import date


class BookingManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()
        self.guest_dal = GuestDataAccess()
        self.room_dal = RoomDataAccess()
        self.invoice_manager = InvoiceManager()

    def book_room(self, guest: Guest, room_id: int, check_in: date, check_out: date, guest_count: int) -> tuple[
        int, int]:

        existing_guest = self.guest_dal.get_guest_by_email(guest.email)
        if existing_guest:
            guest_id = existing_guest.guest_id
        else:
            guest_id = self.guest_dal.create_guest(guest)


        booking = Booking(
            booking_id=None,
            guest_id=guest_id,
            room_id=room_id,
            check_in_date=check_in,
            check_out_date=check_out,
            guest_count=guest_count
        )
        booking_id = self.booking_dal.create_booking(booking)


        invoice_id = self.invoice_manager.generate_reservation_invoice(booking_id)

        return booking_id, invoice_id

    def make_reservation(self, guest: Guest, room_id: int, check_in: date, check_out: date, guest_count: int) -> dict:

        booking_id, invoice_id = self.book_room(guest, room_id, check_in, check_out, guest_count)


        invoice_details = self.get_invoice_details_for_display(invoice_id)

        return {
            "booking_id": booking_id,
            "invoice_id": invoice_id,
            "invoice_details": invoice_details,
            "message": "Reservation confirmed! Invoice generated as payment confirmation."
        }

    def cancel_booking(self, booking_id: int):

        try:
            invoice = self.invoice_manager.invoice_dal.get_invoice_by_booking_id(booking_id)
            if invoice:
                self.invoice_manager.invoice_dal.delete_invoice(invoice.invoice_id)
        except Exception:
            pass
        self.booking_dal.delete_booking(booking_id)

    def get_guest_invoice(self, guest_id: int, booking_id: int):

        return self.invoice_manager.get_invoice_for_guest(guest_id, booking_id)

    def get_invoice_details_for_display(self, invoice_id: int):

        return self.invoice_manager.get_invoice_details(invoice_id)
