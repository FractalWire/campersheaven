from __future__ import annotations
from typing import Dict, Any, ByteString, TYPE_CHECKING

if TYPE_CHECKING:
    from .datastore import DictionaryStore


class Engine:
    """This class implement API-like interface for the camper search"""

    def __init__(self, store: DictionaryStore) -> None:
        self.store: DictionaryStore = store

    def insert_data(self, data: ByteString) -> None:
        """Insert new data to the store used by the Engine"""
        pass

    def search(self, search_query: ByteString) -> ByteString:
        """Search for matching campers based on a query"""
        pass
