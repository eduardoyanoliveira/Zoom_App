from pydantic import BaseModel
from typing import str

class CreateProductCategoryRequest(BaseModel):
    name: str