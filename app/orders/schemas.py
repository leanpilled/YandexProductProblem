from datetime import date
from pydantic import BaseModel

class SOrders(BaseModel):
    weight: float
    region: int
    time: str
    price: float
    
    class Config:
        orm_mode = True
        
class FOrders(BaseModel):
    weight: float
    region: int
    time: str
    price: float
    status: str
    complition_time: str
    complition_date: date
    courier_id: int
    
    class Config:
        orm_mode = True