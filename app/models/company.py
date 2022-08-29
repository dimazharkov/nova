from sqlalchemy import Column, String
from core.model import Model

class Company(Model):
    title = Column(String)
