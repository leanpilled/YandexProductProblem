from enum import Enum
from pydantic import BaseModel

class CourierType(str, Enum):
    FOOT = "FOOT"
    BIKE = "BIKE"
    AUTO = "AUTO"

class SCouriers(BaseModel):
    type: CourierType
    regions: list[int]
    working_hours: list[str]
    
    class Config:
        orm_mode = True