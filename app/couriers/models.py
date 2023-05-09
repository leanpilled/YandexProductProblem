from sqlalchemy import Column, Integer, Enum, ARRAY, String
from app.db import Base


class Couriers(Base):
    __tablename__ = "couriers"
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum("FOOT","BIKE","AUTO"), nullable=False)
    regions = Column(ARRAY(Integer), nullable=False)
    working_hours = Column(ARRAY(String), nullable=False)