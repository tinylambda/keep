from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello world'}


# PYTHONPATH=module_fastapi uvicorn fastapi_helloworld:app --reload
