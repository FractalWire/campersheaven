import unittest

from datetime import datetime

from campersheaven.models import Camper


class TestModels(unittest.TestCase):
    def test_dates_price(self):
        start_date = datetime.fromisoformat('2020-01-01')
        end_date = datetime.fromisoformat('2020-01-02')
        date_range = (start_date, end_date)

        camper1 = Camper(**{
            "id": 3,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "price_per_day": 85.5,
            "weekly_discount": 0.25
        })
        self.assertEqual(
            camper1.dates_price(*date_range),
            171.0
        )

        end_date = datetime.fromisoformat('2020-01-08')
        date_range = (start_date, end_date)
        self.assertEqual(
            camper1.dates_price(*date_range),
            513.0
        )

        camper2 = Camper(**{
            "id": 3,
            "latitude": 38.7436883,
            "longitude": -9.1952226,
            "price_per_day": 85.5
        })
        self.assertEqual(
            camper2.dates_price(*date_range),
            684.0
        )
