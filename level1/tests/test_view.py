import unittest

from campersheaven.view import View
from campersheaven.models import Camper


class TestView(unittest.TestCase):
    datadir = "tests/data"

    def test_render_no_campers(self):
        results = View.render([])
        with open(f"{self.datadir}/empty_results.json") as f:
            self.assertEqual(
                results,
                f.read()
            )

    def test_render_one_camper(self):
        results = View.render([
            Camper(**{
                "id": 1,
                "latitude": 44.8637834,
                "longitude": -0.6211603
            })
        ])
        with open(f"{self.datadir}/results_one.json") as f:
            self.assertEqual(
                results,
                f.read()
            )

    def test_render_many_campers(self):
        results = View.render([
            Camper(**{
                "id": 1,
                "latitude": 44.8637834,
                "longitude": -0.6211603
            }),
            Camper(**{
                "id": 2,
                "latitude": 44.8313035,
                "longitude": -0.7169664
            }),
            Camper(**{
                "id": 3,
                "latitude": 38.7436883,
                "longitude": -9.1952226
            })
        ])
        with open(f"{self.datadir}/results_many.json") as f:
            self.assertEqual(
                results,
                f.read()
            )
