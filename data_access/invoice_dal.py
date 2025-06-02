from data_access.base_data_access import BaseDataAccess
from model.invoice import Invoice

class InvoiceDataAccess(BaseDataAccess):
    def create_invoice(self, invoice: Invoice) -> int:
        sql = """
        INSERT INTO Invoice (booking_id, amount, issue_date, is_paid)
        VALUES (?, ?, ?, ?)
        """
        params = (
            invoice.booking_id,
            invoice.amount,
            invoice.issue_date,
            invoice.is_paid
        )
        last_row_id, _ = self.execute(sql, params)
        return last_row_id

    def read_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
        SELECT invoice_id, booking_id, amount, issue_date, is_paid
        FROM Invoice WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        return Invoice(*row) if row else None

    def read_all_invoices(self) -> list[Invoice]:
        sql = "SELECT invoice_id, booking_id, amount, issue_date, is_paid FROM Invoice"
        rows = self.fetchall(sql)
        return [Invoice(*row) for row in rows]

    def mark_invoice_as_paid(self, invoice_id: int) -> None:
        sql = "UPDATE Invoice SET is_paid = 1 WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))

    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice | None:
        sql = """
        SELECT invoice_id, booking_id, amount, issue_date, is_paid
        FROM Invoice WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        return Invoice(*row) if row else None

    def delete_invoice(self, invoice_id: int) -> None:
        sql = "DELETE FROM Invoice WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))
