from __future__ import annotations
from typing import List, Dict, Any, Callable, TYPE_CHECKING
from dataclasses import replace

if TYPE_CHECKING:
    from .models import ModelType


class DictionaryStore:
    def __init__(self, model: ModelType) -> None:
        self.model = model
        self.store: Dict[int, ModelType] = dict()

    def upsert_data(self, data: List[Dict[str, Any]]) -> None:
        pass

    def upsert(self, row: Dict[str, Any]) -> None:
        id_ = row["id"]
        if id_ in self.store:
            self.store[id_] = replace(self.store[id_], **row)
        else:
            self.store[id_] = self.model(**row)

    def filter(self, predicate: Callable[[ModelType], bool]) -> List[ModelType]:
        return [item for item in self.store if predicate(item)]
