from sqlalchemy.orm import Session
from typing import List

from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from infra.data.models.models import Product


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