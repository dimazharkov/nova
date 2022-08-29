from typing import Optional
from pydantic import BaseModel

class Status(BaseModel):
    name : str
    color_text : str
    color_bg : str
    icon_name : str

    class Config(): # assure convertion to json
        orm_mode = True
