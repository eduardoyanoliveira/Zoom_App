from typing import List
from domain.entities.Product import Product
from domain_services.Abstracts.Product.AbstractListProductsCommand import AbstractListProductsCommand
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository


class ListProductsCommand(AbstractListProductsCommand):

    def __init__(self, product_repository: AbstractProductRepository) -> None:
        self._product_repository = product_repository

    def execute(self) -> List[Product]:
        return self._product_repository.list()