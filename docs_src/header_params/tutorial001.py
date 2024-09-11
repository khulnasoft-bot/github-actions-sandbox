from typing import Union

from raedyapi import RaedyAPI, Header

app = RaedyAPI()


@app.get("/items/")
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}
