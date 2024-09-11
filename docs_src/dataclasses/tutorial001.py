from dataclasses import dataclass
from typing import Union

from raedyapi import RaedyAPI


@dataclass
class Item:
    name: str
    price: float
    description: Union[str, None] = None
    tax: Union[float, None] = None


app = RaedyAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
