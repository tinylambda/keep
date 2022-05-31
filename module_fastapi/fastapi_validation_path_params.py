from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/{item_id}")
async def read_items2(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=1, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# PYTHONPATH=module_fastapi uvicorn fastapi_validation_path_params:app --reload
