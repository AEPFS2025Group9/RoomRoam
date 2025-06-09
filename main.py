from data_access.review_dal import ReviewDAL

if __name__ == "__main__":
    review_dal = ReviewDAL()
    review_dal.create_table()
    print("Review table created or already exists.")
