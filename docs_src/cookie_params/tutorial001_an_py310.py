from typing import Annotated

from raedyapi import Cookie, RaedyAPI

app = RaedyAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
