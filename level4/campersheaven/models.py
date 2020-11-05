from __future__ import annotations
from typing import Union, Set
from dataclasses import dataclass, InitVar, field
from datetime import datetime
from weakref import WeakSet

from .geometries import Point


@dataclass(frozen=True)
class Camper:
    id: int
    latitude: InitVar[float]
    longitude: InitVar[float]
    price_per_day: float
    weekly_discount: float = 0.0
    point: Point = field(init=False)
    calendars: Set[Calendar] = field(default_factory=WeakSet)

    def __post_init__(self, latitude: float, longitude: float) -> None:
        # this is not working which is weird because init=False
        # self.point = Point(longitude, latitude)
        super().__setattr__('point', Point(longitude, latitude))
        assert self.point.valid()

    def price(self, start_date: datetime = None, end_date: datetime = None) -> float:
        """Get the price for the `Camper` between `start_date` and `end_date`"""
        if not start_date:
            return self.price_per_day

        tdelta = end_date - start_date
        discount_rate = (1 - (self.weekly_discount if tdelta.days >= 7 else 0))
        return (self.price_per_day * (tdelta.days + 1)) * discount_rate

    def isavailable(
            self, start_date: datetime, end_date: datetime) -> bool:
        """Check wether or not the `Camper` is available between `start_date` and
        `end_date`"""
        return all(c.isdaterange_overlaps(start_date, end_date) for c in
                   self.calendars)


@dataclass(frozen=True)
class Search:
    id: int
    latitude: InitVar[float]
    longitude: InitVar[float]
    point: Point = field(init=False)
    start_date: datetime = None
    end_date: datetime = None

    def __post_init__(self, latitude: float, longitude: float) -> None:
        # self.point = Point(longitude, latitude)
        super().__setattr__('point', Point(longitude, latitude))
        assert self.point.valid()

        if (isinstance(self.start_date, str)):
            super().__setattr__(
                'start_date',
                datetime.fromisoformat(self.start_date)
            )
        if (isinstance(self.end_date, str)):
            super().__setattr__(
                'end_date',
                datetime.fromisoformat(self.end_date)
            )


@ dataclass(frozen=True)
class Calendar:
    id: int
    camper_id: int
    camper_is_available: bool
    start_date: datetime
    end_date: datetime

    def __post_init__(self) -> None:
        if (isinstance(self.start_date, str)):
            super().__setattr__(
                'start_date',
                datetime.fromisoformat(self.start_date)
            )
        if (isinstance(self.end_date, str)):
            super().__setattr__(
                'end_date',
                datetime.fromisoformat(self.end_date)
            )

    def isdaterange_overlaps(
            self, start_date: datetime, end_date: datetime) -> bool:
        """Check wether or not Calendar daterange overlaps daterange provided"""
        return any([
            self.start_date <= start_date <= self.end_date,
            self.start_date <= end_date <= self.end_date,
            start_date < self.start_date and end_date > self.end_date
        ])


"""ModelType is a dataclass, can't specify that"""
ModelType = Union[Camper, Search, Calendar]
