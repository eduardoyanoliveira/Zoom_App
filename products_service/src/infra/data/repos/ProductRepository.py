from typing import List
import datetime
from sqlalchemy.orm import Session

from domain.entities.Product import Product, ProductCategory
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from infra.data.models.ProductModel import ProductModel

product_categories : List[ProductCategory] = [
    ProductCategory(        
        id=1,
        created_at=datetime.datetime.now(), 
        updated_at=datetime.datetime.now(), 
        name="tools"
    ),
    ProductCategory(
        id=2,
        created_at=datetime.datetime.now(), 
        updated_at=datetime.datetime.now(), 
        name="eletronic"
    ),
]

products: List[Product] = [
    Product(
        id=0,
        created_at=datetime.datetime.now(), 
        updated_at=datetime.datetime.now(), 
        name="Hammer", 
        base_price=9.99, 
        amount=20, 
        is_stored=True, 
        category=product_categories[0]
    ),
    Product(
        id=1,
        created_at=datetime.datetime.now(), 
        updated_at=datetime.datetime.now(), 
        name="Saw", 
        base_price=39.99, 
        amount=10, 
        is_stored=True, 
        category=product_categories[0]
    ),
    Product(
        id=2,
        created_at=datetime.datetime.now(), 
        updated_at=datetime.datetime.now(), 
        name="Computer", 
        base_price=700.99, 
        amount=15, 
        is_stored=True, 
        category=product_categories[1]
    ),
]


class ProductRepository(AbstractProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int) -> Product:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def list(self) -> List[Product]:
        return self.db.query(Product).all()


# class ProductRepository(AbstractProductRepository):

#     def get_all_products(self) -> List[Product]:
#         return products