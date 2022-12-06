from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


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
    print(item)
    return item
