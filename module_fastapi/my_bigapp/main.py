from fastapi import FastAPI, Depends

from .dependencies import get_query_token, get_token_header
from .routers import users, items
from .internal import admin

app = FastAPI(
    dependencies=[Depends(get_query_token)]
)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix='/admin',
    tags=['admin'],
    dependencies=[Depends(get_token_header)],
    responses={418: {'description': 'I am a teapot'}},
)


@app.get('/')
async def root():
    return {'message': 'Hello Bigger Applications!'}

# PYTHONPATH=module_fastapi uvicorn my_bigapp.main:app --reload
