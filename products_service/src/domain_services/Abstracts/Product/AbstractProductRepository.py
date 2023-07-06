from abc import ABC, abstractmethod
from typing import List
from domain.entities.Product import Product

class AbstractProductRepository(ABC):
    @abstractmethod
    def list(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod    
    def create_product(self, product: Product) -> Product:
        pass