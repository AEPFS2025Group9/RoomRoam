class Facility:
    """
    Model Class Facility
    """

    def __init__(self, id: int, name: str, description: str):
        self._id = id
        self._name = name
        self._description = description

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    def __str__(self):
        return f"{self._name}: {self._description}"
