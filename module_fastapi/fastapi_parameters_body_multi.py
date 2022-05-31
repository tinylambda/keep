from typing import Optional

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get"),
    ge=0,
    le=1000,
    q: Optional[str] = None,
    item: Optional[Item] = None,
    user: User,
    importance: int = Body(...),  # put it in the body
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})

    if item:
        results.update({"item": item})

    results.update({"user": user, "importance": importance})

    return results


# PYTHONPATH=module_fastapi uvicorn fastapi_parameters_body_multi:app --reload
