from typing import Optional

from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse

app = FastAPI()

items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}


@app.put("/items/{item_id}")
async def upsert_item(
    item_id: str, name: Optional[str] = Body(None), size: Optional[int] = Body(None)
):
    if item_id in items:
        item = items[item_id]
        item[name] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_additional_status_code:app --reload
