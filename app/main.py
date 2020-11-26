from fastapi import FastAPI

from app.api.routes.api_router import api_router

app = FastAPI()
app.include_router(api_router)