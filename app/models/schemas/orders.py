from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

from app.models.schemas import Item
from app.models.struct import Status


class Order(BaseModel):
    id: int
    user_id: int
    items: List[Item]
    status: Status
    time_of_order: datetime
    time_of_pickup: Optional[datetime]

    class Config:
        orm_mode = True