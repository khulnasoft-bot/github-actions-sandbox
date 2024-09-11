from raedyapi import RaedyAPI
from raedyapi.responses import UJSONResponse

app = RaedyAPI()


@app.get("/items/", response_class=UJSONResponse)
async def read_items():
    return [{"item_id": "Foo"}]
