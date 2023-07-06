from domain.entities.Product import Product
from domain_services.Abstracts.Product.AbstractGetProductCommand import AbstractGetProductsCommand
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from typing import int

class GetProductCommand(AbstractGetProductsCommand):

    _product_repository: AbstractProductRepository

    def __init__(self, product_repository: AbstractProductRepository) -> None:
        self._product_repository = product_repository
    
    def execute(self, id: int) -> Product:
        return self._product_repository.get_product_by_id(id)