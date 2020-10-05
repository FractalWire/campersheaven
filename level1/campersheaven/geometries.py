from __future__ import annotations
from typing import NamedTuple, Tuple

SRID_4326_BOUNDARIES = (-180.0, 180.0, -90.0, 90.0)


class Point(NamedTuple):
    x: float
    y: float

    def valid(self) -> bool:
        """Wether or not the Point is a valid one"""
        srid_xmin, srid_xmax, srid_ymin, srid_ymax = SRID_4326_BOUNDARIES
        return (srid_xmin <= self.x <= srid_xmax) and (srid_ymin <= self.y <= srid_ymax)

    def bbox(self, bbox_diff: Tuple) -> Bbox:
        """Output a valid Bbox"""
        srid_xmin, srid_xmax, srid_ymin, srid_ymax = SRID_4326_BOUNDARIES
        xmin, xmax, ymin, ymax = bbox_diff
        return Bbox(
            max(self.x+xmin, srid_xmin),
            min(self.x+xmax, srid_xmax),
            max(self.y+ymin, srid_ymin),
            min(self.y+ymax, srid_ymax)
        )

    def within(self, bbox: Bbox) -> bool:
        """Wether or not the point is in bbox"""
        xmin, xmax, ymin, ymax = bbox
        return (xmin <= self.x <= xmax) and (ymin <= self.y <= ymax)


class Bbox(NamedTuple):
    xmin: float
    xmax: float
    ymin: float
    ymax: float

    def valid(self) -> bool:
        """Wether or not the Bbox is a valid one"""
        srid_xmin, srid_xmax, srid_ymin, srid_ymax = SRID_4326_BOUNDARIES
        return all([
            (srid_xmin <= self.xmin <= srid_xmax),
            (srid_xmin <= self.xmax <= srid_xmax),
            (srid_ymin <= self.ymin <= srid_ymax),
            (srid_ymin <= self.ymax <= srid_ymax)
        ])
