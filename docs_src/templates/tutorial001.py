from raedyapi import RaedyAPI, Request
from raedyapi.responses import HTMLResponse
from raedyapi.staticfiles import StaticFiles
from raedyapi.templating import Jinja2Templates

app = RaedyAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
