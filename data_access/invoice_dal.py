from data_access.base_data_access import BaseDataAccess
from model.invoice import Invoice
from typing import Optional, List
from datetime import datetime

class InvoiceDataAccess(BaseDataAccess):
    def create_invoice(self, invoice: Invoice) -> int:
        sql = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount, is_paid)
        VALUES (?, ?, ?, ?)
        """
        params = (
            invoice.booking_id,
            invoice.issue_date,
            invoice.total_amount,
            invoice.is_paid
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def _parse_invoice_row(self, row):
        return Invoice(
            invoice_id=row[0],
            booking_id=row[1],
            issue_date=datetime.strptime(row[2], "%Y-%m-%d").date() if isinstance(row[2], str) else row[2],
            total_amount=row[3],
            is_paid=bool(row[4])
        )

    def read_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount, is_paid
        FROM Invoice WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        return self._parse_invoice_row(row) if row else None

    def read_all_invoices(self) -> List[Invoice]:
        sql = "SELECT invoice_id, booking_id, issue_date, total_amount, is_paid FROM Invoice"
        rows = self.fetchall(sql)
        return [self._parse_invoice_row(row) for row in rows]

    def mark_invoice_as_paid(self, invoice_id: int) -> None:
        sql = "UPDATE Invoice SET is_paid = 1 WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))

    def get_invoice_by_booking_id(self, booking_id: int) -> Optional[Invoice]:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount, is_paid
        FROM Invoice WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        return self._parse_invoice_row(row) if row else None

    def delete_invoice(self, invoice_id: int) -> None:
        sql = "DELETE FROM Invoice WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))

    def get_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount, is_paid
        FROM Invoice WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        return self._parse_invoice_row(row) if row else None
