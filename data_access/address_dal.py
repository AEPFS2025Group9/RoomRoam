# address_dal.py

from data_access.base_data_access import BaseDataAccess
from model.address import Address

class AddressDataAccess(BaseDataAccess):
    def create_address(self, address: Address):
        sql = "INSERT INTO Address (Street, City, Country) VALUES (?, ?, ?)"
        return self.execute(sql, (address.street, address.city, address.country))

    def get_address_by_id(self, address_id: int) -> Address | None:
        sql = "SELECT AddressId, Street, City, Country FROM Address WHERE AddressId = ?"
        row = self.fetchone(sql, (address_id,))
        return Address(*row) if row else None
