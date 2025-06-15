from typing import List, Optional
from data_access.booking_dal import BookingDataAccess
from data_access.hotel_dal import HotelDataAccess
from data_access.address_dal import AddressDataAccess
from model.hotel import Hotel
from model.address import Address

class AdminManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()
        self.hotel_dal = HotelDataAccess()
        self.address_dal = AddressDataAccess()

    # --- Buchungen ---

    def get_booking_overview(self):
        """Übersicht aller Buchungen"""
        return self.booking_dal.read_all_booking_overview()

    def get_booking_overview_as_df(self):
        """Buchungen für Datenvisualisierung"""
        return self.booking_dal.read_all_booking_overview_as_df()

    def get_bookings_per_room_type(self):
        """Buchungen pro Zimmertyp"""
        return self.booking_dal.get_bookings_per_room_type()

    def get_bookings_per_room_type_as_df(self):
        """Buchungen pro Zimmertyp für Visualisierung"""
        return self.booking_dal.get_bookings_per_room_type_as_df()

    def get_room_type_summary(self):
        """Zusammenfassung pro Zimmertyp"""
        return self.booking_dal.get_room_type_summary()

    def get_room_type_summary_as_df(self, hotel_id: Optional[int] = None):
        df = self.booking_dal.get_room_type_summary_as_df()
        print("DEBUG: Columns in room type summary DF:", df.columns)  # <== Add this
        if hotel_id is not None:
            df = df[df["hotel_id"] == hotel_id]
        return df

    # --- Hotel-Logik ---

    def get_all_hotels(self) -> List[Hotel]:
        """Alle Hotels mit Adressen anzeigen"""
        try:
            return self.hotel_dal.read_all_hotels()

        except Exception as e:
            print(f"Fehler beim Abrufen der Hotels: {e}")
            raise

    def get_hotel_by_id(self, hotel_id: int) -> Optional[Hotel]:
        """Hotel anhand der ID abrufen"""
        try:
            hotels = self.get_all_hotels()
            return next((hotel for hotel in hotels if hotel.hotel_id == hotel_id), None)
        except Exception as e:
            print(f"Fehler beim Abrufen des Hotels: {e}")
            return None

    def get_hotels_by_city(self, city: str) -> List[Hotel]:
        """Hotels nach Stadt filtern"""
        try:
            return self.hotel_dal.read_all_hotels()
        except Exception as e:
            print(f"Fehler beim Abrufen der Hotels für Stadt '{city}': {e}")
            raise

    def get_hotels_by_stars(self, min_stars: int = 1, max_stars: int = 5) -> List[Hotel]:
        """Hotels nach Sterne filtern"""
        try:
            return [hotel for hotel in self.get_all_hotels() if min_stars <= hotel.stars <= max_stars]
        except Exception as e:
            print(f"Fehler beim Filtern nach Sternen: {e}")
            raise

    def add_hotel(self, name: str, stars: int, street: str, zip_code: str, city: str) -> int:
        """Neues Hotel + Adresse hinzufügen"""
        try:
            address = Address(
                street=street,
                zip_code=zip_code,
                city=city,
                address_id=0
            )
            address_id = self.address_dal.create_address(address)
            saved_address = self.address_dal.read_address_by_id(address_id)
            hotel = Hotel(0, name, stars, saved_address)
            return self.hotel_dal.create_hotel(hotel)
        except Exception as e:
            print(f"Fehler beim Hinzufügen des Hotels: {e}")
            return None

    def create_hotel(self, hotel: Hotel) -> Optional[int]:
        """Hotel-Objekt direkt speichern (mit Adresse)"""
        try:
            address_id = self.address_dal.create_address(hotel.address)
            hotel.address.address_id = address_id
            return self.hotel_dal.create_hotel(hotel)
        except Exception as e:
            print(f"Fehler beim Erstellen des Hotels: {e}")
            return None

    def remove_hotel(self, hotel_id: int) -> bool:
        """Hotel entfernen (nur wenn vorhanden)"""
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
        """Alternative Methode zum Löschen"""
        try:
            self.hotel_dal.delete_hotel(hotel_id)
            return True
        except Exception as e:
            print(f"Fehler beim Löschen des Hotels: {e}")
            return False

    def update_hotel(self, hotel_id: int, name: Optional[str] = None, stars: Optional[int] = None,
                     street: Optional[str] = None, zip_code: Optional[str] = None, city: Optional[str] = None) -> bool:
        """Hotelinformationen aktualisieren"""
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
        """Hotelobjekt direkt aktualisieren"""
        try:
            self.hotel_dal.update_hotel(hotel)
            return True
        except Exception as e:
            print(f"Fehler beim Aktualisieren: {e}")
            return False

    def _has_active_bookings(self, hotel_id: int) -> bool:
        """Prüft, ob ein Hotel aktive Buchungen hat"""
        try:
            return self.booking_dal.has_active_bookings_for_hotel(hotel_id)
        except Exception:
            return True
