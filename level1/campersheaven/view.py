from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Camper


class View:
    def render(campers: List[Camper]):
        pass
