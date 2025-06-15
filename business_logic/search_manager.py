import pandas as pd
from datetime import date
from data_access.room_dal import RoomDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.room_facility_dal import RoomFacilityDataAccess
from data_access.facility_dal import FacilityDataAccess
from data_access.hotel_dal import HotelDataAccess
from typing import List


class SearchManager:
    def __init__(self):
        self.room_dal = RoomDataAccess()
        self.room_type_dal = RoomTypeDataAccess()
        self.room_facility_dal = RoomFacilityDataAccess()
        self.facility_dal = FacilityDataAccess()
        self.hotel_dal = HotelDataAccess()

    def get_available_room_details(self, hotel_id: int, guests: int, checkin: date, checkout: date) -> List[dict]:
        """Verfügbare Zimmer inkl. Ausstattung, Preis etc."""
        available_rooms = self.room_dal.get_available_rooms(hotel_id, guests, checkin, checkout)
        nights = (checkout - checkin).days
        result = []

        for room in available_rooms:
            room_type = self.room_type_dal.get_room_type_by_id(room.type_id)
            if room_type is None:
                continue

            facility_ids = self.room_facility_dal.get_facilities_by_room(room.room_id)
            facilities = [self.facility_dal.get_facility_by_id(fid) for fid in facility_ids if self.facility_dal.get_facility_by_id(fid)]

            total_price = room.price_per_night * nights

            room_info = {
                "room_id": room.room_id,
                "room_type": room_type.description,
                "max_guests": room_type.max_guests,
                "description": room_type.description,
                "price_per_night": room.price_per_night,
                "total_price": total_price,
                "facilities": [f.name for f in facilities],
            }
            result.append(room_info)

        return result

    def get_available_rooms_as_df(self) -> pd.DataFrame:
        """Verfügbare Zimmer als DataFrame"""
        return self.room_dal.get_available_rooms_as_df()

    def get_available_room_details_as_df(self, hotel_id: int, guests: int, checkin: date, checkout: date) -> pd.DataFrame:
        """Zimmerdetails als DataFrame"""
        room_details = self.get_available_room_details(hotel_id, guests, checkin, checkout)
        return pd.DataFrame(room_details)

    def search_hotels(self, city: str, min_stars: int, guests: int, checkin: date, checkout: date):
        """Hotels nach Stadt, Sternen und Verfügbarkeit filtern"""
        hotels = self.hotel_dal.read_all_hotels()
        result = []

        for hotel in hotels:
            if city.lower() not in hotel.address.city.lower():
                continue
            if hotel.stars < min_stars:
                continue

            available_rooms = self.room_dal.get_available_rooms(hotel.hotel_id, guests, checkin, checkout)
            if not available_rooms:
                continue

            result.append(hotel)

        return result