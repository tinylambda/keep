from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""


tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


app = FastAPI(
    title="Good API",
    description=description,
    version="0.0.1",
    terms_of_service="http://localhost/terms/",
    contact={
        "name": "Felix",
        "url": "http://localhost/contact",
        "email": "felix@localhost.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    docs_url="/documentation",
    redoc_url=None,
)


@app.get("/items/", tags=["items"])
async def read_items():
    return [
        {"name": "Katana"},
    ]


@app.get("/users/", tags=["users"])
async def get_users():
    return [
        {"name": "Felix"},
    ]


app.mount("/static", StaticFiles(directory="/tmp"), name="static")
