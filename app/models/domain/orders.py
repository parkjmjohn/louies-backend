from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

from app.models.domain import Item
from app.models.domain import Status


class Order(BaseModel):
    items: List[Item]
    status: Status
    time_of_order: datetime
    time_of_pickup: Optional[datetime]
