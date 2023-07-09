from sqlalchemy import Boolean, Column, ForeignKey, Integer, MetaData, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base(metadata=MetaData())

class BaseDbModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProductCategoryModel(BaseDbModel):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    products = relationship("ProductModel", back_populates="category")


class ProductModel(BaseDbModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    base_price = Column(Float)
    is_stored = Column(Boolean)
    amount = Column(Integer, nullable=True)

    category_id = Column(Integer, ForeignKey("product_category.id"))
    category = relationship("ProductCategoryModel", back_populates="products")
