from raedyapi import Cookie, RaedyAPI

app = RaedyAPI()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}
