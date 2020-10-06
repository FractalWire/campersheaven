from __future__ import annotations
from typing import Union, TYPE_CHECKING
from dataclasses import dataclass, InitVar
from datetime import datetime

from .geometries import Point


@dataclass
class Camper:
    id: int
    price_per_day: float
    weekly_discount: float = 0.0
    latitude: InitVar[float] = None
    longitude: InitVar[float] = None
    point: Point = None

    def __post_init__(self, latitude: float, longitude: float) -> None:
        if(latitude and longitude):
            self.point = Point(longitude, latitude)
        assert self.point

    def search_price(self, search: Search) -> float:
        """Get the price for the `Camper` between `start_date` and `end_date`"""
        if not search.start_date:
            return self.price_per_day

        tdelta = search.end_date - search.start_date
        discount_rate = (1 - (self.weekly_discount if tdelta.days >= 7 else 0))
        return (self.price_per_day * (tdelta.days + 1)) * discount_rate


@dataclass
class Search:
    id: int
    latitude: InitVar[float] = None
    longitude: InitVar[float] = None
    point: Point = None
    start_date: datetime = None
    end_date: datetime = None

    def __post_init__(self, latitude: float, longitude: float) -> None:
        if(latitude and longitude):
            self.point = Point(longitude, latitude)
        assert self.point

        if (isinstance(self.start_date, str)):
            self.start_date = datetime.fromisoformat(self.start_date)
        if (isinstance(self.end_date, str)):
            self.end_date = datetime.fromisoformat(self.end_date)


"""ModelType is a dataclass, can't specify that"""
ModelType = Union[Camper]
