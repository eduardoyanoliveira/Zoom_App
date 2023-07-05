from contracts.ProductContracts.CreateProductRequest import CreateProductRequest
from domain.entities.Product import Product
from domain_services.Abstracts.Product.AbstractCreateProductCommand import AbstractCreateProductCommand


class CreateProductCommand(AbstractCreateProductCommand):

    def execute(self, product: CreateProductRequest) -> Product:
        return super().execute(product)