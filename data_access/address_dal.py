from data_access.base_data_access import BaseDataAccess
from model.address import Address

class AddressDataAccess(BaseDataAccess):
    def create_address(self, address: Address) -> int:
        sql = """
        INSERT INTO Address (Street, StreetNumber, Zip, City)
        VALUES (?, ?, ?, ?)
        """
        params = (address.street, address.streetnr, address.zip, address.city)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def get_address_by_id(self, address_id: int) -> Address | None:
        sql = "SELECT AddressId, Street, StreetNumber, Zip, City FROM Address WHERE AddressId = ?"
        row = self.fetchone(sql, (address_id,))
        return Address(*row[1:]) if row else None  # Skip AddressId

