from abc import ABC, abstractmethod
from typing import  List

from domain.entities.Product import ProductCategory

class AbstractProductCategoryRepository(ABC):
    
    @abstractmethod
    def create(self, product_category: ProductCategory) -> ProductCategory:
        pass

    @abstractmethod
    def get(self, category_id: int) -> ProductCategory:
        pass

    @abstractmethod
    def list(self) -> List[ProductCategory]:
        pass