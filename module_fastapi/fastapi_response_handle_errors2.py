from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import BaseModel

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f'OMG! An HTTP error: {repr(exc)}')
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f'OMG! The client sent invalid data: {exc}')
    return await request_validation_exception_handler(request, exc)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({
#             'detail': exc.errors(),
#             'body': exc.body
#         }))


class Item(BaseModel):
    title: str
    size: int


@app.post('/items/')
async def create_item(item: Item):
    return item


# PYTHONPATH=module_fastapi uvicorn fastapi_response_handle_errors2:app --reload
