from typing import Optional
from pydantic import BaseModel

class TransportMode(BaseModel):
    alias : str
    label : str

    class Config(): # assure convertion to json
        orm_mode = True
