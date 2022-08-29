from sqlalchemy import Column, String
from core.model import Model

class Incoterm(Model):
    alias = Column(String)
    label = Column(String)
