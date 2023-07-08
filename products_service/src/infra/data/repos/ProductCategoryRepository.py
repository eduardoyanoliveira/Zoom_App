from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository
from sqlalchemy.orm import Session
from typing import List

from infra.data.models.models import ProductCategory


class ProductCategoryRepository(AbstractProductCategoryRepository):
    
    def __init__(self, db: Session):
        self.db = db

    def get(self, category_id: int) -> ProductCategory:
        return self.db.query(ProductCategory).filter(ProductCategory.id == category_id).first()

    def create(self, product_category: ProductCategory) -> ProductCategory:
        self.db.add(product_category)
        self.db.commit()
        self.db.refresh(product_category)
        return product_category
    
    def list(self) -> List[ProductCategory]:
        return self.db.query(ProductCategory).all()