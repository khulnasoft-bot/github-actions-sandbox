from raedyapi import RaedyAPI

app = RaedyAPI()


@app.get("/")
async def root():
    return {"message": "Tomato"}
