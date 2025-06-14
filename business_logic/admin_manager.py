import pandas as pd
from typing import List, Optional
from data_access.booking_dal import BookingDataAccess
from data_access.hotel_dal import HotelDataAccess
from data_access.address_dal import AddressDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.facility_dal import FacilityDataAccess
from data_access.room_dal import RoomDataAccess
from model.hotel import Hotel
from model.address import Address

class AdminManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()
        self.hotel_dal = HotelDataAccess()
        self.address_dal = AddressDataAccess()
        self.room_type_dal = RoomTypeDataAccess()
        self.facility_dal = FacilityDataAccess()
        self.room_dal = RoomDataAccess()


    # --- Buchungen ---

    def get_booking_overview(self):
        return self.booking_dal.read_all_booking_overview()

    def get_booking_overview_as_df(self):
        return self.booking_dal.read_all_booking_overview_as_df()

    def get_bookings_per_room_type(self):
        return self.booking_dal.get_bookings_per_room_type()

    def get_bookings_per_room_type_as_df(self):
        return self.booking_dal.get_bookings_per_room_type_as_df()

    def get_room_type_summary(self):
        return self.booking_dal.get_room_type_summary()

    def get_room_type_summary_as_df(self):
        return self.booking_dal.get_room_type_summary_as_df()

    # --- Hotel-Logik ---

    def get_all_hotels(self) -> List[Hotel]:
        try:
            return self.hotel_dal.read_all_hotels()
        except Exception as e:
            print(f"Fehler beim Abrufen der Hotels: {e}")
            raise

    def get_hotel_by_id(self, hotel_id: int) -> Optional[Hotel]:
        try:
            hotels = self.get_all_hotels()
            return next((hotel for hotel in hotels if hotel.hotel_id == hotel_id), None)
        except Exception as e:
            print(f"Fehler beim Abrufen des Hotels: {e}")
            return None

    def get_hotels_by_city(self, city: str) -> List[Hotel]:
        try:
            return self.hotel_dal.read_hotels_by_city(city)
        except Exception as e:
            print(f"Fehler beim Abrufen der Hotels für Stadt '{city}': {e}")
            raise

    def get_hotels_by_stars(self, min_stars: int = 1, max_stars: int = 5) -> List[Hotel]:
        try:
            return [hotel for hotel in self.get_all_hotels() if min_stars <= hotel.stars <= max_stars]
        except Exception as e:
            print(f"Fehler beim Filtern nach Sternen: {e}")
            raise

    #neu in deepnote
    def get_hotels_by_guest_count(self, guest_count: int) -> List[Hotel]:
        try:
            matching_hotels = []
            for hotel in self.get_all_hotels():
                rooms = self.room_dal.get_rooms_by_hotel(hotel.hotel_id)
                for room in rooms:
                    room_type = self.room_type_dal.get_room_type_by_id(room.type_id)
                    if room_type and room_type.max_guests >= guest_count:
                        matching_hotels.append(hotel)
                        break 
            return matching_hotels
        except Exception as e:
            print(f"Fehler beim Filtern der Hotels nach Gästezahl: {e}")
            raise

    def add_hotel(self, name: str, stars: int, street: str, zip_code: str, city: str) -> int:
        try:
            address = Address(street, zip_code, city)
            address_id = self.address_dal.create_address(address)
            saved_address = self.address_dal.read_address_by_id(address_id)
            hotel = Hotel(0, name, stars, saved_address)
            return self.hotel_dal.create_hotel(hotel)
        except Exception as e:
            print(f"Fehler beim Hinzufügen des Hotels: {e}")
            return None

    def create_hotel(self, hotel: Hotel) -> Optional[int]:
        try:
            address_id = self.address_dal.create_address(hotel.address)
            hotel.address.address_id = address_id
            return self.hotel_dal.create_hotel(hotel)
        except Exception as e:
            print(f"Fehler beim Erstellen des Hotels: {e}")
            return None

    def remove_hotel(self, hotel_id: int) -> bool:
        try:
            hotel = self.get_hotel_by_id(hotel_id)
            if not hotel:
                print(f"Hotel mit ID {hotel_id} nicht gefunden")
                return False
            self.hotel_dal.delete_hotel(hotel_id)
            return True
        except Exception as e:
            print(f"Fehler beim Entfernen des Hotels: {e}")
            return False

    def delete_hotel(self, hotel_id: int) -> bool:
        try:
            self.hotel_dal.delete_hotel(hotel_id)
            return True
        except Exception as e:
            print(f"Fehler beim Löschen des Hotels: {e}")
            return False

    def update_hotel(self, hotel_id: int, name: Optional[str] = None, stars: Optional[int] = None,
                     street: Optional[str] = None, zip_code: Optional[str] = None, city: Optional[str] = None) -> bool:
        try:
            hotel = self.get_hotel_by_id(hotel_id)
            if not hotel:
                print(f"Hotel mit ID {hotel_id} nicht gefunden")
                return False
            if name is not None:
                hotel.name = name
            if stars is not None:
                hotel.stars = stars
            if any([street, zip_code, city]):
                if street: hotel.address.street = street
                if zip_code: hotel.address.zip_code = zip_code
                if city: hotel.address.city = city
                self.address_dal.update_address(hotel.address)
            self.hotel_dal.update_hotel(hotel)
            return True
        except Exception as e:
            print(f"Fehler beim Aktualisieren: {e}")
            return False

    def update_hotel_object(self, hotel: Hotel) -> bool:
        try:
            self.hotel_dal.update_hotel(hotel)
            return True
        except Exception as e:
            print(f"Fehler beim Aktualisieren: {e}")
            return False

    def update_room_type(self, type_id: int, description: Optional[str] = None, max_guests: Optional[int] = None) -> bool:
        try:
            room_type = self.room_type_dal.get_room_type_by_id(type_id)
            if not room_type:
                print(f"Zimmertyp mit ID {type_id} nicht gefunden")
                return False
            if description: room_type.description = description
            if max_guests is not None: room_type.max_guests = max_guests
            self.room_type_dal.update_room_type(room_type)
            return True
        except Exception as e:
            print(f"Fehler beim Aktualisieren des Zimmertyps: {e}")
            return False

    def update_facility(self, facility_id: int, name: Optional[str] = None, description: Optional[str] = None) -> bool:
        try:
            facility = self.facility_dal.get_facility_by_id(facility_id)
            if not facility:
                print(f"Ausstattung mit ID {facility_id} nicht gefunden")
                return False
            if name is not None:
                facility.name = name
            if description is not None:
                facility.description = description
            self.facility_dal.update_facility(facility)
            return True
        except Exception as e:
            print(f"Fehler beim Aktualisieren der Ausstattung: {e}")
            return False

    def update_room_price(self, room_id: int, new_price: float) -> bool:
        try:
            room = self.room_dal.get_room_by_id(room_id)
            if not room:
                print(f"Zimmer mit ID {room_id} nicht gefunden")
                return False
            room.price_per_night = new_price
            self.room_dal.update_room(room)
            return True
        except Exception as e:
            print(f"Fehler beim Aktualisieren des Zimmerpreises: {e}")
            return False

    def _has_active_bookings(self, hotel_id: int) -> bool:
        try:
            return self.booking_dal.has_active_bookings_for_hotel(hotel_id)
        except Exception:
            return True

    def list_rooms_with_facilities(self) -> List[tuple]:
    
        room_facility_list = []
        for hotel in self.get_all_hotels():
            rooms = self.room_dal.get_rooms_by_hotel(hotel.hotel_id)
            for room in rooms:
                facilities = self.facility_dal.get_facilities_by_room(room.room_id)
                facility_names = [fac.name for fac in facilities]
                room_facility_list.append((hotel.name, room.room_number, facility_names))
        return room_facility_list