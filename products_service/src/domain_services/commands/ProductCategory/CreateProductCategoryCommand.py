from contracts.ProductCategoryContracts.CreateProductCategory import CreateProductCategoryRequest
from domain.entities.Product import ProductCategory
from domain_services.Abstracts.ProductCategory.AbstractCreateProductCategoryCommand import AbstractCreateProductCategoryCommand
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository


class CreateProductCategoryCommand(AbstractCreateProductCategoryCommand):

    def __init__(self, product_category_repository: AbstractProductCategoryRepository) -> None:
        self._product_category_repository = product_category_repository
    
    def execute(self, request: CreateProductCategoryRequest) -> ProductCategory:
        product_category: ProductCategory = ProductCategory(name= request.name)
        
        return self._product_category_repository.create(product_category)