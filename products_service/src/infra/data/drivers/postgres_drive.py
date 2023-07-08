from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

DATABASE_URL = "postgresql://postgres:sa@localhost/zoom_app_products"  # Replace with your actual connection details

engine = create_engine(DATABASE_URL)
SessionLocal : Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)