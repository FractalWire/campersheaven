from random import uniform
from datetime import date
import factory
import factory.fuzzy
from faker.providers import BaseProvider

from campersheaven.models import Camper, Search, Calendar
from campersheaven.geometries import SRID_4326_BOUNDARIES

xmin, xmax, ymin, ymax = SRID_4326_BOUNDARIES
coordinates_precision = 5
price_precision = 2
daterange = (
    date.fromisoformat('2020-01-01'),
    date.fromisoformat('2021-01-01'),
)


class PercentProvider(BaseProvider):
    def percent(self, min_value=0, max_value=1, precision=None):
        if any(v < 0 or v > 1 for v in [min_value, max_value]):
            raise ValueError(
                "min_value and max_value must be a float between 0.0 and 1.0")
        if min_value > max_value:
            raise ValueError("min_value <= max_value condition not satisfied")

        if precision:
            return round(uniform(min_value, max_value), precision)
        return uniform(min_value, max_value)


fake = factory.Faker
fake.add_provider(PercentProvider)


class CamperFactory(factory.Factory):
    class Meta:
        model = Camper

    id = factory.Sequence(lambda n: n)
    latitude = fake('pyfloat', min_value=ymin,
                    max_value=ymax, right_digits=coordinates_precision)
    longitude = fake('pyfloat', min_value=xmin,
                     max_value=xmax, right_digits=coordinates_precision)
    price_per_day = fake(
        'pyfloat', min_value=50, max_value=300, right_digits=price_precision)
    weekly_discount = fake(
        'percent', max_value=0.5, precision=price_precision)


class SearchFactory(factory.Factory):
    class Meta:
        model = Search

    id = factory.Sequence(lambda n: n)
    latitude = fake('pyfloat', min_value=ymin,
                    max_value=ymax, right_digits=coordinates_precision)
    longitude = fake('pyfloat', min_value=xmin,
                     max_value=xmax, right_digits=coordinates_precision)
    start_date = fake(
        'date_between_dates',
        date_start=daterange[0],
        date_end=daterange[1]
    )

    @factory.lazy_attribute
    def end_date(self):
        return factory.fuzzy.FuzzyDate(
            self.start_date,
            daterange[1]
        ).fuzz()

    # /!\ Faker is not working properly here -> return date of today instead /!\
    # end_date = factory.LazyAttribute(lambda search: fake(
    #     'date_between_dates',
    #     date_start=daterange[0],
    #     date_end=daterange[1]
    # ).generate({'locale': None})
    # )
