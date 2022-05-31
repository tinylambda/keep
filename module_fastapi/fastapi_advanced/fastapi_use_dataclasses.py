from dataclasses import dataclass, field
from typing import Optional, List

from fastapi import FastAPI

app = FastAPI()


@dataclass
class Item:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    description: Optional[str] = None
    tax: Optional[float] = None


# BUG: https://github.com/tiangolo/fastapi/issues/4117
# @app.post('/items/')
# async def create_item(item: Item):
#     return item


@app.get("/items/next", response_model=Item)
async def read_next_item():
    return {
        "name": "Hello world",
        "price": 12.99,
        "description": "Hi",
        "tags": ["tag1"],
    }


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_use_dataclasses:app --reload
