from __future__ import annotations
from typing import Dict, Any, ByteString, TYPE_CHECKING
import json

from .datastore import DataStoreAccess
from .view import View
from .geometries import Point

if TYPE_CHECKING:
    from .datastore import DictionaryStore


class Engine:
    """This class implement API-like interface for the camper search"""

    def __init__(self, store: DictionaryStore) -> None:
        self.store: DictionaryStore = store

    def insert_data(self, data: ByteString) -> None:
        """Insert new data to the store used by the Engine"""
        d = json.loads(data)
        DataStoreAccess.populate_campers(self.store, d)

    def search(self, search_query: ByteString) -> ByteString:
        """Search for matching campers based on a query"""
        d = json.loads(search_query)

        search_campersresults = []
        for search in d["searches"]:
            search_id = search["id"]
            lat = search["latitude"]
            lon = search["longitude"]

            position = Point(lon, lat)
            results_camper = DataStoreAccess.find_campers_around(
                self.store, position)
            search_campersresult = (search_id, results_camper)

            search_campersresults.append(search_campersresult)

        return View.render(search_campersresults)
