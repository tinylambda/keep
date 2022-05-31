from typing import List

import yaml
from fastapi import FastAPI, HTTPException, status
from fastapi.requests import Request
from pydantic import BaseModel, ValidationError

app = FastAPI()


def magic_data_reader(raw_body: bytes):
    return {
        "size": len(raw_body),
        "content": {
            "name": "Maaaagic",
            "price": 47,
            "description": "Just kidding, no magic here.",
        },
    }


@app.get("/items/", openapi_extra={"x-aperture-labs-portal": "blue"})
async def read_items():
    return [{"item_id": "portal-gun"}]


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
        }
    },
)
async def create_item(request: Request):
    raw_body = await request.body()
    data = magic_data_reader(raw_body)
    return data


class Item(BaseModel):
    name: str
    tags: List[str]


@app.post(
    "/items2/",
    openapi_extra={
        "requestBody": {
            "content": {"application/yaml": {"schema": Item.schema()}},
            "required": True,
        }
    },
)
async def create_item2(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid YAML"
        )

    try:
        item = Item.parse_obj(data)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.errors()
        )
    return item


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_openapi_extra:app --reload
