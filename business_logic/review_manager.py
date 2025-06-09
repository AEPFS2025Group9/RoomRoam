from data_access.review_dal import ReviewDAL
from model.review import Review
from datetime import datetime

class ReviewManager:
    def __init__(self):
        self.dal = ReviewDAL()

    def add_review(self, guest_id: int, hotel_id: int, rating: int, comment: str) -> Review:
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        if not comment or not isinstance(comment, str):
            raise ValueError("Comment must be a non-empty string")

        self.dal.insert_review(guest_id, hotel_id, rating, comment)

        review_id = self.dal.get_last_inserted_id()  # optional enhancement
        review_date = datetime.now().strftime("%Y-%m-%d")

        return Review(review_id, guest_id, hotel_id, rating, comment, review_date)

    def get_reviews_for_hotel(self, hotel_id: int) -> list[Review]:
        raw_reviews = self.dal.get_reviews_by_hotel(hotel_id)
        review_list = []

        for r in raw_reviews:
            review = Review(
                review_id=r["id"],
                guest_id=r["guest_id"],
                hotel_id=hotel_id,
                rating=r["rating"],
                comment=r["comment"],
                review_date=r["review_date"]
            )
            review_list.append(review)

        return review_list
