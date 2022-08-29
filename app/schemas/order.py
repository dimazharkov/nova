from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime
from schemas.incoterm import Incoterm
from schemas.transportmode import TransportMode
from schemas.transportoption import TransportOption
from schemas.currency import Currency
from schemas.status import Status

class OrderBase(BaseModel):
    number : Optional[int] = None
    reference_no : Optional[str] = None
    external_id : Optional[int] = None
    transport_price : Optional[float] = None
    transport_price_currency_id : Optional[int] = None
    cargo_value : Optional[float] = None
    cargo_value_currency_id : Optional[int] = None
    owner_id : Optional[int] = None
    customer_id : Optional[int] = None
    shipper_id : Optional[int] = None
    consignee_id : Optional[int] = None
    incoterm_id : Optional[int] = None
    transport_mode_id : Optional[int] = None
    transport_option_id : Optional[int] = None
    status_id : Optional[int] = None

class OrderCreate(OrderBase):
    number : int
    reference_no : str
    incoterm_id : int
    transport_mode_id : int
    transport_option_id : int
    status_id : int

class OrderUpdate(OrderBase):
    number : int
    reference_no : str
    incoterm_id : int
    transport_mode_id : int
    transport_option_id : int
    status_id : int

class Order(OrderBase):
    number : int
    reference_no : str
    incoterm : Incoterm
    transport_mode : TransportMode
    transport_option : TransportOption
    transport_price_currency : Currency
    cargo_value_currency : Currency
    status : Status

    class Config(): # assure convertion to json
        orm_mode = True
