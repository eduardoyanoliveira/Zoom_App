from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from domain.entities.Product import ProductCategory

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_price = Column(Float)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    created_at = Column(DateTime)

    category = relationship(ProductCategory)