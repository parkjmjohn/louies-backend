from typing import Optional, List
from pydantic import BaseModel, EmailStr

from app.models.schemas import Order


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = EmailStr
    phone: str
    orders: Optional[List[Order]] = []
    past_orders: Optional[List[Order]] = []

    class Config:
        orm_mode = True