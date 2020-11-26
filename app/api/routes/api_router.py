from fastapi import APIRouter

from app.api.routes import items, orders, users

api_router = APIRouter()

api_router.include_router(items.router, prefix='/items')