from sqlalchemy import Column, String
from core.model import Model

class TransportMode(Model):
    alias = Column(String)
    label = Column(String)
