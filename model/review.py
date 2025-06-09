class Review:
    """
    Model Class Review
    """

    def __init__(self, review_id: int, guest_id: int, hotel_id: int,
                 rating: int, comment: str, review_date: str):
        if not isinstance(review_id, int) or review_id < 0:
            raise ValueError("Review ID must be a positive integer")
        if not isinstance(guest_id, int) or guest_id < 0:
            raise ValueError("Guest ID must be a positive integer")
        if not isinstance(hotel_id, int) or hotel_id < 0:
            raise ValueError("Hotel ID must be a positive integer")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        if not isinstance(comment, str):
            raise ValueError("Comment must be a string")
        if not isinstance(review_date, str):
            raise ValueError("Review date must be a string")

        self.__review_id = review_id
        self.__guest_id = guest_id
        self.__hotel_id = hotel_id
        self.__rating = rating
        self.__comment = comment
        self.__review_date = review_date

    @property
    def review_id(self):
        return self.__review_id

    @property
    def guest_id(self):
        return self.__guest_id

    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5")
        self.__rating = value

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        if not isinstance(value, str):
            raise ValueError("Comment must be a string")
        self.__comment = value

    @property
    def review_date(self):
        return self.__review_date

    def __str__(self):
        return (f"Review[{self.__review_id}] Guest {self.__guest_id} rated Hotel {self.__hotel_id} "
                f"{self.__rating}★ on {self.__review_date} - \"{self.__comment}\"")
