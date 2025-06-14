from data_access.invoice_dal import InvoiceDataAccess
from data_access.booking_dal import BookingDataAccess
from data_access.room_dal import RoomDataAccess
from data_access.guest_dal import GuestDataAccess
from model.invoice import Invoice
from model.booking import Booking
from datetime import date
from typing import Optional, Dict

class InvoiceManager:
    def __init__(self):
        self.invoice_dal = InvoiceDataAccess()
        self.booking_dal = BookingDataAccess()
        self.room_dal = RoomDataAccess()
        self.guest_dal = GuestDataAccess()

    def generate_invoice_for_booking(self, booking_id: int) -> int:


        booking = self.booking_dal.read_booking_by_id(booking_id)
        if not booking:
            raise ValueError(f"Booking with ID {booking_id} not found")


        existing_invoice = self.invoice_dal.get_invoice_by_booking_id(booking_id)
        if existing_invoice:
            return existing_invoice.invoice_id


        room = self.room_dal.get_room_by_id(booking.room_id)
        if not room:
            raise ValueError(f"Room with ID {booking.room_id} not found")


        nights = booking.calculate_nights()
        total_amount = float(nights * room.price)


        invoice = Invoice(
            invoice_id=0,
            booking_id=booking_id,
            issue_date=date.today(),
            total_amount=total_amount,
            is_paid=False
        )


        invoice_id = self.invoice_dal.create_invoice(invoice)
        return invoice_id

    def get_invoice_for_guest(self, guest_id: int, booking_id: int) -> Optional[Invoice]:


        booking = self.booking_dal.read_booking_by_id(booking_id)
        if not booking or booking.guest_id != guest_id:
            return None

        return self.invoice_dal.get_invoice_by_booking_id(booking_id)

    def get_invoice_details(self, invoice_id: int) -> Optional[Dict]:

        invoice = self.invoice_dal.read_invoice_by_id(invoice_id)
        if not invoice:
            return None


        booking = self.booking_dal.read_booking_by_id(invoice.booking_id)
        if not booking:
            return None


        guest = self.guest_dal.read_guest_by_id(booking.guest_id)
        if not guest:
            return None


        room = self.room_dal.get_room_by_id(booking.room_id)
        if not room:
            return None


        nights = booking.calculate_nights()

        return {
            "invoice_id": invoice.invoice_id,
            "issue_date": invoice.issiu_date,
            "total_amount": invoice.total_amount,
            "is_paid": invoice.is_paid,
            "guest_name": f"{guest.first_name} {guest.last_name}",
            "guest_email": guest.email,
            "room_number": room.room_number,
            "room_price_per_night": room.price,
            "check_in_date": booking.check_in_date,
            "check_out_date": booking.check_out_date,
            "nights_stayed": nights,
            "guest_count": booking.guest_count
        }

    def mark_invoice_as_paid(self, invoice_id: int) -> bool:

        try:
            self.invoice_dal.mark_invoice_as_paid(invoice_id)
            return True
        except Exception:
            return False

    def generate_reservation_invoice(self, booking_id: int) -> int:

        return self.generate_invoice_for_booking(booking_id)