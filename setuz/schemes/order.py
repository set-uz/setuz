from dataclasses import dataclass
from .base_schema import MainSchema
from datetime import datetime
from typing import Optional, List


@dataclass
class Product:
    provider_product_id: Optional[int]
    name: str


@dataclass
class OrderProductSchema:
    id: int
    total_price: float
    quantity: int
    product: Product


@dataclass
class OrderSchema:
    id: int
    tm: int
    total_price: float
    status: str
    order_products: List[OrderProductSchema]
    created_date: datetime


@dataclass
class OrderListSchema(MainSchema):
    results: List[OrderSchema]
