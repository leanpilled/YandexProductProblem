from pydantic import BaseModel


class SCouriers(BaseModel):
    type: str
    regions: list[int]
    working_hours: list[str]
    
    class Config:
        orm_mode = True