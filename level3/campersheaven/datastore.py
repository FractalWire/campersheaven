from __future__ import annotations
from typing import (
    List, Dict, Any, Callable, Union,
    NamedTuple, TYPE_CHECKING
)
from weakref import WeakSet
from dataclasses import replace

if TYPE_CHECKING:
    from .models import ModelType, Camper
    from .geometries import Point


class ForeignKeyDictionaryStore(NamedTuple):
    id: str
    store: DictionaryStore
    store_column: str


class DictionaryStore:
    """Implement a simple store capable of doing operations comparable to a DB"""

    def __init__(self, name: str, model: Callable[[Dict[str, Any]], ModelType],
                 foreign_keys=list()) -> None:
        self.name: str = name
        self.model: Callable[[Dict[str, Any]], ModelType] = model
        self.store: Dict[int, ModelType] = dict()
        self.foreign_keys: List[ForeignKeyDictionaryStore] = foreign_keys

    def upsert_data(self, data: List[Dict[str, Any]]) -> None:
        """Upsert data to the store, i.e. insert if id does not exists, update otherwise"""
        for row in data:
            self.upsert(row)

    def upsert(self, row: Dict[str, Any]) -> None:
        """Upsert row to the store, i.e. insert if id does not exists, update otherwise"""
        def update_fk_link(
                fk_ds: ForeignKeyDictionaryStore,
                row_model: ModelType) -> None:
            store = fk_ds.store.store
            assert id_ in store

            foreign_row = store[row[fk_ds.id]]
            fcs: WeakSet = foreign_row.__getattribute__(fk_ds.store_column)
            assert isinstance(fcs, WeakSet)

            fcs.add(row_model)

        id_ = row["id"]
        if id_ in self.store:
            self.store[id_] = replace(self.store[id_], **row)
        else:
            self.store[id_] = self.model(**row)

        for fk_ds in self.foreign_keys:
            try:
                update_fk_link(fk_ds, self.store[id_])
            except:
                self.store.pop(id_)
                print("update_fk_link failed")
                raise

    def filter(self, predicate: Callable[[ModelType], bool]) -> List[ModelType]:
        """Filter store content based on a predicate operating on every rows of
        the store.
        This allow SELECT-like operations with ease"""
        return [row for row in self.store.values() if predicate(row)]


DataStore = Union[DictionaryStore]


class DataStoreAccess:
    """Abstraction layer to access various DataStore"""

    @staticmethod
    def populate_store(store: DataStore, data: Dict[str, Any]) -> None:
        """Populate data into store"""
        store_data = data[store.name]
        store.upsert_data(store_data)

    @staticmethod
    def find_campers_around(store: DataStore, position: Point) -> List[Camper]:
        """Find the campers in the store that are in a 2 degrees square bounding box
        around position"""
        bbox = position.bbox((-0.1, 0.1, -0.1, 0.1,))

        return store.filter(lambda camper: camper.point.within(bbox))

    @classmethod
    def find_campers_by_price(
            cls, store: DataStore, position: Point, start_date: datetime, end_date: datetime
    ) -> List[Camper]:
        """Find the campers in the store that are in a 2 degrees square bounding box
        around position, sorted by price"""
        campers = cls.find_campers_around(store, position)
        return sorted(campers, key=lambda camper: camper.price(start_date, end_date))
