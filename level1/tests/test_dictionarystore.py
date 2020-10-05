from typing import Any
import unittest
from dataclasses import dataclass, asdict

from campersheaven.datastore import DictionaryStore


@dataclass
class DummyModel:
    id: int
    val: Any


class TestDictionaryStore(unittest.TestCase):
    def setUp(self):
        self.ds = DictionaryStore(DummyModel)

    def test_upsert_data_one(self):
        item1 = {"id": 1, "val": "bla"}
        data = [item1]

        self.ds.upsert_data(data)
        self.assertDictEqual(self.ds.store, {1: DummyModel(**item1)})

    def test_upsert_data_many(self):
        item1 = {"id": 1, "val": "bla"}
        item2 = {"id": 2, "val": "lab"}
        item3 = {"id": 3, "val": "alb"}
        data = [item1, item2, item3]

        self.ds.upsert_data(data)
        self.assertDictEqual(
            self.ds.store,
            {
                1: DummyModel(**item1),
                2: DummyModel(**item2),
                3: DummyModel(**item3),
            }
        )

    def test_upsert_insert(self):
        item = {"id": 1, "val": "bla"}
        self.ds.upsert(item)
        self.assertEqual(DummyModel(**item), self.ds.store[item["id"]])

    def test_upsert_update(self):
        item = {"id": 1, "val": "bla"}
        self.ds.upsert(item)

        changed_item = {"id": 1, "val": "lab"}
        self.ds.upsert(changed_item)

        self.assertEqual(DummyModel(**changed_item),
                         self.ds.store[item["id"]])

    def test_filter_false(self):
        item1 = {"id": 1, "val": "bla"}
        item2 = {"id": 2, "val": "lab"}
        item3 = {"id": 3, "val": "alb"}
        data = [item1, item2, item3]
        self.ds.upsert_data(data)

        results = self.ds.filter(lambda item: False)

        self.assertListEqual(results, [])

    def test_filter_true(self):
        item1 = {"id": 1, "val": "bla"}
        item2 = {"id": 2, "val": "lab"}
        item3 = {"id": 3, "val": "alb"}
        data = [item1, item2, item3]
        self.ds.upsert_data(data)

        results = self.ds.filter(lambda item: True)

        self.assertTrue(all(asdict(item) in data for item in results))

    def test_filter_by_field(self):
        item1 = {"id": 1, "val": "bla"}
        item2 = {"id": 2, "val": "lab"}
        item3 = {"id": 3, "val": "alb"}
        data = [item1, item2, item3]
        self.ds.upsert_data(data)

        results = self.ds.filter(lambda row: row.val == "bla" or row.id == 3)

        self.assertTrue(all(asdict(item) in [item1, item3] for item in results))
