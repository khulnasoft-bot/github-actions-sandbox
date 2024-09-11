from raedyapi import RaedyAPI
from raedyapi.responses import ORJSONResponse

app = RaedyAPI(default_response_class=ORJSONResponse)


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]
