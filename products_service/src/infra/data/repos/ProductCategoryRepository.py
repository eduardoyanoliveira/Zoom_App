from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.exc import SQLAlchemyError 

from infra.data.models.models import ProductCategoryModel
from domain.entities.Product import ProductCategory

class ProductCategoryRepository(AbstractProductCategoryRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, category_id: int) -> ProductCategory:
        mapped = self.db.query(ProductCategoryModel).get(category_id)
        if mapped:
            return self._map_to_domain_entity(mapped)
        return None

    def create(self, product_category: ProductCategory) -> ProductCategory:
        try:
            mapped = ProductCategoryModel(name=product_category.name)
            self.db.add(mapped)
            self.db.commit()
            self.db.refresh(mapped)
            return self._map_to_domain_entity(mapped)
        except SQLAlchemyError as e:
            self.db.rollback()
            raise e
    
    def list(self) -> List[ProductCategory]:
        mapped_categories = self.db.query(ProductCategoryModel).all()
        return [self._map_to_domain_entity(mapped) for mapped in mapped_categories]

    def _map_to_domain_entity(self, mapped: ProductCategoryModel) -> ProductCategory:
        return ProductCategory(
            id=mapped.id,
            created_at=mapped.created_at,
            updated_at=mapped.updated_at,
            name=mapped.name
        )