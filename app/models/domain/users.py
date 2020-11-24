from typing import Optional, List
from pydantic import BaseModel

from app.models.domain import Order


class User(BaseModel):
    name: str
    email: Optional[str] = None
    phone: str
    orders: Optional[List[Order]] = []
    past_orders: Optional[List[Order]] = []
