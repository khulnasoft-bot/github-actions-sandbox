from typing import List, Union

from raedyapi import RaedyAPI, Query

app = RaedyAPI()


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items
