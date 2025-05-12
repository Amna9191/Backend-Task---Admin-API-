# Import necessary libraries
from fastapi import FastAPI
from app.Routers import Products, Inventory , Sales

# Initialize App
app = FastAPI(title="Admin API")

# Include Routers
app.include_router(Products.router)
app.include_router(Inventory.router)
app.include_router(Sales.router)
