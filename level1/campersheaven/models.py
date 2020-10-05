from __future__ import annotations
from typing import Union
from dataclasses import dataclass, InitVar

from .geometries import Point


@dataclass
class Camper:
    id: int
    latitude: InitVar[float] = None
    longitude: InitVar[float] = None
    point: Point = None

    def __post_init__(self, latitude: float, longitude: float) -> None:
        if latitude and longitude:
            self.point = Point(longitude, latitude)


"""ModelType is a dataclass, can't specify that"""
ModelType = Union[Camper]
