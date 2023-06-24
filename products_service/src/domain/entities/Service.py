from pydantic import validator
from domain.entities.BaseEntity import BaseEntity

from domain.entities.Product import Product


class ServiceCategory(BaseEntity):
    id: int
    name: str


class ServiceProduct(BaseEntity):
    id: int
    product: Product
    amount: int
    price: float 

    @validator('price', pre=True, always=True)
    def set_default_price(cls, price, values):
        if price is None:
            product = values.get('product')
            if product:
                return product.base_price
        return price


class Service(BaseEntity):
    id: int
    name: str
    products: list[ServiceProduct]
    category: ServiceCategory
