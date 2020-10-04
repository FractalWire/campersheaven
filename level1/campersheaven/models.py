from dataclasses import dataclass, InitVar

from .geometries import Point


@dataclass
class Camper:
    id: int
    latitude: InitVar[float] = None
    longitude: InitVar[float] = None
    point: Point = None

    def __post_init__(self, latitude, longitude):
        if latitude and longitude:
            self.point = Point(longitude, latitude)
