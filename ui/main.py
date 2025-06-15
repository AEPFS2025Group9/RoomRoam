from business_logic.admin_manager import AdminManager
from business_logic.booking_manager import BookingManager
from business_logic.search_manager import SearchManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.review_manager import ReviewManager
from business_logic.master_data_manager import MasterDataManager
from model.guest import Guest
from datetime import datetime, date

# Instantiate managers
admin = AdminManager()
booking = BookingManager()
search = SearchManager()
invoice = InvoiceManager()
review = ReviewManager()
master = MasterDataManager()

def print_header():
    print("#" * 50)
    print("#" + " " * 11 + "Welcome to your Reservation Manager" + " " * 11 + "#")
    print("#" * 50)

def main_menu():
    while True:
        print_header()
        print("\nMain Menu:")
        print("1. Guest Actions")
        print("2. Admin Actions")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            guest_menu()
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            print("\nThank you for using Reservation Manager. Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter a number from 1 to 3.")

def guest_menu():
    while True:
        print("\n--- Guest Actions ---")
        print("1. Search Hotels by City")
        print("2. Search Hotels by Minimum Stars")
        print("3. Search Hotels by Guest Capacity")
        print("4. Search Hotels by Availability Dates")
        print("5. Search Hotels with Combined Filters")
        print("6. View Invoice by Booking ID")
        print("7. Cancel a Booking")
        print("8. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice in {"1", "2", "3", "4", "5"}:
            hotel_results = search_hotels_flow(choice)
            if hotel_results:
                handle_hotel_results(hotel_results)
        elif choice == "6":
            view_invoice_flow()
        elif choice == "7":
            cancel_booking_flow()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

def search_hotels_flow(choice):
    try:
        if choice == "1":
            city = input("\nEnter city name: ").strip()
            return [h for h in admin.get_all_hotels() if city.lower() in h.address.city.lower()]
        elif choice == "2":
            stars = int(input("\nEnter minimum star rating (1-5): ").strip())
            return admin.get_hotels_by_stars(min_stars=stars)
        elif choice == "3":
            guests = int(input("\nEnter number of guests: ").strip())
            return search.search_hotels("", 1, guests, date.today(), date.today())
        elif choice == "4":
            checkin = datetime.strptime(input("Enter check-in date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
            checkout = datetime.strptime(input("Enter check-out date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
            return search.search_hotels("", 1, 1, checkin, checkout)
        elif choice == "5":
            city = input("\nEnter city name: ").strip()
            stars = int(input("Enter minimum star rating (1-5): ").strip())
            guests = int(input("Enter number of guests: ").strip())
            checkin = datetime.strptime(input("Enter check-in date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
            checkout = datetime.strptime(input("Enter check-out date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
            return search.search_hotels(city, stars, guests, checkin, checkout)
    except Exception as e:
        print(f"Error during search: {e}")
        return []

def handle_hotel_results(hotels):
    if not hotels:
        print("No hotels found.")
        return

    print("\nMatching Hotels:")
    print("=" * 50)
    for h in hotels:
        print(f"ID: {h.hotel_id} | Name: {h.name} | Stars: {h.stars}")
        print(f"Address: {h.address.street}, {h.address.zip_code} {h.address.city}")
        print("-" * 50)

    while True:
        choice = input("\nWould you like to see room details for a hotel? (y/n): ").strip().lower()
        if choice == "y":
            try:
                hotel_id = int(input("Enter Hotel ID to view room details: ").strip())
                show_available = input("Only show available rooms for specific dates? (y/n): ").strip().lower()
                if show_available == "y":
                    checkin = datetime.strptime(input("Enter check-in date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
                    checkout = datetime.strptime(input("Enter check-out date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
                    guests = int(input("Enter number of guests: ").strip())
                    rooms = search.get_available_room_details(hotel_id, guests, checkin, checkout)
                    booking_context = (checkin, checkout, guests)
                else:
                    rooms = search.get_available_room_details(hotel_id, 1, date.today(), date.today())
                    booking_context = None

                print("\nRoom Type Details:")
                print("=" * 50)
                for room in rooms:
                    print(f"Room ID: {room['room_id']} | Room Type: {room['room_type']}")
                    print(f"Max Guests: {room['max_guests']}")
                    print(f"Description: {room['description']}")
                    print(f"Price/Night: {room['price_per_night']} | Total Price: {room['total_price']}")
                    print(f"Facilities: {', '.join(room['facilities'])}")
                    print("-" * 50)

                book_now = input("Would you like to book one of these rooms now? (y/n): ").strip().lower()
                if book_now == "y":
                    book_room_flow(booking_context)
                break
            except Exception as e:
                print(f"Error retrieving room type details: {e}")
        elif choice == "n":
            break
        else:
            print("Please enter 'y' or 'n'.")

def book_room_flow(booking_context=None):
    try:
        room_id = int(input("\nEnter Room ID to book: ").strip())
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        birth_str = input("Enter your birthdate (DD.MM.YYYY): ").strip()
        birthdate = datetime.strptime(birth_str, "%d.%m.%Y").date()
        nationality = input("Enter your nationality: ").strip()
        email = input("Enter your email address: ").strip()
        tel = int(input("Enter your phone number: ").strip())

        guest = Guest(first_name, last_name, birthdate, nationality, email, telnr=tel, address_id=1)

        if booking_context:
            checkin, checkout, guests = booking_context
        else:
            guests = int(input("Enter number of guests: ").strip())
            checkin = datetime.strptime(input("Enter check-in date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()
            checkout = datetime.strptime(input("Enter check-out date (DD.MM.YYYY): ").strip(), "%d.%m.%Y").date()

        result = booking.make_reservation(guest, room_id, checkin, checkout, guests)

        print("\nBooking successful!")
        print(f"Booking ID: {result['booking_id']}")
        print(f"Invoice ID: {result['invoice_id']}")
        print(f"Total Amount: {result['invoice_details'].total_amount}")
        print(f"Issue Date: {result['invoice_details'].issue_date}")
        print(f"Paid: {'Yes' if result['invoice_details'].is_paid else 'No'}")
    except Exception as e:
        print(f"Error during booking: {e}")

def view_invoice_flow():
    try:
        booking_id = int(input("\nEnter your Booking ID to view the invoice: ").strip())
        invoice_data = booking.get_invoice_by_booking(booking_id)
        if invoice_data:
            print("\nInvoice Details:")
            print(invoice_data)
        else:
            print("No invoice found for the given booking.")
    except Exception as e:
        print(f"Error retrieving invoice: {e}")

def cancel_booking_flow():
    try:
        booking_id = int(input("\nEnter the Booking ID you want to cancel: ").strip())
        confirm = input("Are you sure you want to cancel this booking? (y/n): ").strip().lower()
        if confirm == "y":
            booking.cancel_booking(booking_id)
            print("Booking cancelled successfully.")
        else:
            print("Cancellation aborted.")
    except Exception as e:
        print(f"Error cancelling booking: {e}")

def admin_menu():
    print("\n--- Admin Actions (To be implemented) ---")
    input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    main_menu()
