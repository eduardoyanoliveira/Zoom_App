from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from domain_services.DependencyInjectionContainer import provide_list_products_command
from infra.DependencyInjectionContainer import get_db

product_router = APIRouter()

@product_router.get("/")
def index():
    command = provide_list_products_command()
    products = command.execute()
    return products

@product_router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = product_repository(db).get_product_by_id(product_id)
    return {"product": product}

@product_router.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = product_repository(db).create_product(product)
    return {"product": created_product}