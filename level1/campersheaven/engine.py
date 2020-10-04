from __future__ import annotations
from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Camper


class Engine:
    def __init__(self, store: Dict[int, Camper]):
        self.store = store

    def insert_data(self, data: Dict[str, Any]):
        pass

    def search(self, search_query: Dict[str, Any]):
        pass
