from raedyapi import RaedyAPI
from raedyapi.responses import RedirectResponse

app = RaedyAPI()


@app.get("/pydantic", response_class=RedirectResponse, status_code=302)
async def redirect_pydantic():
    return "https://pydantic-docs.helpmanual.io/"
