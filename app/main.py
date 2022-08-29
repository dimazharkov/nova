from fastapi import FastAPI
from core.config import settings
from core.router import api_router
from db.session import engine
from models.base import Model

def include_router(app):
	app.include_router(api_router)

def create_tables():
	Model.metadata.create_all(
		bind = engine
	)

def start_application():
	app = FastAPI(
		title = settings.PROJECT_NAME,
		version = settings.PROJECT_VERSION
	)
	include_router(app)
	create_tables()
	return app

app = start_application()
