from abc import ABC, abstractmethod
from contracts.ProductContracts.CreateProductRequest import CreateProductRequest
from domain.entities.Product import Product

class AbstractCreateProductCommand(ABC):
    @abstractmethod
    def execute(self, request: CreateProductRequest) -> Product:
        pass
