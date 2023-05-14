from datetime import date
from pydantic import BaseModel

class SAssignments(BaseModel):
    
    courier_id: int
    time: str
    order_ids: list[int]
    date: date
    
    class Config:
        orm_mode = True