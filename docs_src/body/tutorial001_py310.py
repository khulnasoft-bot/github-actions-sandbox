from raedyapi import RaedyAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = RaedyAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
