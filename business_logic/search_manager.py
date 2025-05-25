from datetime import date
from data_access.room_dal import RoomDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.room_facility_dal import RoomFacilityDataAccess
from data_access.facilities_dal import FacilitiesDataAccess

class SearchManager:
    def get_available_room_details(self, hotel_id: int, guests: int, checkin: date, checkout: date):
        room_dal = RoomDataAccess()
        room_type_dal = RoomTypeDataAccess()
        room_facility_dal = RoomFacilityDataAccess()
        facilities_dal = FacilitiesDataAccess()

        # Schritt 1: Verfügbare Zimmer mit Mindest-Gästezahl
        available_rooms = room_dal.get_available_rooms(hotel_id, guests, checkin, checkout)

        result = []
        nights = (checkout - checkin).days

        for room in available_rooms:
            # Zimmertyp laden
            room_type = room_type_dal.get_room_type_by_id(room.room_type_id)
            # Ausstattung laden
            facility_ids = room_facility_dal.get_facilities_by_room(room.room_id)
            facilities = [facilities_dal.get_facility_by_id(fid) for fid in facility_ids]
            # Gesamtpreis berechnen
            total_price = room.price * nights

            room_info = {
                "room_id": room.room_id,
                "room_type": room_type.name,
                "max_guests": room_type.max_guests,
                "description": room_type.description,
                "price_per_night": room.price,
                "total_price": total_price,
                "facilities": [f.name for f in facilities],
            }
            result.append(room_info)

        return result