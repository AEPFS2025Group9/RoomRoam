class RoomType:
    """
   Model Class RoomType
    """

    def __init__(self, id: int, name: str, description: str, max_guests: int, price: float):
        self._id = id
        self._name = name
        self._description = description
        self._max_guests = max_guests
        self._price = price

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def max_guests(self) -> int:
        return self._max_guests

    @property
    def price(self) -> float:
        return self._price

    def __str__(self):
        return f"{self._name} ({self._max_guests} guests) - CHF {self._price:.2f}"
