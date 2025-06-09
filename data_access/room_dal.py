import pandas as pd

from data_access.base_data_access import BaseDataAccess
from model.room import Room
from model.room_type import RoomType
from typing import List

class RoomDataAccess(BaseDataAccess):
    def get_rooms_by_hotel(self, hotel_id: int) -> List[Room]:
        sql = """
        SELECT room_id, hotel_id, room_number, type_id, price_per_night
        FROM Room WHERE hotel_id = ?
        """
        rows = self.fetchall(sql, (hotel_id,))
        
        # Create RoomType objects for each room
        result = []
        for row in rows:
            room_type = self.get_room_type_by_id(row[3])  # Assuming you have a method to fetch RoomType by type_id
            room = Room(room_id=row[0], hotel_id=row[1], room_number=row[2], type_id=row[3], price_per_night=row[4])
            result.append(room)
        return result

    def get_available_rooms(self, hotel_id: int, guests: int, check_in_date, check_out_date) -> List[Room]:
        sql = """
        SELECT r.room_id, r.hotel_id, r.room_number, r.type_id, r.price_per_night
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE r.hotel_id = ?
            AND rt.max_guests >= ?
            AND r.room_id NOT IN (
                SELECT b.room_id FROM Booking b
                WHERE NOT (b.check_out_date <= ? OR b.check_in_date >= ?)
            )
        """
        rows = self.fetchall(sql, (hotel_id, guests, check_out_date, check_in_date))
        
        # Create RoomType objects for each room
        result = []
        for row in rows:
            room_type = self.get_room_type_by_id(row[3])  # Assuming you have a method to fetch RoomType by type_id
            room = Room(room_id=row[0], hotel_id=row[1], room_number=row[2], type_id=row[3], price_per_night=row[4])
            result.append(room)
        return result

    def get_room_type_by_id(self, type_id: int) -> RoomType:
        sql = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        row = self.fetchone(sql, (type_id,))
        if row:
        # Handle None or empty description
            description = row[1] if row[1] and str(row[1]).strip() else "Standard room"
            return RoomType(type_id=row[0], description=description, max_guests=row[2])
        return None

    def get_available_rooms_as_df(self) -> pd.DataFrame:
        sql = """
        SELECT room_id, hotel_id, room_number, type_id, price_per_night
        FROM Room
        """
        rows = self.fetchall(sql)
        
        # Convert to DataFrame manually
        if rows:
            df = pd.DataFrame(rows, columns=['room_id', 'hotel_id', 'room_number', 'type_id', 'price_per_night'])
            df = df.set_index('room_id')
            return df
        else:
            # Return empty DataFrame with correct columns
            return pd.DataFrame(columns=['hotel_id', 'room_number', 'type_id', 'price_per_night']).set_index(pd.Index([], name='room_id'))