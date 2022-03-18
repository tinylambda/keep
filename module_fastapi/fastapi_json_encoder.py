from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}

app = FastAPI()


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str]


@app.put('/items/{id}')
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    print(json_compatible_item_data, '!')
    fake_db[id] = json_compatible_item_data


# PYTHONPATH=module_fastapi uvicorn fastapi_json_encoder:app --reload
