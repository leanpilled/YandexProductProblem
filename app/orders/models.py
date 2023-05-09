from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.db import Base


class Orders(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    weight = Column(Float, nullable=False)
    region = Column(Integer, nullable=False)
    time = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="PENDING", nullable=True)
    complition_time = Column(String, nullable=True)
    complition_date = Column(Date, nullable=True)
    courier_id = Column(Integer, ForeignKey("couriers.id"),nullable=True)