from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from infra.data.repos.ProductRepository import ProductRepository

def provide_product_repository() -> AbstractProductRepository:
    return ProductRepository()
