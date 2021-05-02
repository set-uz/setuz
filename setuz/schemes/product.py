from dataclasses import dataclass
from typing import List


@dataclass
class ProductImagesSchema:
    photo_id: int
    is_main: bool


@dataclass
class ProductCreateSchema:
    provider_product_id: int
    category_id: int
    brand_id: int
    measurement_id: int
    name: str
    description: str
    price: float
    cashback: int
    barcode: str
    product_images: List[ProductImagesSchema]
