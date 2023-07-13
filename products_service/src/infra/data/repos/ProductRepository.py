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
        mapped = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        return self._map_to_domain_entity(mapped)


    def create_product(self, product: Product) -> Product:
        try:
            mapped_product = ProductModel(
                id=product.id,
                name=product.name,
                base_price=product.base_price,
                amount=product.amount,
                is_stored=product.is_stored,
                category_id=product.category.id
            )
            self.db.add(mapped_product)
            self.db.commit()
            self.db.refresh(mapped_product)
            return mapped_product
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e
    
    
    def list(self) -> List[Product]:
        mapped_products = self.db.query(ProductModel).all()
        return [self._map_to_domain_entity(mapped) for mapped in mapped_products]
    
    def _map_to_domain_entity(self, mapped: ProductModel) -> Product:
        return Product(
            id=mapped.id,
            created_at=mapped.created_at,
            updated_at=mapped.updated_at,
            name=mapped.name,
            amount = mapped.amount,
            base_price = mapped.base_price,
            category = mapped.category,
            is_stored= mapped.is_stored
        )