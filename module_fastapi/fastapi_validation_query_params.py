from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex='^fixedquery$')):
async def read_items(
    q: Optional[str] = Query(
        ...,
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        title="Query string",
        description="the items to search in the database that have a good match",
        alias="item-query",
        deprecated=True,
    ),
    m: Optional[List[str]] = Query(None),
    strs: List[str] = Query(["foo", "bar"]),
    hidden_query: Optional[str] = Query(None, include_in_schema=False),
):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    if m:
        results.update({"m": m})

    results.update({"strs": strs})

    if hidden_query:
        results.update({"hidden_query": hidden_query})

    return results


# PYTHONPATH=module_fastapi uvicorn fastapi_validation_query_params:app --reload
