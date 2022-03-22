import time

from fastapi import FastAPI
from fastapi.requests import Request

app = FastAPI()


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response


@app.get('/items/')
async def read_items():
    return [
        {'item': 'Portal Gun'},
        {'item': 'Plumbus'},
    ]

# PYTHONPATH=module_fastapi uvicorn fastapi_middleware:app --reload
