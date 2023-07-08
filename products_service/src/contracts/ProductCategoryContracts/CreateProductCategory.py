from pydantic import BaseModel

class CreateProductCategoryRequest(BaseModel):
    name: str