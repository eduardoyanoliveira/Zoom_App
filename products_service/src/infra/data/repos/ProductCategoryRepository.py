from domain.entities.Product import ProductCategory
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository
from sqlalchemy.orm import Session
from typing import List, int

class ProductCategoryRepository(AbstractProductCategoryRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_category_id: int) -> ProductCategory:
        return self.db.query(ProductCategory).filter(ProductCategory.id == product_category_id).first()

    def create_product(self, product_category: ProductCategory) -> ProductCategory:
        self.db.add(product_category)
        self.db.commit()
        self.db.refresh(product_category)
        return product_category
    
    def list(self) -> List[ProductCategory]:
        return self.db.query(ProductCategory).all()
