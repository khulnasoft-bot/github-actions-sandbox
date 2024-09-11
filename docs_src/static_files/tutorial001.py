from raedyapi import RaedyAPI
from raedyapi.staticfiles import StaticFiles

app = RaedyAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
