from sqlalchemy import Column,Integer, String,Boolean, ForeignKey
from sqlalchemy.orm import relationship
from core.model import Model

class User(Model):
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    is_active = Column(Boolean(),default=True)
    is_admin = Column(Boolean(),default=False)
