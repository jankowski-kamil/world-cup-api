from enum import StrEnum
from pydantic import BaseModel


class TableModel(BaseModel):
    name: str
    total_points: int


class SortType(StrEnum):
    asc = "asc"
    desc = "desc"
