from __future__ import annotations
from typing import List, Tuple, TYPE_CHECKING
import json

from .models import Search, Camper

SearchCampersTuple = Tuple[Search, List[Camper]]
ViewData = List[SearchCampersTuple]


class View:
    @classmethod
    def render(cls, view_data: ViewData) -> ByteString:
        """Render the search view based on search_id and campersresults
        associated to this search"""
        return json.dumps(cls._render_many(view_data))

    @classmethod
    def _render_many(cls, view_data: ViewData) -> Dict[str, Any]:
        results = []
        for searchcampers_tuple in view_data:
            results.append(cls._render_one(searchcampers_tuple))
        return {"results": results}

    @classmethod
    def _render_one(cls, searchcampers_tuple: SearchCampersTuple) -> Dict[str, Any]:
        search, campers = searchcampers_tuple
        search_results = []
        date_range = (search.start_date, search.end_date)
        for camper in campers:
            search_results.append({
                "camper_id": camper.id,
                "price": camper.price(*date_range)
            })

        return {
            "search_id": search.id,
            "search_results": search_results
        }
