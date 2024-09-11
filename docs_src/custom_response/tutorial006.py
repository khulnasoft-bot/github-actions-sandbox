from raedyapi import RaedyAPI
from raedyapi.responses import RedirectResponse

app = RaedyAPI()


@app.get("/cligenius")
async def redirect_cligenius():
    return RedirectResponse("https://cligenius.khulnasoft.com")
