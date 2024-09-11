from typing import List, Union

from raedyapi import RaedyAPI, Query
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items
