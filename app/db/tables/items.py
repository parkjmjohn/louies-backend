from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.orm import relationship

from app.db.tables.base import Base


class Item(Base):
    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=False)
    description = Column(String, nullable=False)
    allergies = Column(ARRAY(String))
    quantity = Column(Integer)
    user_comment = Column(String)
    order_id = Column(Integer, ForeignKey('order_id'))
