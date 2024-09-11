from typing import Union

from raedyapi import RaedyAPI, Response
from raedyapi.responses import RedirectResponse

app = RaedyAPI()


@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}
