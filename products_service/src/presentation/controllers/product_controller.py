from fastapi import APIRouter

from domain_services.DependencyInjectionContainer import provide_list_products_command

product_router = APIRouter()

@product_router.get("/")
def index():
    command = provide_list_products_command()
    products = command.execute()
    return products