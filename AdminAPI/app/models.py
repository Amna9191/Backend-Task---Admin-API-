# Import necessary libraries
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime



# ----------------------------------------
# Define the Table Models
# ----------------------------------------



# Define Products Table
class Product(Base):
    __tablename__ = "products"  # Table name

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    product_name = Column(String, nullable=False)       # Product name (required)
    category = Column(String)                           # Product category
    price = Column(Float)                               # Product price
    time_created = Column(DateTime, default=datetime.utcnow)  # Timestamp of creation



# Define Inventory Table
class Inventory(Base):
    __tablename__ = "inventory"  # Table name

    id = Column(Integer, primary_key=True, index=True)       # Primary key
    product_id = Column(Integer, ForeignKey("products.id"))  # Foreign key to Product
    quantity = Column(Integer)                               # Inventory quantity
    time_updated = Column(DateTime, default=datetime.utcnow) # Timestamp of update

    product = relationship("Product")  # ORM relationship to Product



# Define Sales Table
class Sale(Base):
    __tablename__ = "sales"  # Table name

    id = Column(Integer, primary_key=True, index=True)       # Primary key
    product_id = Column(Integer, ForeignKey("products.id"))  # Foreign key to Product
    sold_quantity = Column(Integer)                          # Quantity sold
    total_price = Column(Float)                              # Total sale amount
    date_sold = Column(Date)                                 # Date of sale

    product = relationship("Product")  # ORM relationship to Product
