from enum import Enum
from typing import Optional, Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Tags(Enum):
    items = 'items'
    users = 'users'


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()


# @app.post('/items/', response_model=Item, status_code=status.HTTP_201_CREATED, tags=['items'])
@app.post(
    '/items/',
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.items],
    summary='Create an item',
    # description='Create an item with all the information, name, description, price',
    response_description='The created item',
    deprecated=True,
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


# @app.get('/items/', tags=['items'])
@app.get('/items/', tags=[Tags.items])
async def read_items():
    return [{'name': 'Foo', 'price': 42}]


# @app.get('/users/', tags=['users'])
@app.get('/users/', tags=[Tags.users])
async def read_users():
    return {'username': 'johndoe'}

# PYTHONPATH=module_fastapi uvicorn fastapi_path_operation_config:app --reload
