from typing import Optional, List
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    label: str
    description: str
    allegries: Optional[List[str]] = []
    quantity: Optional[int] = 1
    user_comment: Optional[str] = None
    order_id: Optional[int] = None

    class Config:
        orm_mode = True