# FastAPI - framework, high performance, easy to learn, fast to code, ready for production

# pip install fastapi

# example taked here: https://habr.com/ru/post/708678/
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int):
    return JSONResponse({"item": item.dict(), "item_id": item_id})

@app.get("/")
async def homepage():
    return JSONResponse({'hello': 'world'})

@app.get("/get_items/{item_id}")
async def read_item(item_id: int):
    print("item_id", item_id)
    return {"item_id": item_id}
