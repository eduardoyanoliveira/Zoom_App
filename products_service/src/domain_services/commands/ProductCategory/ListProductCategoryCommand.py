from domain_services.Abstracts.ProductCategory.AbstractListProductCategoryCommand import AbstractListProductCategoryCommand
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository


class ListProductCategoryCommand(AbstractListProductCategoryCommand):

    def __init__(self, product_category_repository: AbstractProductCategoryRepository) -> None:
        self._product_category_repository = product_category_repository

    def execute(self):
        return self._product_category_repository.list()