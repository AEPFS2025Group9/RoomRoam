# guest_dal.py

from data_access.base_data_access import BaseDataAccess
from model.guest import Guest

class GuestDataAccess(BaseDataAccess):
    def get_guest_by_email(self, email: str) -> Guest | None:
        sql = "SELECT GuestId, FirstName, LastName, Email FROM Guest WHERE Email = ?"
        row = self.fetchone(sql, (email,))
        return Guest(*row) if row else None

    def create_guest(self, guest: Guest):
        sql = "INSERT INTO Guest (FirstName, LastName, Email) VALUES (?, ?, ?)"
        return self.execute(sql, (guest.first_name, guest.last_name, guest.email))

