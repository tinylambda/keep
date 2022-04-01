from fastapi import FastAPI

app = FastAPI()


@app.get('/app')
def read_main():
    return {'message': 'Hello world from main app'}


subapi = FastAPI()


@subapi.get('/sub')
def read_sub():
    return {'message': 'Hello world from sub API'}


app.mount('/subapi', subapi)

# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_mount:app --reload
