from __future__ import annotations
from typing import Union, TYPE_CHECKING
from dataclasses import dataclass, InitVar
from datetime import datetime

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

    def search_price(self, search: Search) -> float:
        """Get the price for the `Camper` between `start_date` and `end_date`"""
        if not search.start_date:
            return self.price_per_day

        tdelta = search.end_date - search.start_date
        discount_rate = (1 - (self.weekly_discount if tdelta.days >= 7 else 0))
        return (self.price_per_day * tdelta.days) * discount_rate


"""ModelType is a dataclass, can't specify that"""
ModelType = Union[Camper]
