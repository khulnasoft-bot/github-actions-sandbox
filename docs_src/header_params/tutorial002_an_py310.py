from typing import Annotated

from raedyapi import RaedyAPI, Header

app = RaedyAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
):
    return {"strange_header": strange_header}
