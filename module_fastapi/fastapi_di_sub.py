from typing import Optional

from fastapi import FastAPI, Depends, Cookie

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


"""
Using the same dependency multiple times¶

If one of your dependencies is declared multiple times for the same path operation, for example, multiple dependencies 
have a common sub-dependency, FastAPI will know to call that sub-dependency only once per request.

And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific 
request, instead of calling the dependency multiple times for the same request.

In an advanced scenario where you know you need the dependency to be called at every step (possibly multiple times) in the same request instead of using the "cached" value, you can set the parameter use_cache=False when using Depends:
"""

# PYTHONPATH=module_fastapi uvicorn fastapi_di_sub:app --reload
