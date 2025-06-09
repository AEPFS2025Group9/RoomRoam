import os

import model
import data_access
from data_access.booking_dal import BookingDataAccess

class AdminManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()

    def get_booking_overview(self):
        return self.booking_dal.read_all_booking_overview()

    def get_booking_overview_as_df(self):
        return self.booking_dal.read_all_booking_overview_as_df()