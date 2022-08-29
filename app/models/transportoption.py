from sqlalchemy import Column, String
from core.model import Model

class TransportOption(Model):
    alias = Column(String)
    label = Column(String)
