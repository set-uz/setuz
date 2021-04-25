from dataclasses import dataclass
from .base_schema import MainSchema
from typing import List


@dataclass
class MeasurementSchema:
    id: int
    name: str
    short_name: str
    tm: int


@dataclass
class MeasurementListSchema(MainSchema):
    results: List[MeasurementSchema]
