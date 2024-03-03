from typing import List

from pydantic import BaseModel


class FavoritesGetItemModel(BaseModel):
    id: List[int]
    artnum: List[str]
