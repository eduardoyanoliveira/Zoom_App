from domain_services.Abstracts.Product.AbstractCreateProductCommand import AbstractCreateProductCommand
from domain_services.Abstracts.Product.AbstractListProductsCommand import AbstractListProductsCommand
from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from domain_services.Abstracts.ProductCategory.AbstractCreateProductCategoryCommand import AbstractCreateProductCategoryCommand
from domain_services.Abstracts.ProductCategory.AbstractGetProductCategoryCommand import AbstractGetProductCategoryCommand
from domain_services.Abstracts.ProductCategory.AbstractListProductCategoryCommand import AbstractListProductCategoryCommand
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository
from domain_services.commands.Product.CreateProductCommand import CreateProductCommand
from domain_services.commands.Product.GetProductCommand import GetProductCommand
from domain_services.commands.Product.ListProductsCommand import ListProductsCommand
from domain_services.commands.ProductCategory.CreateProductCategoryCommand import CreateProductCategoryCommand
from domain_services.commands.ProductCategory.GetProductCategoryCommand import GetProductCategoryCommand
from domain_services.commands.ProductCategory.ListProductCategoryCommand import ListProductCategoryCommand
from infra.DependencyInjectionContainer import provide_product_category_repository, provide_product_repository
from sqlalchemy.orm import Session

def provide_create_product_category_command(db: Session) -> AbstractCreateProductCategoryCommand:
    product_category_repository : AbstractProductCategoryRepository = provide_product_category_repository(db)
    return CreateProductCategoryCommand(product_category_repository)

def provide_get_product_category_command(db: Session) -> AbstractGetProductCategoryCommand:
    product_category_repository : AbstractProductCategoryRepository = provide_product_category_repository(db)
    return GetProductCategoryCommand(product_category_repository)

def provide_list_product_category_command(db: Session) -> AbstractListProductCategoryCommand:
    product_category_repository : AbstractProductCategoryRepository = provide_product_category_repository(db)
    return ListProductCategoryCommand(product_category_repository)

def provide_create_product_command(db: Session) -> AbstractCreateProductCommand:
    product_category_repository : AbstractProductCategoryRepository = provide_product_category_repository(db)
    product_repository : AbstractProductRepository = provide_product_repository(db)
    return CreateProductCommand(product_repository, product_category_repository)

def provide_list_products_command(db: Session) -> AbstractListProductsCommand:
    product_repository : AbstractProductRepository = provide_product_repository(db)
    return ListProductsCommand(product_repository)

def provide_get_product_command(db: Session) -> AbstractListProductsCommand:
    product_repository : AbstractProductRepository = provide_product_repository(db)
    return GetProductCommand(product_repository)

