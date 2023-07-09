from sqlalchemy.orm import Session
from typing import List
from domain.entities.Product import Product

from sqlalchemy.exc import SQLAlchemyError 

from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from infra.data.models.models import ProductModel


class ProductRepository(AbstractProductRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int) -> Product:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create_product(self, product: Product) -> Product:
        try:
            mapped_product = ProductModel(
                    id=product.id,
                    name=product.name,
                    base_price=product.base_price,
                    amount=product.amount,
                    is_stored=product.is_stored,
                    category=product.category
                )
            self.db.add(mapped_product)
            self.db.commit()
            self.db.refresh(mapped_product)
            return mapped_product
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e
    
    
    def list(self) -> List[Product]:
        return self.db.query(Product).all()