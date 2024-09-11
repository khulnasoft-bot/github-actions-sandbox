from raedyapi import RaedyAPI, status

app = RaedyAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
