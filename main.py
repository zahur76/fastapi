from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy.orm import Session, session
from sql_app.database import SessionLocal

from schema import Sensors  as SchemaSensor

from sql_app.models import Sensors as ModelSensors

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
def home_page():

    return {"Hello": "World"}


@app.get("/item/{item_id}")
async def read_item(item_id: str):
    """
        view with params
    """
    return {"item_id": item_id}
 


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    """
        View with optional items
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    """
        example post view
    """
    print(item)
    return item


@app.post('/sensors/', response_model=SchemaSensor)
async def sensor(sensor: SchemaSensor, db:Session = Depends(get_db)):
    """
    View to post details for sensor
    """
    db_sensor = ModelSensors(name=sensor.name, unit=sensor.unit)
    db.add(db_sensor)
    db.commit()
    return db_sensor


@app.get('/sensors/')
async def all_sensor(db:Session = Depends(get_db)):
    """
    View to return all sensors
    """
    db_sensor = db.query(ModelSensors).all()
    print(db_sensor)
    return db_sensor

