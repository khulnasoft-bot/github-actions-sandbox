from typing import Union

from raedyapi import RaedyAPI, Query
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
