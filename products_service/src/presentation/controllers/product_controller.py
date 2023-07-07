from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from contracts.ProductCategoryContracts.CreateProductCategory import CreateProductCategoryRequest
from contracts.ProductContracts.CreateProductRequest import CreateProductRequest
from typing import int

from domain_services.DependencyInjectionContainer import provide_list_products_command
from infra.DependencyInjectionContainer import get_db, provide_product_category_repository, provide_product_repository

product_router = APIRouter()

@product_router.get("/")
def index():
    command = provide_list_products_command()
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
def create_product(request: CreateProductCategoryRequest, db: Session = Depends(get_db)):
    result = provide_product_category_repository(db).create(request)
    return {"product_category": result}

@product_router.posgett("/product_categories/{product_category_id}")
def create_product(pk: int, db: Session = Depends(get_db)):
    result = provide_product_category_repository(db).create(pk)
    return {"product_category": result}