from typing import Annotated

from raedyapi import RaedyAPI, Form

app = RaedyAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
