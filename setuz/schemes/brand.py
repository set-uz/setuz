from dataclasses import dataclass
from .base_schema import MainSchema
from typing import List


@dataclass
class BrandSchema:
    id: int
    name: str


@dataclass
class BrandListSchema(MainSchema):
    results: List[BrandSchema]
