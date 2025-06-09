import os
import pandas as pd

import model
import data_access
from data_access.booking_dal import BookingDataAccess

class AdminManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()

    def get_booking_overview(self):
        """Get basic booking overview"""
        return self.booking_dal.read_all_booking_overview()

    def get_booking_overview_as_df(self):
        """Get booking overview as DataFrame"""
        return self.booking_dal.read_all_booking_overview_as_df()

    def get_bookings_per_room_type(self):
        """Get all bookings grouped by room type"""
        return self.booking_dal.get_bookings_per_room_type()

    def get_bookings_per_room_type_as_df(self):
        """Get bookings per room type as DataFrame"""
        return self.booking_dal.get_bookings_per_room_type_as_df()

    def get_room_type_summary(self):
        """Get summary statistics for bookings per room type"""
        return self.booking_dal.get_room_type_summary()

    def get_room_type_summary_as_df(self):
        """Get room type summary as DataFrame"""
        return self.booking_dal.get_room_type_summary_as_df()