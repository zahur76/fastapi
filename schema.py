# build a schema using pydantic
from pydantic import BaseModel

class Sensors(BaseModel):
    name: str
    unit: str

    class Config:
        orm_mode = True
        