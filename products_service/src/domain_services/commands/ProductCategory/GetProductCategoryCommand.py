from domain_services.Abstracts.ProductCategory.AbstractGetProductCategoryCommand import AbstractGetProductCategoryCommand
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository


class GetProductCategoryCommand(AbstractGetProductCategoryCommand):

    def __init__(self, product_category_repository: AbstractProductCategoryRepository) -> None:
        self._product_category_repository = product_category_repository

    def execute(self, category_id: int):
        return self._product_category_repository.get(category_id)