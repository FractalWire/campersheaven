import unittest
import json

from campersheaven.view import View
from campersheaven.models import Camper


class TestView(unittest.TestCase):
    datadir = "tests/data"

    def test_render_no_campers(self):
        results = View.render([
            (1, [])
        ])
        with open(f"{self.datadir}/empty_results.json") as f:
            self.assertEqual(
                json.loads(results),
                json.load(f)
            )

    def test_render_one_camper(self):
        camper3 = Camper(**{
            "id": 3,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "price_per_day": 0.0
        })
        results = View.render([
            (1, [camper3])
        ])
        with open(f"{self.datadir}/results_one.json") as f:
            self.assertDictEqual(
                json.loads(results),
                json.load(f)
            )

    def test_render_many_campers(self):
        camper1 = Camper(**{
            "id": 1,
            "latitude": 44.8637834,
            "longitude": -0.6211603,
            "price_per_day": 0.0
        })
        camper2 = Camper(**{
            "id": 2,
            "latitude": 44.8313035,
            "longitude": -0.7169664,
            "price_per_day": 0.0
        })
        camper3 = Camper(**{
            "id": 3,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "price_per_day": 0.0
        })
        results = View.render([
            (1, [camper3]),
            (2, [camper1, camper2]),
            (3, [])
        ])
        with open(f"{self.datadir}/results_many.json") as f:
            self.assertDictEqual(
                json.loads(results),
                json.load(f)
            )
