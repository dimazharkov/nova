from sqlalchemy import Column, String
from core.model import Model

class Currency(Model):
    label = Column(String)
