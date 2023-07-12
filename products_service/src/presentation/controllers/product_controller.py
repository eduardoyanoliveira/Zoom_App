from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from contracts.ProductCategoryContracts.CreateProductCategory import \
    CreateProductCategoryRequest
from contracts.ProductContracts.CreateProductRequest import \
    CreateProductRequest
from domain_services.DependencyInjectionContainer import (
    provide_create_product_category_command, provide_create_product_command,
    provide_get_product_category_command, provide_get_product_command,
    provide_list_product_category_command, provide_list_products_command)
from infra.DependencyInjectionContainer import get_db

product_router = APIRouter()

@product_router.get("/products")
def index(db: Session = Depends(get_db)):
    command = provide_list_products_command(db)
    products = command.execute()
    return products

@product_router.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    result = provide_get_product_command(db).execute(id)
    return {"product": result}

@product_router.post("/products")
def create_product(request: CreateProductRequest, db: Session = Depends(get_db)):
    result = provide_create_product_command(db).execute(request)
    return {"product": result}

@product_router.post("/product_categories")
def create_product_category(
        request: CreateProductCategoryRequest, 
        db: Session = Depends(get_db)   
    ):
    result = provide_create_product_category_command(db).execute(request)
    return {"product_category": result}

@product_router.get("/product_categories/{id}")
def get_product_category(id: int, db: Session = Depends(get_db)):
    result = provide_get_product_category_command(db).execute(id)
    return {"product_category": result}

@product_router.get("/product_categories")
def get_product_category(db: Session = Depends(get_db)):
    result = provide_list_product_category_command(db).execute()
    return {"product_categories": result}