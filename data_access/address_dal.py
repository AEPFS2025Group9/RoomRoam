from data_access.base_data_access import BaseDataAccess
from model.address import Address
from typing import List, Optional

class AddressDataAccess(BaseDataAccess):
    def create_address(self, address: Address) -> int:
        """Neue Adresse erstellen"""
        sql = "INSERT INTO Address (street, zip_code, city) VALUES (?, ?, ?)"
        params = (address.street, address.zip_code, address.city)
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_address_by_id(self, address_id: int) -> Optional[Address]:
        """Adresse anhand der ID anzeigen"""
        sql = "SELECT address_id, street, zip_code, city FROM Address WHERE address_id = ?"
        rows = self.fetchall(sql, (address_id,))
        
        if rows:
            address_id, street, zip_code, city = rows[0]
            return Address(address_id, street, zip_code, city)
        return None

    def read_all_addresses(self) -> List[Address]:
        """Alle Adressen anzeigen"""
        sql = "SELECT address_id, street, zip_code, city FROM Address"
        rows = self.fetchall(sql)
        addresses = []
        for address_id, street, zip_code, city in rows:
            address = Address(address_id, street, zip_code, city)
            addresses.append(address)
        return addresses

    def update_address(self, address: Address) -> None:
        """Adresse aktualisieren"""
        sql = "UPDATE Address SET street = ?, zip_code = ?, city = ? WHERE address_id = ?"
        params = (address.street, address.zip_code, address.city, address.address_id)
        self.execute(sql, params)

    def delete_address(self, address_id: int) -> None:
        """Adresse löschen"""
        sql = "DELETE FROM Address WHERE address_id = ?"
        self.execute(sql, (address_id,))

    def get_addresses_by_city(self, city: str) -> List[Address]:
        """Adressen nach Stadt filtern"""
        sql = "SELECT address_id, street, zip_code, city FROM Address WHERE city = ?"
        rows = self.fetchall(sql, (city,))
        addresses = []
        for address_id, street, zip_code, city in rows:
            address = Address(address_id, street, zip_code, city)
            addresses.append(address)
        return addresses