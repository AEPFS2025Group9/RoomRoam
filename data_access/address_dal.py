from data_access.base_data_access import BaseDataAccess
from model.address import Address
from typing import List, Optional

class AddressDataAccess(BaseDataAccess):
    def create_address(self, address: Address) -> int:
        sql = "INSERT INTO Address (street, zip_code, city) VALUES (?, ?, ?)"
        params = (address.street, address.zip_code, address.city)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_address_by_id(self, address_id: int) -> Optional[Address]:
        sql = "SELECT address_id, street, zip_code, city FROM Address WHERE address_id = ?"
        row = self.fetchone(sql, (address_id,))
        if row:
            address = Address.from_db(
                address_id=row["address_id"],
                street=row["street"],
                zip_code=row["zip_code"],
                city=row["city"]
            )
            return address
        return None

    def read_all_addresses(self) -> List[Address]:
        sql = "SELECT address_id, street, zip_code, city FROM Address"
        rows = self.fetchall(sql)
        return [
            Address.from_db(
                address_id=row["address_id"],
                street=row["street"],
                zip_code=row["zip_code"],
                city=row["city"]
            ) for row in rows
        ]

    def update_address(self, address: Address) -> None:
        sql = "UPDATE Address SET street = ?, zip_code = ?, city = ? WHERE address_id = ?"
        params = (address.street, address.zip_code, address.city, address.address_id)
        self.execute(sql, params)

    def delete_address(self, address_id: int) -> None:
        sql = "DELETE FROM Address WHERE address_id = ?"
        self.execute(sql, (address_id,))

    def get_addresses_by_city(self, city: str) -> List[Address]:
        sql = "SELECT address_id, street, zip_code, city FROM Address WHERE city = ?"
        rows = self.fetchall(sql, (city,))
        return [
            Address.from_db(
                address_id=row["address_id"],
                street=row["street"],
                zip_code=row["zip_code"],
                city=row["city"]
            ) for row in rows
        ]

    def get_address_by_id(self, address_id: int) -> Optional[Address]:
        return self.read_address_by_id(address_id)
