from raedyapi import RaedyAPI, Query

app = RaedyAPI()


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
