from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from typing import Generator

engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine
