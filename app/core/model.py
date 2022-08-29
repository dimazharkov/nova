# from https://docs.sqlalchemy.org/en/14/orm/mapping_api.html#sqlalchemy.orm.as_declarative
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, DateTime
import datetime

@as_declarative()
class Model:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)
