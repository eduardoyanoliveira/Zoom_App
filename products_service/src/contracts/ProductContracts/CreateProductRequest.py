from typing import Optional
from pydantic import BaseModel

class CreateProductRequest(BaseModel):
    name: str
    base_price: float
    category_id: int
    is_stored: bool
    amount: Optional[int]