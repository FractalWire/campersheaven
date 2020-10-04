from dataclasses import dataclass, InitVar


@dataclass
class Camper:
    id: int
    latitude: InitVar[float] = None
    longitude: InitVar[float] = None
    point: Point = None

    def __post_init__(self):
        if latitude and longitude:
            self.point = Point(longitude, latitude)
