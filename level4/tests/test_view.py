import unittest
import json

from campersheaven.view import View
from campersheaven.models import Camper, Search


class TestView(unittest.TestCase):
    datadir = "tests/data"

    with open(f"{datadir}/correct_campers.json") as f:
        j = json.load(f)
        camper1, camper2, camper3 = [Camper(**c) for c in j["campers"]]
    with open(f"{datadir}/search_many.json") as f:
        j = json.load(f)
        search1, search2, search3 = [Search(**s) for s in j["searches"]]

    def test_render_no_campers(self):
        results = View.render([
            (self.search1, [])
        ])
        with open(f"{self.datadir}/empty_results.json") as f:
            self.assertEqual(
                json.loads(results),
                json.load(f)
            )

    def test_render_one_camper(self):
        results = View.render([
            (self.search1, [self.camper3])
        ])
        with open(f"{self.datadir}/results_one.json") as f:
            self.assertDictEqual(
                json.loads(results),
                json.load(f)
            )

    def test_render_many_campers(self):
        self.maxDiff = None
        results = View.render([
            (self.search1, [self.camper3]),
            (self.search2, [self.camper2, self.camper1]),
            (self.search3, [self.camper2, self.camper1])
        ])
        with open(f"{self.datadir}/results_many.json") as f:
            self.assertDictEqual(
                json.loads(results),
                json.load(f)
            )
