from typing import List, Union

from raedyapi import RaedyAPI, Header
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}
