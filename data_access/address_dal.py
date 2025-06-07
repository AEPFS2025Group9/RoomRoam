from data_access.base_data_access import BaseDataAccess
from model.address import Address
from typing import Optional

class AddressDataAccess(BaseDataAccess):
    def create_address(self, address: Address) -> int:
        sql = """
        INSERT INTO Address (street, city, zip_code)
        VALUES (?, ?, ?, ?)
        """
        params = (address.street, address.city, address.zip_code)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def get_address_by_id(self, address_id: int) -> Optional[Address]:
        sql = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        row = self.fetchone(sql, (address_id,))
        return Address(*row[1:]) if row else None  # Skip adress_id

