from typing import Union

from raedyapi import Cookie, RaedyAPI
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}
