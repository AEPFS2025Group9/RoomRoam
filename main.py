from data_access.review_dal import ReviewDAL
from data_access.invoice_dal import InvoiceDataAccess

if __name__ == "__main__":
    # Review table
    review_dal = ReviewDAL()
    review_dal.create_table()
    print("Review table created or already exists.")

    # Invoice table
    invoice_dal = InvoiceDataAccess()
    invoice_dal.create_table()
    print("Invoice table created or already exists.")