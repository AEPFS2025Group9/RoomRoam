from datetime import date
from data_access.room_dal import RoomDataAccess
from data_access.room_type_dal import RoomTypeDataAccess
from data_access.room_facility_dal import RoomFacilityDataAccess
from data_access.facility_dal import FacilityDataAccess

class SearchManager:
    def get_available_room_details(self, hotel_id: int, guests: int, checkin: date, checkout: date):
        room_dal = RoomDataAccess()
        room_type_dal = RoomTypeDataAccess()
        room_facility_dal = RoomFacilityDataAccess()
        facility_dal = FacilityDataAccess()

        # Schritt 1: Verfügbare Zimmer mit Mindest-Gästezahl
        available_rooms = room_dal.get_available_rooms(hotel_id, guests, checkin, checkout)

        result = []
        nights = (checkout - checkin).days

        for room in available_rooms:
            # Zimmertyp laden
            room_type = room_type_dal.get_room_type_by_id(room.type_id)
            if room_type is None:
                continue  # Skip if room type not found
                
            # Ausstattung laden
            facility_ids = room_facility_dal.get_facilities_by_room(room.room_id)
            facilities = [facility_dal.get_facility_by_id(fid) for fid in facility_ids if facility_dal.get_facility_by_id(fid) is not None]
            
            # Gesamtpreis berechnen
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