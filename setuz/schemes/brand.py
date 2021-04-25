from dataclasses import dataclass
from .base_schema import MainSchema
from typing import List


@dataclass
class BrandSchema:
    id: int
    name: str
    tm: int


@dataclass
class BrandListSchema(MainSchema):
    results: List[BrandSchema]
