from typing import Union

from raedyapi import RaedyAPI, Header
from typing_extensions import Annotated

app = RaedyAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[
        Union[str, None], Header(convert_underscores=False)
    ] = None
):
    return {"strange_header": strange_header}
