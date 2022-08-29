from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from core.model import Model

class Status(Model):
    name  = Column(String)
    color_text  = Column(String)
    color_bg  = Column(String)
    icon_name  = Column(String)    
