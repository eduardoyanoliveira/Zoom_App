from domain.entities.BaseEntity import BaseEntity

class ProductCategory(BaseEntity):
    id: int
    name: str


class Product(BaseEntity):
    id: int
    name: str
    base_price: float
    category: ProductCategory
