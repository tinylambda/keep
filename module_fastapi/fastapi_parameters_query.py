from typing import Optional

from fastapi import FastAPI


app = FastAPI()


fake_items_db = [
    {"item_name": "foo"},
    {"item_name": "bar"},
    {"item_name": "baz"},
]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(
    item_id: str, needy: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "needy": needy}
    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "that is an amazing item that has long description"}
        )

    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "that is an amazing item that has long description"}
        )
    return item


# PYTHONPATH=module_fastapi uvicorn fastapi_parameters_query:app --reload
