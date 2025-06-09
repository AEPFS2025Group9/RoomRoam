import os
import pandas as pd

import model
import data_access
from data_access.booking_dal import BookingDataAccess

class AdminManager:
    def __init__(self):
        self.booking_dal = BookingDataAccess()

    def get_booking_overview(self):
        """Übersicht aller Buchungen"""
        return self.booking_dal.read_all_booking_overview()

    def get_booking_overview_as_df(self):
        """Buchungen für die Datenvisualisierung"""
        return self.booking_dal.read_all_booking_overview_as_df()

    def get_bookings_per_room_type(self):
        """BUchungen pro Zimmertyp"""
        return self.booking_dal.get_bookings_per_room_type()

    def get_bookings_per_room_type_as_df(self):
        """Buchungen pro Zimmertyp für Datenvisualisierung"""
        return self.booking_dal.get_bookings_per_room_type_as_df()

    def get_room_type_summary(self):
        """ZUsammenfassung der Daten po Zimmertyp"""
        return self.booking_dal.get_room_type_summary()

    def get_room_type_summary_as_df(self):
        """Zimmertypen-ZUsammenfassung für Datenvis."""
        return self.booking_dal.get_room_type_summary_as_df()