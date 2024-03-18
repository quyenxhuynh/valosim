from constants import Region


class Team:
    def __init__(self):
        self.id: int = 0
        self.name: str = None
        self.region: Region = Region.NONE
        self.country: str = None

    def __str__(self):
        return self.name