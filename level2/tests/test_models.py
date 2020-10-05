import unittest

from datetime import datetime

from campersheaven.models import Camper, Search


class TestModels(unittest.TestCase):
    def test_search_price(self):
        start_date = '2020-01-01'
        end_date = '2020-01-02'
        search1 = Search(**{
            "id": 1,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "start_date": start_date,
            "end_date": end_date
        })

        camper1 = Camper(**{
            "id": 3,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "price_per_day": 85.5,
            "weekly_discount": 0.25
        })
        self.assertEqual(
            camper1.search_price(search1),
            85.5
        )

        end_date = '2020-01-08'
        search2 = Search(**{
            "id": 2,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "start_date": start_date,
            "end_date": end_date
        })
        self.assertEqual(
            camper1.search_price(search2),
            448.875
        )

        camper2 = Camper(**{
            "id": 3,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "price_per_day": 85.5
        })
        self.assertEqual(
            camper2.search_price(search2),
            598.5
        )
