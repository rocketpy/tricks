# FastAPI - framework, high performance, easy to learn, fast to code, ready for production

# Documentation: https://fastapi.tiangolo.com
# Source Code: https://github.com/tiangolo/fastapi

# Requirements
"""
Python 3.7+
FastAPI stands on the shoulders of giants:
    Starlette for the web parts.
    Pydantic for the data parts.

Optional Dependencies:

Used by Pydantic:
    ujson - for faster JSON "parsing".
    email_validator - for email validation.

Used by Starlette:
    httpx - Required if you want to use the TestClient.
    jinja2 - Required if you want to use the default template configuration.
    python-multipart - Required if you want to support form "parsing", with request.form().
    itsdangerous - Required for SessionMiddleware support.
    pyyaml - Required for Starlette's SchemaGenerator support (you probably don't need it with FastAPI).
    ujson - Required if you want to use UJSONResponse.

Used by FastAPI / Starlette:
    uvicorn - for the server that loads and serves your application.
    orjson - Required if you want to use ORJSONResponse.

- Install all of these with pip install "fastapi[all]".

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


# Path Operation Advanced Configuration
# unique for each operation.
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", operation_id="some_specific_id_you_define")
async def read_items():
    return [{"item_id": "Foo"}]


# Using the path operation function name as the operationId
from fastapi import FastAPI
from fastapi.routing import APIRoute

app = FastAPI()


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]

def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'

use_route_names_as_operation_ids(app)


# Exclude from OpenAPI
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", include_in_schema=False)
async def read_items():
    return [{"item_id": "Foo"}]


# Advanced description from docstring
from typing import Set, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
        
@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item


# OpenAPI Extensions
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/", openapi_extra={"x-aperture-labs-portal": "blue"})
async def read_items():
    return [{"item_id": "portal-gun"}]


# Custom OpenAPI path operation schema
from fastapi import FastAPI, Request

app = FastAPI()


def magic_data_reader(raw_body: bytes):
    return {
        "size": len(raw_body),
        "content": {
            "name": "Maaaagic",
            "price": 42,
            "description": "Just kiddin', no magic here. ✨",
        },
    }

@app.post(
    "/items/",
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "required": ["name", "price"],
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "price": {"type": "number"},
                            "description": {"type": "string"},
                        },
                    }
                }
            },
            "required": True,
        },
    },
)
async def create_item(request: Request):
    raw_body = await request.body()
    data = magic_data_reader(raw_body)
    return data


# Custom OpenAPI content type
from typing import List
import yaml
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Item(BaseModel):
    name: str
    tags: List[str]


@app.post(
    "/items/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml": {"schema": Item.schema()}},
            "required": True,
        },
    },
)

async def create_item(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    try:
        item = Item.parse_obj(data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    return item


#
from typing import List
import yaml
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError

app = FastAPI()


class Item(BaseModel):
    name: str
    tags: List[str]


@app.post(
    "/items/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml": {"schema": Item.schema()}},
            "required": True,
        },
    },
)


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
