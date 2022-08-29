from sqlalchemy.orm import Session
from models.order import Order
import schemas.order as schema

def create(order: schema.OrderCreate, db: Session):
    order = Order(**order.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def read(id: int, db: Session):
    return db.query(Order).filter(Order.id == id).first()

def update(id: int, order: schema.OrderUpdate, db: Session):
    existing = db.query(Order).filter(Order.id == id)
    if not existing.first():
        return False
    existing.update(order.__dict__)
    db.commit()
    return True

def delete(id: int, db: Session):
    existing = db.query(Order).filter(Order.id == id)
    if not existing.first():
        return False
    existing.delete(synchronize_session=False)
    db.commit()
    return True

def list(db: Session):
    return db.query(Order).all()
