from fastapi import APIRouter

import routes.default as default_routes
import routes.orders as orders_routes

api_router = APIRouter()

api_router.include_router(
    default_routes.router,
    prefix = "",
    tags = ["default"])

api_router.include_router(
    orders_routes.router,
    prefix="/api/orders",
    tags=["orders"]
)
