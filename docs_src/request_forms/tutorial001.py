from raedyapi import RaedyAPI, Form

app = RaedyAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
