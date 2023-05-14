from sqlalchemy import Column, Integer, ARRAY, String, ForeignKey, Date
from app.db import Base


class Assignments(Base):
    __tablename__ = "assignments"
    
    id = Column(Integer, primary_key=True)
    courier_id = Column(Integer, ForeignKey("couriers.id"))
    time = Column(String, nullable=False)
    order_id = Column(ARRAY(Integer), nullable=False)
    date = Column(Date, nullable=False)