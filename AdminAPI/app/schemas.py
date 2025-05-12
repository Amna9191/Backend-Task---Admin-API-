# Import necessary libraries
from pydantic import BaseModel
from datetime import datetime, date


# ------------------------------
# Define Schemas for the Tables
# ------------------------------


# -------------------------
# Product Schemas
# -------------------------

# Shared properties for creating/updating products
class ProductBase(BaseModel):
    product_name: str
    category: str
    price: float

# Schema for creating a product (inherits from ProductBase)
class ProductCreate(ProductBase):
    pass

# Schema for reading product data (includes id and timestamp)
class Product(ProductBase):
    id: int
    time_created: datetime

    class Config:
        orm_mode = True



# -------------------------
# Inventory Schemas
# -------------------------

# Schema for inventory
class InventoryBase(BaseModel):
    product_id: int
    quantity: int

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    time_updated: datetime

    class Config:
        orm_mode = True



# -------------------------
# Sale Schemas
# -------------------------

# Schema for sales
class SaleBase(BaseModel):
    product_id: int
    sold_quantity: int
    total_price: float
    date_sold: date

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True
