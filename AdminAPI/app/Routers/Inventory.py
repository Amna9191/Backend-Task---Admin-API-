from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, CRUDs

router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def view_inventory(db: Session = Depends(get_db)):
    return CRUDs.Inventory.get_inventory(db)

@router.put("/update/{product_id}")
def update_inventory(product_id: int, quantity: int, db: Session = Depends(get_db)):
    return CRUDs.Inventory.update_inventory(db, product_id, quantity)
