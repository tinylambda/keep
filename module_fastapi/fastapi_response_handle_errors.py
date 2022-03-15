from fastapi import FastAPI, HTTPException, status, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(status_code=status.HTTP_418_IM_A_TEAPOT, content={
        'message': f'Oops! {exc.name} did something. There goes a rainbow',
    })


@app.exception_handler(RequestValidationError)
async def http_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@app.exception_handler(HTTPException)
async def http_exception_handler2(request: Request, exc: HTTPException):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item not found',
            headers={'X-Error': 'There goes my error'},
        )
    return {'item': items[item_id]}


@app.get('/items2/{item_id}')
async def read_item2(item_id: int):
    if item_id == 3:
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            detail='Nope! I don\'t like 3!',
        )
    return {'item_id': item_id}


@app.get('/unicorns/{name}')
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {'unicorn_name': name}


# PYTHONPATH=module_fastapi uvicorn fastapi_response_handle_errors:app --reload
