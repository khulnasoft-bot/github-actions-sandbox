from raedyapi import RaedyAPI
from raedyapi.responses import RedirectResponse

app = RaedyAPI()


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
