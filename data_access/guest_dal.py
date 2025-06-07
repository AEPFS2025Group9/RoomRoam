from data_access.base_data_access import BaseDataAccess
from model.guest import Guest
from typing import Optional

class GuestDataAccess(BaseDataAccess):
    def get_guest_by_email(self, email: str) -> Optional[Guest]:
        sql = """
        SELECT first_name, last_name, email, address_id
        FROM Guest WHERE email = ?
        """
        row = self.fetchone(sql, (email,))
        return Guest(*row) if row else None

    def create_guest(self, guest: Guest) -> int:
        sql = """
        INSERT INTO Guest (first_name, last_name, email, address_id)
        VALUES (?, ?, ?, ?)
        """
        params = (
            guest.first_name,
            guest.last_name,
            guest.email,
            guest.address_id
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id
