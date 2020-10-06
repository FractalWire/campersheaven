from __future__ import annotations
from typing import Dict, Any, ByteString, TYPE_CHECKING
import json

from .datastore import DataStoreAccess
from .view import View
from .geometries import Point
from .models import Search

if TYPE_CHECKING:
    from .datastore import DictionaryStore


class Engine:
    """This class implement API-like interface for the camper search"""

    def __init__(self, camper_store: DictionaryStore,
                 calendar_store: DictionaryStore) -> None:
        self.stores: Dict[DictionaryStore] = {
            camper_store.name: camper_store,
            calendar_store.name: calendar_store
        }

    def insert_data(self, data: ByteString) -> None:
        """Insert new data to the store used by the Engine"""
        d = json.loads(data)
        for store_name, store_data in d.items():
            DataStoreAccess.populate_store(self.stores[store_name], store_data)

    def search(self, search_query: ByteString) -> ByteString:
        """Search for matching campers based on a query"""
        d = json.loads(search_query)

        view_data = []
        for search_query in d["searches"]:
            search = Search(**search_query)

            campers = DataStoreAccess.find_available_campers(
                self.stores["campers"], search.point,
                search.start_date, search.end_date)

            searchcampers_tuple = (search, campers)
            view_data.append(searchcampers_tuple)

        return View.render(view_data)
