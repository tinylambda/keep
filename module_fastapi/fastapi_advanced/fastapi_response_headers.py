from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse

app = FastAPI()


@app.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["X-Cat-Dog"] = "alone in the world"
    return {"message": "Hello World"}


@app.get("/headers/")
def get_headers2():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog2": "alone in the world 2", "Content-Language": "zh-CN"}
    return JSONResponse(content=content, headers=headers)


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_response_headers:app --reload
