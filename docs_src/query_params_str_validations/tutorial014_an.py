from typing import Union

from raedyapi import RaedyAPI, Query
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
