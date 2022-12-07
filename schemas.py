from pydantic import BaseModel
from typing import List



class Sensor(BaseModel):
    name: str
    unit: str

    class Config:
        orm_mode = True