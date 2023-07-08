from pydantic import BaseModel
from typing import Any, Optional
from domain.entities.BaseEntity import BaseEntity

class ProductCategory(BaseModel):
    id: int
    name: str

class Product(BaseEntity):
    id: int
    name: str
    base_price: float
    category: ProductCategory
    is_stored: bool
    amount: Optional[int]
