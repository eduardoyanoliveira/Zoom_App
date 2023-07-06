from contracts.ProductContracts.CreateProductRequest import CreateProductRequest
from domain.entities.Product import Product
from domain_services.Abstracts.Product.AbstractCreateProductCommand import AbstractCreateProductCommand
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
import datetime

from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository

class CreateProductCommand(AbstractCreateProductCommand):
    _product_repository: AbstractProductRepository
    _category_repository: AbstractProductCategoryRepository

    def execute(self, request: CreateProductRequest) -> Product:
        is_stored = request.amount is not None

        # Retrieve the category object from the repository
        category = self._category_repository.get_category_by_id(request.category_id)

        product = Product(
            id=request.id,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            name=request.name,
            base_price=request.base_price,
            amount=request.amount,
            is_stored=is_stored,
            category=category
        )

        return self._product_repository.create_product(product)