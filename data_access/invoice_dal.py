import model

class InvoiceDataAccess(BaseDataAccess):
    def create_invoice(self, invoice: model.Invoice) -> int:
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

    def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
        sql = "SELECT * FROM Invoice WHERE invoice_id = ?"
        result = self.fetchone(sql, (invoice_id,))
        if result:
            return model.Invoice(*result)
        return None

    def read_all_invoices(self) -> list[model.Invoice]:
        sql = "SELECT * FROM Invoice"
        results = self.fetchall(sql)
        return [model.Invoice(*row) for row in results]

    def mark_invoice_as_paid(self, invoice_id: int) -> None:
        sql = "UPDATE Invoice SET is_paid = 1 WHERE invoice_id = ?"
        self.execute(sql, (invoice_id,))
