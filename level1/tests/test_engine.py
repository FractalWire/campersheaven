import unittest
import tempfile

from campersheaven.engine import Engine
from campersheaven.datastore import DictionaryStore
from campersheaven.model import Camper


class TestEngine(unittest.TestCase):

    datadir = "tests/data"
    with open(f"{datadir}/empty_camper.json") as f:
        empty_data = f.read()
    with open(f"{datadir}/correct_camper.json") as f:
        correct_camper_data = f.read()
    with open(f"{datadir}/correct_campers.json") as f:
        correct_campers_data = f.read()

    def setUp(self):
        """Setup Engine with an associated DictionaryStore"""
        self.ds = DictionaryStore(Camper)
        self.engine = Engine(self.ds)

    def test_insert_empty_data(self):
        """Test insertion results of empty data"""
        self.engine.insert_data(self.empty_data)
        self.assertDictEqual(self.ds.store, {})

    def test_insert_data(self):
        """Test insertion results of correct data"""
        self.engine.insert_data(self.correct_camper_data)
        self.assertDictEqual(
            self.ds.store,
            {
                1: Camper(**{
                    "id": 1,
                    "latitude": 44.8637834,
                    "longitude": -0.6211603
                })
            })

    with open(f"{datadir}/search_one.json") as f:
        search_one = f.read()
    with open(f"{datadir}/search_many.json") as f:
        search_many = f.read()

    def test_search_emptystore(self):
        """Test search results in an empty store"""
        results = self.engine.search(self.search_one)
        with open(f"{self.datadir}/empty_results.json") as f:
            self.assertEqual(
                results,
                f.read()
            )

    def test_search_one(self):
        """Test search results giving only one result"""
        self.engine.insert_data(self.correct_camper_data)
        results = self.engine.search(self.search_one)
        with open(f"{self.datadir}/results_one.json") as f:
            self.assertEqual(
                results,
                f.read()
            )

    def test_search_many(self):
        """Test search results giving many results"""
        self.engine.insert_data(self.correct_campers_data)
        results = self.engine.search(self.search_many)
        with open(f"{self.datadir}/results_many.json") as f:
            self.assertEqual(
                results,
                f.read()
            )
