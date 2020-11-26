from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, ARRAY
from sqlalchemy.orm import relationship

from app.db.tables.base import Base
from app.db.tables.users import User
from app.db.tables.items import Item


class Order(Base):
    id = Column(Integer, primary_key=True)
    items = Column(ARRAY(Item), nullable=False)
    status = Column(String, nullable=False)
    time_of_order = Column(DateTime, nullable=False)
    time_of_pickup = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('User', back_populates='orders')