from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
import json

from .models import Camper

SearchCampersResult = Tuple[int, List[Camper]]
SearchCampersResults = List[SearchCampersResult]


class View:
    @classmethod
    def render(cls, search_campersresults: SearchCampersResults) -> ByteString:
        return json.dumps(cls._render_many(search_campersresults))

    @classmethod
    def _render_many(cls, search_campersresults: SearchCampersResults) -> Dict[str, Any]:
        results = []
        for search_campersresult in search_campersresults:
            results.append(cls._render_one(search_campersresult))
        return {"results": results}

    @classmethod
    def _render_one(cls, search_campersresult: SearchCampersResult) -> Dict[str, Any]:
        search_id, campers = search_campersresult
        search_results = []
        for camper in campers:
            search_results.append({
                "camper_id": camper.id
            })

        return {
            "search_id": search_id,
            "search_results": search_results
        }
