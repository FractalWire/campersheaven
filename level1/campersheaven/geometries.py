from __future__ import annotations
from typing import NamedTuple, Tuple


class Point(NamedTuple):
    x: float
    y: float

    def valid(self) -> bool:
        """Wether or not the Point is a valid one"""
        pass

    def bbox(self, bbox_diff: Tuple) -> Bbox:
        """Output a valid Bbox"""
        pass

    def within(self, bbox: Bbox) -> bool:
        pass


class Bbox(NamedTuple):
    x_min: float
    x_max: float
    y_min: float
    y_max: float

    def valid(self) -> bool:
        """Wether or not the Bbox is a valid one"""
        pass
