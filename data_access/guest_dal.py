from data_access.base_data_access import BaseDataAccess
from model.guest import Guest
from typing import Optional
from datetime import datetime

class GuestDataAccess(BaseDataAccess):
    def get_guest_by_email(self, email: str) -> Optional[Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, birthdate, nationality, email, telnr, address_id
        FROM Guest WHERE email = ?
        """
        row = self.fetchone(sql, (email,))
        if row:
            birthdate = datetime.strptime(row[3], "%Y-%m-%d").date() if isinstance(row[3], str) else row[3]
            return Guest(
                first_name=row[1],
                last_name=row[2],
                birthdate=birthdate,
                nationality=row[4],
                email=row[5],
                telnr=row[6],
                address_id=row[7],
                guest_id=row[0]
            )

        return None

    def create_guest(self, guest: Guest) -> int:
        sql = """
        INSERT INTO Guest (first_name, last_name, birthdate, nationality, email, telnr, address_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            guest.first_name,
            guest.last_name,
            guest.birthdate,
            guest.nationality,
            guest.email,
            guest.telnr,
            guest.address_id
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id
