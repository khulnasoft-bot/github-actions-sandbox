from raedyapi import RaedyAPI, Form
from typing_extensions import Annotated

app = RaedyAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
