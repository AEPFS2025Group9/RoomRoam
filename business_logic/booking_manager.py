from data_access.guest_dal import GuestDataAccess
from data_access.booking_dal import BookingDataAccess
from data_access.invoice_dal import InvoiceDataAccess
from data_access.room_dal import RoomDataAccess
from model.guest import Guest
from model.booking import Booking
from model.invoice import Invoice
from datetime import date
from typing import Optional


class BookingManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()
        self.invoice_dal = InvoiceDataAccess()
        self.guest_dal = GuestDataAccess()
        self.room_dal = RoomDataAccess()

    def book_room(self, guest: Guest, room_id: int, check_in: date, check_out: date, guest_count: int) -> tuple[int, int]:
        """Gast speichern, Buchung + Rechnung anlegen"""
        # 1. Gast suchen oder neu anlegen
        existing_guest = self.guest_dal.get_guest_by_email(guest.email)
        guest_id = existing_guest.guest_id if existing_guest else self.guest_dal.create_guest(guest)

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

        # 3. Dynamische Preisberechnung
        nights = (check_out - check_in).days
        room = self.room_dal.get_room_by_id(room_id)
        dynamic_price = room.get_dynamic_price(check_in)
        amount = round(nights * dynamic_price, 2)

        # 4. Rechnung erstellen
        invoice = Invoice(
            invoice_id=None,
            booking_id=booking_id,
            total_amount=amount,
            issue_date=date.today(),
            is_paid=False
        )

        invoice_id = self.invoice_dal.create_invoice(invoice)

        return booking_id, invoice_id

    def make_reservation(self, guest: Guest, room_id: int, check_in: date, check_out: date, guest_count: int) -> dict:
        """Komplette Reservierung inkl. Nachricht"""
        booking_id, invoice_id = self.book_room(guest, room_id, check_in, check_out, guest_count)
        invoice = self.invoice_dal.get_invoice_by_id(invoice_id)

        return {
            "booking_id": booking_id,
            "invoice_id": invoice_id,
            "invoice_details": invoice,
            "message": "Reservation confirmed! Invoice generated as payment confirmation."
        }

    def cancel_booking(self, booking_id: int):
        """Buchung + zugehörige Rechnung löschen"""
        try:
            invoice = self.invoice_dal.get_invoice_by_booking_id(booking_id)
            if invoice:
                self.invoice_dal.delete_invoice(invoice.invoice_id)
        except Exception:
            pass
        self.booking_dal.delete_booking(booking_id)

    def get_guest_invoice(self, guest_id: int, booking_id: int) -> Optional[Invoice]:
        """Rechnung für Gast abrufen (nach Gast- und Buchungs-ID)"""
        invoice = self.invoice_dal.get_invoice_by_booking_id(booking_id)
        if invoice and invoice.booking_id == booking_id:
            return invoice
        return None

    def get_invoice_details_for_display(self, invoice_id: int) -> Optional[Invoice]:
        """Rechnungsdetails abrufen"""
        return self.invoice_dal.get_invoice_by_id(invoice_id)

    def get_invoice_by_booking(self, booking_id: int) -> Optional[Invoice]:
        """Rechnung per Buchungs-ID abrufen"""
        return self.invoice_dal.get_invoice_by_booking_id(booking_id)

