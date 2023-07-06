from abc import ABC, abstractmethod
from typing import int, List

from domain.entities.Product import ProductCategory

class AbstractProductCategoryRepository(ABC):
    
    @abstractmethod
    def create(self, product_category: ProductCategory) -> ProductCategory:
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int) -> ProductCategory:
        pass

    @abstractmethod
    def list(self) -> List[ProductCategory]:
        pass