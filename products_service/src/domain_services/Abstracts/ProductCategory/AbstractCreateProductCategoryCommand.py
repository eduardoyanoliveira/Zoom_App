from abc import ABC, abstractmethod

from contracts.ProductCategoryContracts.CreateProductCategory import CreateProductCategoryRequest
from domain.entities.Product import ProductCategory

class AbstractCreateProductCategoryCommand(ABC):
    @abstractmethod
    def execute(self, request: CreateProductCategoryRequest) -> ProductCategory:
        pass