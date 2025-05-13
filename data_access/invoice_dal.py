# invoice_dal.py

from data_access.base_data_access import BaseDataAccess
from model.invoice import Invoice

class InvoiceDataAccess(BaseDataAccess):
    def create_invoice(self, invoice: Invoice):
        sql = "INSERT INTO Invoice (BookingId, IssueDate, TotalAmount) VALUES (?, ?, ?)"
        return self.execute(sql, (invoice.booking_id, invoice.issue_date, invoice.total_amount))
