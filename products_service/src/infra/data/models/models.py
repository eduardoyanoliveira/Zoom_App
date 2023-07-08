from sqlalchemy import Boolean, Column, ForeignKey, Integer, MetaData, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base(metadata=MetaData())

class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    products = relationship("Product", back_populates="category")



class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    base_price = Column(Float)
    is_stored = Column(Boolean)
    amount = Column(Integer, nullable=True)

    category_id = Column(Integer, ForeignKey("product_category.id"))
    category = relationship("ProductCategory", back_populates="products")
