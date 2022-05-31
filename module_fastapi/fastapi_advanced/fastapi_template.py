from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="module_fastapi/fastapi_advanced/static"),
    name="static",
)

templates = Jinja2Templates(directory="module_fastapi/fastapi_advanced/templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


# PYTHONPATH=module_fastapi/fastapi_advanced uvicorn fastapi_template:app --reload
