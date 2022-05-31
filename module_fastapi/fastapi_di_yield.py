import random

from fastapi import Depends, FastAPI


async def dependency_a():
    session_a = random.randint(1, 100)
    try:
        yield session_a
    finally:
        del session_a


async def dependency_b(dep_a=Depends(dependency_a)):
    session_b_with_a = f"{dep_a}_{random.randint(1, 100)}"
    try:
        yield session_b_with_a
    finally:
        del session_b_with_a


async def dependency_c(dep_b=Depends(dependency_b)):
    session_c_with_b = f"{dep_b}_{random.randint(1, 100)}"
    try:
        yield session_c_with_b
    finally:
        del session_c_with_b


app = FastAPI()


@app.get("/items/")
async def read_items(c_value: str = Depends(dependency_c)):
    return [
        {"c_value": c_value},
    ]


# PYTHONPATH=module_fastapi uvicorn fastapi_di_yield:app --reload
