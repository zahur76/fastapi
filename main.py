from typing import Union
from fastapi import FastAPI


app = FastAPI()


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
