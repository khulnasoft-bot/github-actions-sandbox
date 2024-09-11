from raedyapi import RaedyAPI

app = RaedyAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
