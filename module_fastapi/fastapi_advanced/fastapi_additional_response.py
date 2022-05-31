from typing import Optional

from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={status.HTTP_404_NOT_FOUND: {"model": Message}},
)
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "Item not found"}
        )


IMAGE_FILE = "/home/felix/Downloads/python.png"


@app.get(
    "/items2/{item_id}",
    responses={
        status.HTTP_200_OK: {
            "content": {"image/png": {}},
            "description": "Return the JSON item or an image.",
        }
    },
)
async def read_item2(item_id: str, img: Optional[bool] = None):
    if img:
        return FileResponse(IMAGE_FILE, media_type="image/png")
    else:
        return {"id": "foo", "value": "there goes my hero"}


@app.get(
    "/items3/{item_id}",
    response_model=Item,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": Message,
            "description": "The item was not found",
        },
        status.HTTP_200_OK: {
            "description": "Item requested by ID",
            "content": {
                "application/json": {
                    "example": {"id": "bar", "value": "the bar tenders"},
                }
            },
        },
    },
)
async def read_item3(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found')
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Item is not found"},
        )


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_additional_response:app --reload
