from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def get_inventory(db: Session):
    return db.query(models.Inventory).all()

def update_inventory(db: Session, product_id: int, quantity: int):
    inventory = db.query(models.Inventory).filter(models.Inventory.product_id == product_id).first()
    if inventory:
        inventory.quantity = quantity
        inventory.updated_at = datetime.utcnow()
    else:
        inventory = models.Inventory(product_id=product_id, quantity=quantity)
        db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory
