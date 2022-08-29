import core.auth as auth
from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database
from core.config import settings

from db.session import get_db
from models.currency import Currency
from models.status import Status
from models.incoterm import Incoterm
from models.transportmode import TransportMode
from models.transportoption import TransportOption
from models.user import User
from models.order import Order

router = APIRouter()

@router.get("/")
async def home(request: Request):
    return {"message": "You are on index hook"}

# seeding some data
@router.get("/init")
async def init(db: Session = Depends(get_db), user: User = Depends(auth.get_current_user)):
    if not user.is_admin:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = f"Acceess denied",
        )

    #if database_exists(settings.DB_URL):
    #    return {"result": "db is already initiated"}

    #create_database(settings.DB_URL)

    db.add(Currency(
        label = "PLN"
    ))
    db.add(Status(
        name = "New",
        color_text = "black",
        color_bg = "white",
        icon_name = "new.png"
    ))
    db.add(Status(
        name = "In Process",
        color_text = "black",
        color_bg = "yellow",
        icon_name = "process.png"
    ))
    db.add(Incoterm(
        alias = "FCA",
        label = "Free Carrier"
    ))
    db.add(TransportMode(
        alias = "SEA",
        label = "Sea"
    ))
    db.add(TransportOption(
        alias = "FTL",
        label = "Full Truckload"
    ))
    db.add(Order(
        number = 1001,
        reference_no = "ref: 123",
        external_id = 0,
        transport_price = 1000,
        transport_price_currency_id = 1,
        cargo_value = 1000,
        cargo_value_currency_id = 1,
        incoterm_id = 1,
        transport_mode_id = 1,
        transport_option_id = 1,
        status_id = 1
    ))
    db.add(Order(
        number = 1002,
        reference_no = "ref: 100-1-1",
        external_id = 0,
        transport_price = 22000,
        transport_price_currency_id = 1,
        cargo_value = 22000,
        cargo_value_currency_id = 1,
        incoterm_id = 1,
        transport_mode_id = 1,
        transport_option_id = 1,
        status_id = 2
    ))
    db.commit()

    return {"result": "initiated successfully"}
