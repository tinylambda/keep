from typing import Optional

from fastapi import FastAPI, Header, HTTPException, status, Depends
from pydantic import BaseModel

fake_secret_token = "coneofsilence"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

app = FastAPI()


class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None


async def check_x_token_header(x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid X-Token header"
        )
    return x_token


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.get("/items/{item_id}", response_model=Item)
async def read_main2(item_id: str, x_token: str = Depends(check_x_token_header)):
    if item_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return fake_db[item_id]


@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Depends(check_x_token_header)):
    if item.id in fake_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists"
        )
    fake_db[item.id] = item
    return item
