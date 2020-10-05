from __future__ import annotations
from typing import List, Dict, Any, Callable, Union, TYPE_CHECKING
from dataclasses import replace

if TYPE_CHECKING:
    from .models import ModelType, Camper
    from .geometries import Position


class DictionaryStore:
    """Implement a simple store capable of doing operations comparable to a DB"""

    def __init__(self, model: Callable[[Dict[str, Any]], ModelType]) -> None:
        self.model: Callable[[Dict[str, Any]], ModelType] = model
        self.store: Dict[int, ModelType] = dict()

    def upsert_data(self, data: List[Dict[str, Any]]) -> None:
        """Upsert data to the store, i.e. insert if id does not exists, update otherwise"""
        for row in data:
            self.upsert(row)

    def upsert(self, row: Dict[str, Any]) -> None:
        """Upsert row to the store, i.e. insert if id does not exists, update otherwise"""
        id_ = row["id"]
        if id_ in self.store:
            self.store[id_] = replace(self.store[id_], **row)
        else:
            self.store[id_] = self.model(**row)

    def filter(self, predicate: Callable[[ModelType], bool]) -> List[ModelType]:
        """Filter store content based on a predicate operating on every rows of
        the store.
        This allow SELECT-like operations with ease"""
        return [item for item in self.store.values() if predicate(item)]


DataStore = Union[DictionaryStore]


class DataStoreAccess:
    """Abstraction layer to access various DataStore"""

    @staticmethod
    def populate_campers(store: DataStore, data: Dict[str, Any]) -> None:
        """Populate data into store"""
        # store.upsert_data(data)
        pass

    @staticmethod
    def find_campers_around(store: DataStore, position: Position) -> List[Camper]:
        """Find the campers in the store that are in a 2 degrees square bounding box
        around position"""
        def filter_position(camper: Camper) -> bool:
            bbox = position.bbox((-0.1, 0.1, -0.1, -0.1,))
            return camper.position.within(bbox)

        return store.filter(filter_position)
