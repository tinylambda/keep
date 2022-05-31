"""
"Dependency Injection" means, in programming, that there is a way for your code (in this case,
 your path operation functions) to declare things that it requires to work and use: "dependencies".

 And then, that system (in this case FastAPI) will take care of doing whatever is needed to provide
 your code with those needed dependencies ("inject" the dependencies).

 This is very useful when you need to:

    Have shared logic (the same code logic again and again).
    Share database connections.
    Enforce security, authentication, role requirements, etc.
    And many other things...
 All these, while minimizing code repetition.
"""
from typing import Optional

from fastapi import FastAPI, Depends

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


"""
Whenever a new request arrives, FastAPI will take care of:

    Calling your dependency ("dependable") function with the correct parameters.
    Get the result from your function.
    Assign that result to the parameter in your path operation function.

"""


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


# PYTHONPATH=module_fastapi uvicorn fastapi_di_first:app --reload
