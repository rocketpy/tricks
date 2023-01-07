# FastAPI - framework, high performance, easy to learn, fast to code, ready for production

# Documentation: https://fastapi.tiangolo.com
# Source Code: https://github.com/tiangolo/fastapi

# Requirements
"""
Python 3.7+
FastAPI stands on the shoulders of giants:
    Starlette for the web parts.
    Pydantic for the data parts.
"""

# pip install fastapi
# pip install "uvicorn[standard]"

# Run it
# Run the server with:
# $ uvicorn main:app --reload


# Simple Example:

# Create a file main.py with:
from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Example upgrade
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



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
