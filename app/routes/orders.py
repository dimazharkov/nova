import core.auth as auth
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from models.order import Order
from models.user import User
import schemas.order as schema
import repositories.order as repository

router = APIRouter()

# create
@router.post("/", response_model = schema.Order,  status_code = status.HTTP_201_CREATED)
def create_order(order: schema.OrderCreate, db:Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    return repository.create(order = order, db = db)

# read
@router.get("/{id}", response_model = schema.Order)
def read_order(id:int, db:Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    order = repository.read(id = id, db = db)
    if not order:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Order [id={id}] is undefined"
        )
    return order

# update
@router.put("/{id}")
def update_order(id: int, order: schema.OrderUpdate, db:Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    if not user.is_admin:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = f"Acceess denied",
        )
    result = repository.update(id = id, order = order,  db = db)
    if not result:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Order [id={id}] is undefined"
        )
    return {"result": "updated successfully"}

# delete
@router.delete("/{id}")
def delete_order(id: int,db: Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    if not user.is_admin:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = f"Acceess denied",
        )
    result = repository.delete(id = id, db = db)
    if not result:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Order [id={id}] is undefined"
        )
    return {"result": "deleted successfully"}

# list
@router.get("/" ,response_model = List[schema.Order])
def list_orders(db:Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    return repository.list(db = db)
