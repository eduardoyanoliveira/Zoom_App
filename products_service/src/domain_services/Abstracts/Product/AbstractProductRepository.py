from abc import ABC, abstractmethod
from typing import List
from domain.entities.Product import Product

class AbstractProductRepository(ABC):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass
