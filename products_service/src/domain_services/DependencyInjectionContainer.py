from domain_services.Abstracts.Product.AbstractCreateProductCommand import AbstractCreateProductCommand
from domain_services.Abstracts.Product.AbstractListProductsCommand import AbstractListProductsCommand
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository
from domain_services.commands.Product.CreateProductCommand import CreateProductCommand
from domain_services.commands.Product.ListProductsCommand import ListProductsCommand
from domain_services.commands.ProductCategory.CreateProductCategoryCommand import CreateProductCategoryCommand
from domain_services.commands.ProductCategory.GetProductCategoryCommand import GetProductCategoryCommand
from infra.DependencyInjectionContainer import provide_product_category_repository, provide_product_repository
from sqlalchemy.orm import Session

def provide_create_product_category_command(db: Session) -> AbstractCreateProductCommand:
    product_category_repository : AbstractProductCategoryRepository = provide_product_category_repository(db)
    return CreateProductCategoryCommand(product_category_repository)

def provide_get_product_category_command(db: Session) -> AbstractCreateProductCommand:
    product_category_repository : AbstractProductCategoryRepository = provide_product_category_repository(db)
    return GetProductCategoryCommand(product_category_repository)

# def provide_list_product_category_command(db: Session) -> A

def provide_create_product_command(db: Session) -> AbstractCreateProductCommand:
    product_repository : AbstractProductRepository = provide_product_repository(db)
    return CreateProductCommand(product_repository)

def provide_list_products_command(db: Session) -> AbstractListProductsCommand:
    product_repository : AbstractProductRepository = provide_product_repository(db)
    return ListProductsCommand(product_repository)



