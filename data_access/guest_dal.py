from data_access.base_data_access import BaseDataAccess
from model.guest import Guest

class GuestDataAccess(BaseDataAccess):
    def get_guest_by_email(self, email: str) -> Guest | None:
        sql = """
        SELECT FirstName, LastName, Birthdate, Nationality, Email, TelNr
        FROM Guest WHERE Email = ?
        """
        row = self.fetchone(sql, (email,))
        return Guest(*row) if row else None

    def create_guest(self, guest: Guest) -> int:
        sql = """
        INSERT INTO Guest (FirstName, LastName, Birthdate, Nationality, Email, TelNr)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            guest.firstname,
            guest.lastname,
            guest.birthdate,
            guest.nationality,
            guest.email,
            guest.telnr
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id
