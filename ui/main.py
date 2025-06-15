from business_logic.admin_manager import AdminManager
from business_logic.booking_manager import BookingManager
from business_logic.search_manager import SearchManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.review_manager import ReviewManager
from business_logic.master_data_manager import MasterDataManager
from model.guest import Guest
from datetime import datetime, date
from data_access.booking_dal import BookingDataAccess
from data_access.room_dal import RoomDataAccess
from data_access.review_dal import ReviewDAL
import matplotlib.pyplot as plt

# Instantiate managers
admin = AdminManager()
booking = BookingManager()
search = SearchManager()
invoice = InvoiceManager()
review = ReviewManager()
master = MasterDataManager()

# Ensure reviews table exists
ReviewDAL().create_table()

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

def show_room_type_occupancy_chart():
    try:
        hotels = admin.get_all_hotels()
        print("\nAvailable Hotels:")
        for h in hotels:
            print(f"{h.hotel_id}: {h.name}")
        print("0: All Hotels")

        hotel_id = int(input("\nEnter the Hotel ID to view room type occupancy chart (0 for all): ").strip())

        if hotel_id == 0:
            summary_df = admin.get_room_type_summary_as_df()
            title = "Buchungen pro Zimmertyp - Alle Hotels"
        else:
            summary_df = admin.get_room_type_summary_as_df(hotel_id)
            title = f"Buchungen pro Zimmertyp - Hotel ID {hotel_id}"

        if summary_df.empty:
            print("No data available for the selected option.")
            return

        plt.figure(figsize=(10, 6))
        plt.bar(summary_df["room_type"], summary_df["total_bookings"], color='skyblue')
        plt.title(title)
        plt.xlabel("Zimmertyp")
        plt.ylabel("Anzahl Buchungen")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error generating chart: {e}")

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
                    checkin = checkout = date.today()
                    rooms = search.get_available_room_details(hotel_id, 1, checkin, checkout)
                    booking_context = (checkin, checkout, 1)

                print("\nRoom Type Details:")
                print("=" * 50)
                for room in rooms:
                    print(f"Room ID: {room['room_id']} | Room Type: {room['room_type']}")
                    print(f"Max Guests: {room['max_guests']}")
                    print(f"Description: {room['description']}")
                    month = booking_context[0].month
                    if month in [6, 7, 8, 12]:
                        season_label = "(High Season: +20%)"
                    elif month in [1, 2, 11]:
                        season_label = "(Low Season: -15%)"
                    else:
                        season_label = "(Standard Rate)"
                    print(f"Dynamic Price/Night: {room['price_per_night']} {season_label} | Total Price: {room['total_price']}")
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

