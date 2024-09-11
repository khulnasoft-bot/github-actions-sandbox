from typing import List

from raedyapi import RaedyAPI, Query
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items
