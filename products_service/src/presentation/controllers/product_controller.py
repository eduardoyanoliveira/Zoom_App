from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from contracts.ProductCategoryContracts.CreateProductCategory import CreateProductCategoryRequest
from contracts.ProductContracts.CreateProductRequest import CreateProductRequest
from domain_services.Abstracts.ProductCategory.AbstractCreateProductCategoryCommand import AbstractCreateProductCategoryCommand


from domain_services.DependencyInjectionContainer import provide_create_product_category_command, provide_list_products_command
from infra.DependencyInjectionContainer import get_db, provide_product_category_repository, provide_product_repository

product_router = APIRouter()

@product_router.get("/")
def index(db: Session = Depends(get_db)):
    command = provide_list_products_command(db)
    products = command.execute()
    return products

@product_router.get("/products/{product_id}")
def get_product(pk: int, db: Session = Depends(get_db)):
    result = provide_product_repository(db).get_product_by_id(pk)
    return {"product": result}

@product_router.post("/products")
def create_product(request: CreateProductRequest, db: Session = Depends(get_db)):
    result = provide_product_repository(db).create_product(request)
    return {"product": result}

@product_router.post("/product_categories")
def create_product_category(
        request: CreateProductCategoryRequest, 
        db: Session = Depends(get_db)   
    ):
    result = provide_create_product_category_command(db).execute(request)
    return {"product_category": result}

@product_router.get("/product_categories/{product_category_id}")
def get_product_category(pk: int, db: Session = Depends(get_db)):
    result = provide_product_category_repository(db).get(pk)
    return {"product_category": result}