from typing import Annotated

from raedyapi import RaedyAPI, Query

app = RaedyAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items