def book_room_flow(booking_context):
    try:
        room_id = int(input("\nEnter Room ID to book: ").strip())
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        birth_str = input("Enter your birthdate (DD.MM.YYYY): ").strip()
        birthdate = datetime.strptime(birth_str, "%d.%m.%Y").date()
        nationality = input("Enter your nationality: ").strip()
        email = input("Enter your email address: ").strip()
        tel = input("Enter your phone number: ").strip()
        if not tel.isdigit():
            raise ValueError("Phone number must contain only digits")

        guest = Guest(first_name, last_name, birthdate, nationality, email, telnr=tel, address_id=1)
        checkin, checkout, guests = booking_context
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
            booking_dal = BookingDataAccess()
            related_booking = booking_dal.read_booking_by_id(invoice_data.booking_id)
            if related_booking:
                month = related_booking.check_in_date.month
                if month in [6, 7, 8, 12]:
                    print("Seasonal Pricing Applied: High Season (+20%)")
                elif month in [1, 2, 11]:
                    print("Seasonal Pricing Applied: Low Season (-15%)")
                else:
                    print("Seasonal Pricing Applied: Standard Rate")

                # Prompt to add a review
                add_review = input("Would you like to leave a review for your stay? (y/n): ").strip().lower()
                if add_review == "y":
                    rating = int(input("Enter rating (1-5): ").strip())
                    comment = input("Enter your comment: ").strip()

                    room_dal = RoomDataAccess()
                    room = room_dal.get_room_by_id(related_booking.room_id)
                    hotel_id = room.hotel_id if room else None

                    if hotel_id:
                        review.add_review(related_booking.guest_id, hotel_id, rating, comment)
                        print("Thank you for your review!")
                    else:
                        print("Error: Hotel information is missing for this booking.")
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
    while True:
        print("\n--- Admin Actions ---")
        print("1. View All Hotels")
        print("2. Add New Hotel")
        print("3. Update Hotel")
        print("4. Delete Hotel")
        print("5. View All Bookings")
        print("6. View Room Facilities")
        print("7. Manage Master Data")
        print("8. Show Room Type Occupancy Chart")
        print("9. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            hotels = admin.get_all_hotels()
            for h in hotels:
                print(h)
        elif choice == "2":
            try:
                name = input("Enter hotel name: ").strip()
                stars = int(input("Enter star rating (1-5): ").strip())
                street = input("Enter street address: ").strip()
                zip_code = input("Enter ZIP code: ").strip()
                city = input("Enter city: ").strip()
                hotel_id = admin.add_hotel(name, stars, street, zip_code, city)
                if hotel_id:
                    print(f"Hotel added with ID: {hotel_id}")
            except Exception as e:
                print(f"Error adding hotel: {e}")
        elif choice == "3":
            try:
                hotel_id = int(input("Enter Hotel ID to update: ").strip())
                name = input("New name (leave blank to skip): ").strip() or None
                stars_input = input("New star rating (1-5, leave blank to skip): ").strip()
                stars = int(stars_input) if stars_input else None
                street = input("New street (leave blank to skip): ").strip() or None
                zip_code = input("New ZIP code (leave blank to skip): ").strip() or None
                city = input("New city (leave blank to skip): ").strip() or None
                success = admin.update_hotel(hotel_id, name, stars, street, zip_code, city)
                print("Hotel updated successfully." if success else "Update failed.")
            except Exception as e:
                print(f"Error updating hotel: {e}")
        elif choice == "4":
            try:
                hotel_id = int(input("Enter Hotel ID to delete: ").strip())
                confirm = input("Are you sure you want to delete this hotel? (y/n): ").strip().lower()
                if confirm == "y":
                    success = admin.remove_hotel(hotel_id)
                    print("Hotel deleted successfully." if success else "Delete failed.")
            except Exception as e:
                print(f"Error deleting hotel: {e}")
        elif choice == "5":
            view_all_bookings()
        elif choice == "6":
            view_room_facilities()
        elif choice == "7":
            manage_master_data()
        elif choice == "8":
            show_room_type_occupancy_chart()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def view_all_bookings():
    try:
        bookings = admin.get_booking_overview()
        if not bookings:
            print("No bookings found.")
            return

        print("\nAll Bookings:")
        print("=" * 50)
        for b in bookings:
            print(
                f"Booking ID: {b['booking_id']} | Guest: {b['guest_name']} | "
                f"Hotel: {b['hotel_name']} | Room: {b['room_number']} | "
                f"Check-in: {b['check_in_date']} | Check-out: {b['check_out_date']}"
            )
    except Exception as e:
        print(f"Error retrieving bookings: {e}")

def view_room_facilities():
    try:
        from data_access.room_dal import RoomDataAccess
        room_dal = RoomDataAccess()

        sql = '''
        SELECT r.room_id, r.room_number, rt.description, h.name, GROUP_CONCAT(f.facility_name, ', ')
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        GROUP BY r.room_id, r.room_number, rt.description, h.name
        ORDER BY h.name, r.room_number
        '''

        results = room_dal.fetchall(sql)

        print("\nRoom Facility Overview:")
        print("=" * 50)
        for row in results:
            room_id, room_number, room_type, hotel_name, facilities = row
            print(f"Hotel: {hotel_name} | Room {room_number} (ID: {room_id}) | Type: {room_type}")
            print(f"Facilities: {facilities if facilities else 'None'}")
            print("-" * 50)

    except Exception as e:
        print(f"Error retrieving room facilities: {e}")

from business_logic.admin_manager import AdminManager
from business_logic.booking_manager import BookingManager
from business_logic.search_manager import SearchManager
from business_logic.invoice_manager import InvoiceManager
from business_logic.review_manager import ReviewManager
from business_logic.master_data_manager import MasterDataManager
from model.guest import Guest
from datetime import datetime, date
from data_access.booking_dal import BookingDataAccess  # 🔁 Needed for dynamic invoice season

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

# --- New Admin Function ---
def view_all_bookings():
    try:
        bookings = admin.get_booking_overview()
        if not bookings:
            print("No bookings found.")
            return

        print("\nAll Bookings:")
        print("=" * 50)
        for b in bookings:
            print(
                f"Booking ID: {b['booking_id']} | Guest: {b['guest_name']} | "
                f"Hotel: {b['hotel_name']} | Room: {b['room_number']} | "
                f"Check-in: {b['check_in_date']} | Check-out: {b['check_out_date']} | "
                f"Guests: {b.get('guest_count', 'N/A')}"
            )
    except Exception as e:
        print(f"Error retrieving bookings: {e}")

# --- New Admin Function ---
def view_all_bookings():
    try:
        bookings = admin.get_booking_overview()
        if not bookings:
            print("No bookings found.")
            return

        print("\nAll Bookings:")
        print("=" * 50)
        for b in bookings:
            print(
                f"Booking ID: {b['booking_id']} | Guest: {b['guest_name']} | "
                f"Hotel: {b['hotel_name']} | Room: {b['room_number']} | "
                f"Check-in: {b['check_in_date']} | Check-out: {b['check_out_date']} | "
                f"Guests: {b.get('guest_count', 'N/A')}"
            )
    except Exception as e:
        print(f"Error retrieving bookings: {e}")

# --- New Admin Function ---
def view_room_facilities():
    try:
        from data_access.room_dal import RoomDataAccess
        room_dal = RoomDataAccess()

        sql = '''
        SELECT r.room_id, r.room_number, rt.description, h.name, GROUP_CONCAT(f.facility_name, ', ')
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        GROUP BY r.room_id, r.room_number, rt.description, h.name
        ORDER BY h.name, r.room_number
        '''

        results = room_dal.fetchall(sql)

        print("\nRoom Facility Overview:")
        print("=" * 50)
        for row in results:
            room_id, room_number, room_type, hotel_name, facilities = row
            print(f"Hotel: {hotel_name} | Room {room_number} (ID: {room_id}) | Type: {room_type}")
            print(f"Facilities: {facilities if facilities else 'None'}")
            print("-" * 50)

    except Exception as e:
        print(f"Error retrieving room facilities: {e}")

def manage_master_data():
    try:
        from data_access.room_type_dal import RoomTypeDataAccess
        from data_access.facility_dal import FacilityDataAccess
        from data_access.room_dal import RoomDataAccess
        from model.facility import Facility

        room_type_dal = RoomTypeDataAccess()
        facility_dal = FacilityDataAccess()
        room_dal = RoomDataAccess()

        print("\n--- Master Data Management ---")
        print("1. View Room Types")
        print("2. Update Room Type")
        print("3. View Facilities")
        print("4. Update Facility")
        print("5. Manage Rooms")
        print("6. Return")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            types = room_type_dal.get_all_room_types()
            for t in types:
                print(f"ID: {t.type_id} | {t.description} | Max Guests: {t.max_guests}")
        elif choice == "2":
            id = int(input("Enter Room Type ID: "))
            desc = input("New Description: ").strip()
            guests = int(input("New Max Guests: "))
            room_type_dal.update_room_type(id, desc, guests)
            print("Room type updated.")
        elif choice == "3":
            facilities = facility_dal.get_all_facilities()
            for f in facilities:
                print(f"ID: {f.id} | {f.name}")
        elif choice == "4":
            id = int(input("Enter Facility ID: "))
            name = input("New Facility Name: ").strip()
            facility = Facility(facility_id=id, facility_name=name)
            facility_dal.update_facility(facility)
            print("Facility updated.")
        elif choice == "5":
            rooms = room_dal.get_available_rooms_as_df()
            from data_access.room_type_dal import RoomTypeDataAccess
            rt_dal = RoomTypeDataAccess()
            room_types = {rt.type_id: rt.description for rt in rt_dal.get_all_room_types()}

            rooms['room_type'] = rooms['type_id'].map(room_types)
            print("\nRooms:")
            print(rooms[['hotel_id', 'room_number', 'room_type', 'price_per_night']])

            room_id = int(input("Enter Room ID to update: ").strip())
            new_price = float(input("Enter new price per night: ").strip())
            room = room_dal.get_room_by_id(room_id)
            room.price_per_night = new_price
            room_dal.update_room(room)
            print("Room price updated.")
    except Exception as e:
        print(f"Error managing master data: {e}")

def admin_menu():
    while True:
        print("\n--- Admin Actions ---")
        print("1. View All Hotels")
        print("2. Add New Hotel")
        print("3. Update Hotel")
        print("4. Delete Hotel")
        print("5. View All Bookings")
        print("6. View Room Facilities")
        print("7. Manage Master Data")
        print("8. Show Room Type Occupancy Chart")
        print("9. Return to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            hotels = admin.get_all_hotels()
            for h in hotels:
                print(h)
        elif choice == "2":
            try:
                name = input("Enter hotel name: ").strip()
                stars = int(input("Enter star rating (1-5): ").strip())
                street = input("Enter street address: ").strip()
                zip_code = input("Enter ZIP code: ").strip()
                city = input("Enter city: ").strip()
                hotel_id = admin.add_hotel(name, stars, street, zip_code, city)
                if hotel_id:
                    print(f"Hotel added with ID: {hotel_id}")
            except Exception as e:
                print(f"Error adding hotel: {e}")
        elif choice == "3":
            try:
                hotel_id = int(input("Enter Hotel ID to update: ").strip())
                name = input("New name (leave blank to skip): ").strip() or None
                stars_input = input("New star rating (1-5, leave blank to skip): ").strip()
                stars = int(stars_input) if stars_input else None
                street = input("New street (leave blank to skip): ").strip() or None
                zip_code = input("New ZIP code (leave blank to skip): ").strip() or None
                city = input("New city (leave blank to skip): ").strip() or None
                success = admin.update_hotel(hotel_id, name, stars, street, zip_code, city)
                print("Hotel updated successfully." if success else "Update failed.")
            except Exception as e:
                print(f"Error updating hotel: {e}")
        elif choice == "4":
            try:
                hotel_id = int(input("Enter Hotel ID to delete: ").strip())
                confirm = input("Are you sure you want to delete this hotel? (y/n): ").strip().lower()
                if confirm == "y":
                    success = admin.remove_hotel(hotel_id)
                    print("Hotel deleted successfully." if success else "Delete failed.")
            except Exception as e:
                print(f"Error deleting hotel: {e}")
        elif choice == "5":
            view_all_bookings()
        elif choice == "6":
            view_room_facilities()
        elif choice == "7":
            manage_master_data()
        elif choice == "8":
            show_room_type_occupancy_chart()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()








