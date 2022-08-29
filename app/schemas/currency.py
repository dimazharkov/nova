from typing import Optional
from pydantic import BaseModel

class Currency(BaseModel):
    label : str

    class Config(): # assure convertion to json
        orm_mode = True
