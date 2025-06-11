import os
import pandas as pd
from typing import List, Optional

import model
import data_access
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

    def get_booking_overview(self):
        """Übersicht aller Buchungen"""
        return self.booking_dal.read_all_booking_overview()

    def get_booking_overview_as_df(self):
        """Buchungen für die Datenvisualisierung"""
        return self.booking_dal.read_all_booking_overview_as_df()

    def get_bookings_per_room_type(self):
        """Buchungen pro Zimmertyp"""
        return self.booking_dal.get_bookings_per_room_type()

    def get_bookings_per_room_type_as_df(self):
        """Buchungen pro Zimmertyp für Datenvisualisierung"""
        return self.booking_dal.get_bookings_per_room_type_as_df()

    def get_room_type_summary(self):
        """Zusammenfassung der Daten pro Zimmertyp"""
        return self.booking_dal.get_room_type_summary()

    def get_room_type_summary_as_df(self):
        """Zimmertypen-Zusammenfassung für Datenvis."""
        return self.booking_dal.get_room_type_summary_as_df()
    
    def add_hotel(self, name: str, stars: int, street: str, zip_code: str, city: str) -> int:
        """Neues Hotel hinzufügen"""
        try:
            address = Address(0, street, zip_code, city)
            address_id = self.address_dal.create_address(address)
            
            saved_address = self.address_dal.read_address_by_id(address_id)
            
            hotel = Hotel(0, name, stars, saved_address)
            hotel_id = self.hotel_dal.create_hotel(hotel)
            
            print(f"Hotel '{name}' erfolgreich hinzugefügt (ID: {hotel_id})")
            return hotel_id
            
        except ValueError as e:
            print(f"Fehler bei der Eingabevalidierung: {e}")
            raise
        except Exception as e:
            print(f"Fehler beim Hinzufügen des Hotels: {e}")
            raise

    def remove_hotel(self, hotel_id: int) -> bool:
        """Hotel entfernen"""
        try:
            """Prüft ob Hotel existiert"""
            hotel = self.get_hotel_by_id(hotel_id)
            if not hotel:
                print(f"Hotel mit ID {hotel_id} nicht gefunden")
                return False
                
            self.hotel_dal.delete_hotel(hotel_id)
            print(f"Hotel '{hotel.name}' (ID: {hotel_id}) erfolgreich entfernt")
            return True
                
        except Exception as e:
            print(f"Fehler beim Entfernen des Hotels: {e}")
            raise

    def update_hotel(self, hotel_id: int, name: Optional[str] = None, stars: Optional[int] = None, 
                    street: Optional[str] = None, zip_code: Optional[str] = None, 
                    city: Optional[str] = None) -> bool:
        """Hotelinformationen aktualisieren"""
        try:
            hotel = self.get_hotel_by_id(hotel_id)
            if not hotel:
                raise Exception(f"Hotel mit ID {hotel_id} nicht gefunden")
                
            if name is not None:
                hotel.name = name
            if stars is not None:
                hotel.stars = stars
            """Adresse aktualisieren"""    
            address_updated = False
            if any([street, zip_code, city]):
                if street is not None:
                    hotel.address.street = street
                    address_updated = True
                if zip_code is not None:
                    hotel.address.zip_code = zip_code
                    address_updated = True
                if city is not None:
                    hotel.address.city = city
                    address_updated = True                    
                if address_updated:
                    self.address_dal.update_address(hotel.address)
                
            self.hotel_dal.update_hotel(hotel)
                
            print(f"Hotel '{hotel.name}' (ID: {hotel_id}) erfolgreich aktualisiert")
            return True
                
        except ValueError as e:
            print(f"Fehler bei der Eingabevalidierung: {e}")
            raise
        except Exception as e:
            print(f"Fehler beim Aktualisieren des Hotels: {e}")
            raise

    def get_all_hotels(self) -> List[Hotel]:
        """Alle Hotels anzeigen"""
        try:
            hotels = self.hotel_dal.read_all_hotels()
            """mit Adresseninfos"""
            result = []
            for hotel in hotels:
                address = self.address_dal.read_address_by_id(hotel.address_id)
                if address:
                    # Hotel-Objekt mit vollständiger Adresse neu erstellen
                    hotel_with_address = Hotel(hotel.hotel_id, hotel.name, hotel.stars, address)
                    result.append(hotel_with_address)
            return result
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
            hotels = self.hotel_dal.read_hotels_by_city(city)
            # Adressinformationen für jedes Hotel laden
            result = []
            for hotel in hotels:
                address = self.address_dal.read_address_by_id(hotel.address_id)
                if address:
                    hotel_with_address = Hotel(hotel.hotel_id, hotel.name, hotel.stars, address)
                    result.append(hotel_with_address)
            return result
        except Exception as e:
            print(f"Fehler beim Abrufen der Hotels für Stadt '{city}': {e}")
            raise

    def get_hotels_by_stars(self, min_stars: int = 1, max_stars: int = 5) -> List[Hotel]:
        """Hotels nach Bewertung filtern"""
        try:
            all_hotels = self.get_all_hotels()
            return [hotel for hotel in all_hotels 
                   if min_stars <= hotel.stars <= max_stars]
        except Exception as e:
            print(f"Fehler beim Filtern der Hotels nach Sternen: {e}")
            raise

    def _has_active_bookings(self, hotel_id: int) -> bool:
        """Prüft ob ein Hotel noch aktive Buchungen hat"""
        try:
            return self.booking_dal.has_active_bookings_for_hotel(hotel_id)
        except Exception:
            return True