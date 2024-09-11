from typing import Annotated, Union

from raedyapi import RaedyAPI, Query

app = RaedyAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        Union[str, None], Query(min_length=3, max_length=50, regex="^fixedquery$")
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
