from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import schemas, CRUDs

router = APIRouter(prefix="/sales", tags=["Sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Sale)
def add_sale(sale: schemas.Sale, db: Session = Depends(get_db)):
    return CRUDs.Sales.record_sale(db, sale)

@router.get("/", response_model=list[schemas.Sale])
def get_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return CRUDs.Sales.get_sales(db, skip, limit)
