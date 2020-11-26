from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.orm import relationship

from app.db.tables.base import Base
from app.db.tables.orders import Order


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    orders = relationship('Order', back_populates='owner')
    past_orders = ARRAY(Order)