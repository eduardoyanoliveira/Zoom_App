from domain_services.Abstracts.Product.AbstractCreateProductCommand import AbstractCreateProductCommand
from domain_services.Abstracts.Product.AbstractListProductsCommand import AbstractListProductsCommand
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from domain_services.commands.Product.CreateProductCommand import CreateProductCommand
from domain_services.commands.Product.ListProductsCommand import ListProductsCommand
from infra.DependencyInjectionContainer import provide_product_repository

def provide_create_product_command() -> AbstractCreateProductCommand:
    return CreateProductCommand()

def provide_list_products_command() -> AbstractListProductsCommand:
    product_repository : AbstractProductRepository = provide_product_repository()
    return ListProductsCommand(product_repository)



