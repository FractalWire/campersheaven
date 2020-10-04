import unittest
import tempfile


class TestEngine(unittest.TestCase):

    datadir = "tests/data"
    with open(f"{datadir}/empty_camper.json") as f:
        empty_data = f.read()
    with open(f"{datadir}/correct_camper.json") as f:
        correct_camper_data = f.read()
    with open(f"{datadir}/correct_campers.json") as f:
        correct_campers_data = f.read()

    def setUp(self):
        self.ds = DictionaryStore(Camper)
        self.engine = Engine(self.ds)

    def test_insert_empty_data(self):
        self.engine.insert_data(empty_data)
        self.assertDictEqual(self.ds.store, {})

    def test_insert_data(self):
        self.engine.insert_data(correct_camper_data)
        self.assertDictEqual(
            self.ds.store,
            {
                1: {
                    "latitude": 44.8637834,
                    "longitude": -0.6211603
                }
            })

    with open(f"{datadir}/search_one.json") as f:
        search_one = f.read()
    with open(f"{datadir}/search_many.json") as f:
        search_many = f.read()

    def test_search_emptystore(self):
        results = self.search(search_one)
        with open(f"{datadir}/empty_results.json") as f:
            self.assertEqual(
                results,
                f.read()
            )

    def test_search_one(self):
        self.engine.insert_data(correct_camper_data)
        results = self.search(search_one)
        with open(f"{datadir}/results_one.json") as f:
            self.assertEqual(
                results,
                f.read()
            )

    def test_search_many(self):
        self.engine.insert_data(correct_campers_data)
        results = self.search(search_many)
        with open(f"{datadir}/results_many.json") as f:
            self.assertEqual(
                results,
                f.read()
            )
