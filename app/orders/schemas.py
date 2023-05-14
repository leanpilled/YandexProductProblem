from pydantic import BaseModel, Field
from typing import Optional

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
    complition_time: Optional[str] = Field(..., nullable=True)
    courier_id: Optional[int] = Field(..., nullable=True)
    
    class Config:
        orm_mode = True