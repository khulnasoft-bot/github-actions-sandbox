from raedyapi import RaedyAPI
from raedyapi.responses import RedirectResponse

app = RaedyAPI()


@app.get("/raedyapi", response_class=RedirectResponse)
async def redirect_raedyapi():
    return "https://raedyapi.khulnasoft.com"
