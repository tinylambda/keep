from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse

app = FastAPI()


@app.post(
    "/cookie-and-object/",
)
def create_cookie(response: Response):
    response.set_cookie(key="fakesession", value="s-value")
    return {"message": "Come to the dark side, we have cookie"}


@app.post("/cookie/")
def create_cookie_direct():
    content = {"message": "oh cookie"}
    response = JSONResponse(content=content)
    response.set_cookie(key="s-key", value="s-value")
    return response


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_response_parameter:app --reload
