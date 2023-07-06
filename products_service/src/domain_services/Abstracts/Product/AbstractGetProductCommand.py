from abc import ABC, abstractmethod
from domain.entities.Product import Product

class AbstractGetProductsCommand(ABC):
    @abstractmethod
    def execute(self, id: int) -> Product:
        pass