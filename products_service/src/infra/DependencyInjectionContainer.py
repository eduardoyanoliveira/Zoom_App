from domain_services.Abstracts.Product.AbstractProductRepository import AbstractProductRepository
from domain_services.Abstracts.ProductCategory.AbstractProductCategoryRepository import AbstractProductCategoryRepository
from infra.data.drivers.postgres_drive import SessionLocal
from infra.data.repos.ProductCategoryRepository import ProductCategoryRepository
from infra.data.repos.ProductRepository import ProductRepository
from sqlalchemy.orm import Session


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def provide_product_category_repository(db: Session) -> AbstractProductCategoryRepository:
    return ProductCategoryRepository(db)

def provide_product_repository(db : Session) -> AbstractProductRepository:
    return ProductRepository(db)
