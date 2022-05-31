from typing import Optional, List, Set, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, item: item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    print([type(x) for x in weights.keys()])  # all int
    return weights


if __name__ == "__main__":
    item1 = Item(name="hello", price=10.2)
    item2 = Item(name="hello2", price=10.3)

    print(item1.tags, id(item1.tags))
    print(item2.tags, id(item2.tags))
    assert id(item1.tags) != id(item2.tags)


# PYTHONPATH=module_fastapi uvicorn fastapi_parameters_body_nested_model:app --reload
