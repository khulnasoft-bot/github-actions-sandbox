from raedyapi import RaedyAPI
from raedyapi.responses import ORJSONResponse

app = RaedyAPI()


@app.get("/items/", response_class=ORJSONResponse)
async def read_items():
    return ORJSONResponse([{"item_id": "Foo"}])
