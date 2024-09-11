from raedyapi import RaedyAPI

app = RaedyAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
